import urllib.request, urllib.parse, urllib.error

fhand=urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
counts=dict()

for line in fhand:
    words=line.decode().split()
    #print(words)
    for word in words:
        if word not in counts:
            counts[word]=counts.get(word,0)+1
    print(line.decode().strip())

#print(counts)
