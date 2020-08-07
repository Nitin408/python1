# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
add=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
        
    aposs=line.find(':')
    host=line[aposs+1:]
    h=float(host)
    add+=h
    count=count+1
        
print("Average spam confidence:",add/count)
