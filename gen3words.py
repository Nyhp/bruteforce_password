from itertools import product
from timeit import default_timer

def loadWord():
	with open("Oxford3000WordListNoSpaces.txt","r") as f:
		words = f.read().split("\n")
	return words

def genRandomWordPW(num):
	words = loadWord()
	pw = [""]
	for i in range(num):
		p = ["".join(p) for p in list(product(pw,words))]
		pw = p 
	return pw 

#start = default_timer()
#genRandomWordPW(2)
#stop = default_timer()
#print("runtime %s" % (stop-start))
print((genRandomWordPW(2)))