#!/Python27/python
import cgi
import cgitb
import re
import time

cgitb.enable()



sep='|'

print "Content-Type: text/html"
print "Cache-control: no-cache"
print

print '<HTML><head><title>Sandwich Queue!</title><!--meta http-equiv="refresh" content="5" --></head>\n<body>\n<H3>Sandwich Queue!</H3>\n'

#layout of queue "database" <name> | <bread> | <cheese, comma sep> | <toppings, comma sep> | unixTime of order\n
#There will be 3 queue "database" files, completed, in progress, and queue
#.lock files will exist for each "database" file

sanatizer = re.compile('[^a-zA-Z0-9_ ,\\|]')



#values:bread, cheese, toppings, name


fs = cgi.FieldStorage()
name = fs["name"].value
bread = fs["bread"].value
cheese = fs["cheese"].value
toppings = fs["toppings"].value

print name
print bread
print cheese
print toppings
print time.time()

#file = open("JacobList.txt", "r")

print '<table style="width:100%" border="1">'
print '<tr>\n <th colspan="4"> In Progress </th></tr>'
print "<tr>\n <th>Name</th>\n <th>Bread</th>\n <th>Cheese</th>\n <th>Toppings</th>\n</tr>"
print inprogressTable
print '<tr>\n <th colspan="4"> Queue </th></tr>'
print "<tr>\n <th>Name</th>\n <th>Bread</th>\n <th>Cheese</th>\n <th>Toppings</th>\n</tr>"
print makeTableLines(queue)
print '<tr>\n <th colspan="4"> Completed </th></tr>'
print "<tr>\n <th>Name</th>\n <th>Bread</th>\n <th>Cheese</th>\n <th>Toppings</th>\n</tr>"
print completedTable
print '</table>'

print '<h3>Request a sandwich!</h3>'
print '<FORM method="post" action="/cgi-bin/grilledCheese/order.py">'
print '<table border="1">\n <tr>\n  <th>Bread</th>\n  <th>Cheese (up to 2)</th>\n  <th>Toppings</th>\n </tr>'
print '  <td>'
columnCheckTable("bread", breads)
print '  </td>'
print '  <td>'
columnCheckTable("cheese", cheeses)
print '  </td>'
print '  <td>'
columnCheckTable("toppings", toppings, 3)
print '   Custom: <input type="text" name=toppings[]>'
print '  </td></tr>'
print '  <tr>'
print '   <td colspan="3"> Name: <input type="text" name="name"></td></tr>'
print ' </table>'
print ' '
print '</body>'


# cpy-paste form example
#        print ("<FORM method=\"post\" action=\"/cgi-bin/jPurchased.py\">{}<INPUT type=\"hidden\" name=\"line\" value=\"{}\">"
#              "<INPUT type=\"submit\" value=\"Mark as purchased\"></FORM>\n").format(m.group(1), i)


