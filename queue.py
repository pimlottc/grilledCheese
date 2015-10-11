#!/Python27/python
import cgi
import cgitb
import re

cgitb.enable()

nameCounts = {}

def makeTableLines(dataList):
    output = ''
    for line in dataList:
        output += "<tr>\n <td>{}</td>\n <td>{}</td>\n <td>{}</td>\n <td>{}</td>\n</tr>\n".format(line[0], line[1], line[2], line[3])
        lName = line[0].lower()
        nameCount = 1
        if (lName in nameCounts):
            nameCount = nameCounts[lName] + 1
        nameCounts[lName] = nameCount
        line.append(nameCount)
    return output

def queueSort(one, two):
    #the number for the person is stored on the 5th item, order time on the 4th
    retVal = one[5] - two[5]
    if retVal == 0:
        retVal = int(one[4]) - int(two[4])
    return retVal

print "Content-Type: text/html"
print "Cache-control: no-cache"
print

print '<HTML><head><title>Sandwich Queue!</title><!--meta http-equiv="refresh" content="5" --></head>\n<body>\n<H3>Sandwich Queue!</H3>\n'

#layout of queue "database" <name> | <bread> | <cheese, comma sep> | <toppings, comma sep> | unixTime of order\n
#There will be 3 queue "database" files, completed, in progress, and queue
#.lock files will exist for each "database" file

sanatizer = re.compile('[^a-zA-Z0-9_ ,\\|]')

queue = [sanatizer.sub('', line.strip()).split('|') for line in open('E:\\WebData\\queue.txt', "r")]
completed = [sanatizer.sub('', line.strip()).split('|') for line in open('E:\\WebData\\completed.txt', "r")]
inprogress = [sanatizer.sub('', line.strip()).split('|') for line in open('E:\\WebData\\inprogress.txt', "r")]

queue = [x for x in queue if len(x) == 5]
completed = [x for x in completed if len(x) == 5]
inprogress = [x for x in inprogress if len(x) == 5]



completedTable = makeTableLines(completed)
inprogressTable = makeTableLines(inprogress)
makeTableLines(queue)

queue.sort(queueSort)



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
print '<p>'

cheeses = ["cheddar", "white cheddar", "pepper jack", "candy"]
print '<h3>Request a sandwich!</h3>'
print '<FORM method="post" action="/cgi-bin/grilledCheese/order.py">'
print '<table>\n <tr>\n  <th>Name</th>\n  <th>Cheese (up to 2)</th>\n  <th>Toppings</th>\n </tr>'
print ' <tr>\n  <td>\n   <input type="text" name="name">\n  </td>'
print '  <td>'
i = 0
print '   <table>\n    <tr><td>'
for cheese in cheeses:
    print '   <INPUT type="checkbox" name="cheese[]" value="{}"> {} '.format(cheese, cheese)
    i += 1
    if i == len(cheeses):
        print ''
    elif i == len(cheeses)/2:
        print '     </td><td>'
    else:
        print '     <br>'

print '</p>'
print '</body>'


# cpy-paste form example
#        print ("<FORM method=\"post\" action=\"/cgi-bin/jPurchased.py\">{}<INPUT type=\"hidden\" name=\"line\" value=\"{}\">"
#              "<INPUT type=\"submit\" value=\"Mark as purchased\"></FORM>\n").format(m.group(1), i)


