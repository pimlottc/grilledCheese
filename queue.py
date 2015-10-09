#!/Python27/python
import cgi
import cgitb
import re

cgitb.enable()

def printQueue(file):
    valid = re.compile('(.*)\\|(.*)\\|(.*)\\|(.*)')
    sanatizer = re.compile('[^a-zA-Z0-9_ ,\\|]')
    for line in file:
        line = sanatizer.sub('', line)
        m = valid.match(line)
        if m:
            print ("<tr>\n <td>{}</td>\n <td>{}</td>\n <td>{}</td>\n <td>{}</td>\n</tr>".format(m.group(1), m.group(2), m.group(3), m.group(4)))

print "Content-Type: text/html"
print "Cache-control: no-cache"
print

print '<HTML><head><title>Sandwich Queue!</title><meta http-equiv="refresh" content="5" ></head>\n<body>\n<H3>Sandwich Queue!</H3>\n'

#layout of queue "database" <name> | <bread> | <cheese, comma sep> | <toppings, comma sep>\n
#There will be 3 queue "database" files, completed, in progress, and queue
#.lock files will exist for each "database" file

print '<meta http-equiv="refresh" content="5" >'

queue = open('/usr/lib/WebData/queue.txt', "r")
completed = open('/usr/lib/WebData/completed.txt', "r")
inprogress = open('/usr/lib/WebData/inprogress.txt', "r")

#file = open("JacobList.txt", "r")

print '<table style="width:100%">'
print '<tr>\n <th rowspan="4"> In Progress </th></tr>'
print "<tr>\n <th>Name</th>\n <th>Bread</th>\n <th>Cheese</th>\n <th>Toppings</th>\n</tr>"
printQueue(inprogress)
print '<tr>\n <th rowspan="4"> Queue </th></tr>'
print "<tr>\n <th>Name</th>\n <th>Bread</th>\n <th>Cheese</th>\n <th>Toppings</th>\n</tr>"
printQueue(queue)
print '<tr>\n <th rowspan="4"> Completed </th></tr>'
print "<tr>\n <th>Name</th>\n <th>Bread</th>\n <th>Cheese</th>\n <th>Toppings</th>\n</tr>"
printQueue(completed)
print '</table></body>'

# cpy-paste form example
#        print ("<FORM method=\"post\" action=\"/cgi-bin/jPurchased.py\">{}<INPUT type=\"hidden\" name=\"line\" value=\"{}\">"
#              "<INPUT type=\"submit\" value=\"Mark as purchased\"></FORM>\n").format(m.group(1), i)


