name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
di=dict()
for line in handle:
    line=line.rstrip()
    if not line.startswith('From '):continue
    lines=line.split()
    x=lines[1]
    #print(x)
    di[x]=di.get(x,0)+1
    #print(di[x],x)
    
largest=-1
word=None
for k,v in di.items():
    #print(k,v)
    if v>largest:
        largest=v
        word=k
print(word,largest)    
