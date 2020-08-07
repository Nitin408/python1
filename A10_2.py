name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
di=dict()
for line in handle:
    line=line.rstrip()
    if not line.startswith("From "): continue
    lines=line.split()
    word=lines[5]
    w=word[:2]
    di[w]=di.get(w,0)+1
    
    #print(di[w],w)
    
lst=list()
for key,val in di.items():
    newtup=(key,val)
    lst.append(newtup)
lst=sorted(lst) 

for  v,k in lst:
     print(v,k)
