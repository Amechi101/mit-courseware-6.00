'''import urllib.request

requestInfo = urllib.request.urlopen("http://www.garmentory.com/designers").read()

print(requestInfo)
'''
print("Hello World")

import urllib2
from lxml import html
import codecs


requestInfo = urllib2.urlopen("http://www.garmentory.com/designers").read()
requestInfo2 = urllib2.urlopen("http://swords-smith.com/pages/designers").read()

tree = html.fromstring(requestInfo)
tree2 = html.fromstring(requestInfo2)

designers = tree.xpath('//div[@class="brand"]/a/text()')
designers2 = tree2.xpath('//*[@id="column1"]/li/a/text()') + tree2.xpath('//*[@id="column2"]/li/a/text()') + tree2.xpath('//*[@id="column3"]/li/a/text()') + tree2.xpath('//*[@id="column4"]/li/a/text()') 
print(len(designers))
print(len(designers2))

allDesigners = designers + designers2 # + any extra designer resources added
allDesigners.sort()
print(len(allDesigners))

saveDesignerFile = codecs.open('designerList.txt', 'w', 'utf-8')
for designerName in allDesigners:
	print designerName
	saveDesignerFile.write(designerName+"\n")
	 
saveDesignerFile.close()
	


