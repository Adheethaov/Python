"""Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
 You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d=dict()


for line in handle:
    x=line.rstrip()
    if not x.startswith('From '):
        continue
    y=x.split()
    #print(y)
    time=y[5]
    t=time.split(":")
    key=t[0]

    if key not in d:
        d[key]=d.get(key,0)+1
    else:
        d[key]=d[key]+1
#
print(d)

#sort by hour - key
tmp=sorted(d.items())
#print(tmp)
for k,v in tmp:
    print(k,v)
