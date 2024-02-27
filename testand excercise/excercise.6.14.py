str = 'X-DSPAM-Confidence:0.8475'
index=str.find(":")
index=index+1
data=str[index:]
print(data)

data=float(data)
