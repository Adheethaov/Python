"""9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."""


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts=dict()
gnumber=None
gsender=None


for line in handle:
    x=line.rstrip()
    if not x.startswith("From "):
        continue
    y=x.split()
    sender=y[1]
    if sender not in counts:
        counts[sender]=counts.get(sender,0)+1
    else:
        counts[sender]= counts[sender]+1

for i in counts:
    if gnumber is None or counts[i]>gnumber:
        gnumber=counts[i]
        gsender=i
print(gsender,gnumber)
