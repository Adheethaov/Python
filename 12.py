"""
write a program that pull down a web page, look for all the links in that web page and pull down all those web pages
"""

import urllib.request, urllib.parse, urllib.error
import re
links=list()
fhand = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")


def fweb(fhand):
    count=0
    for line in fhand:
        line=line.decode().strip()
        print(line)
        hlink=re.findall('^<a.*',line)
        if len(hlink)<1:
            continue
        #print(hlink)
        links.append(hlink[count])
        count = count +1

#print("fhand is ", fhand)
fweb(fhand)
#print("link list  is ",links)
for i in range(0,len(links)):
    y=links[i]
    s=y.split('"')
    print("\n")
    fhand =urllib.request.urlopen(s[1])
    fweb(fhand)
