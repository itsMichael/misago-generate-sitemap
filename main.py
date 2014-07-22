from lxml import etree
import MySQLdb

root = etree.Element('urlset')

print "Connect to database..."

conn = MySQLdb.connect("host", "user", "pass", "name-database") #change

print "Download data..."

c = conn.cursor()
c.execute("SELECT slug, last, start_post_id FROM misago_thread")

print "Create xml file..."

for a in c:
	url = etree.Element('url')
	loc = etree.Element('loc')
	pr = etree.Element('priority')
	last = etree.Element('lastmod')
	loc.text = "http://yoursite.pl/thread/"+a[0]+"-"+str(a[2])
	pr.text = "0.5"
	last.text = str(a[1])

	url.append(loc)
	url.append(pr)
	url.append(last)
	
	root.append(url)


s = etree.tostring(root, pretty_print=True)

et = etree.ElementTree(root)
et.write("sitemap.xml")

print "Finish!"
