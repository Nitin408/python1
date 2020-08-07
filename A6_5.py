text = "X-DSPAM-Confidence:    0.8475";
sppos=text.find(':')
num=text[sppos+1:]
n=float(num) 
print(n)
