from itertools import product

commonSubs = {
	"a": ["@", "4"],
	"b": ["8"],
	"e": ["3"],
	"g": ["6", "9"],
	"i": ["1", "!"],
	"o": ["0"],
	"s": ["5", "$"],
	"t": ["7", "+"]
}

special = "!#$%&'()*+,-./:;<=>@?[\]^_`{|}~"

def genVariations(password):
	password = password.lower()
	varations = [""]
	for p in password:
		uppers = [v+p.upper() for v in varations]#P,A
		lowers = [v+p.lower() for v in varations]#p,a
		vs = uppers + lowers#P,A,p,a
		if p in commonSubs:
			for s in commonSubs[p]:
				x = [v+s for v in varations]#P,@,p,@,P,4,p,4
				vs += x #P,A,p,a,
		varations = vs#P,p
	return varations

def genSuffixes():
	specs = [x for x in special]
	nums = [str(n) for n in range(100)]
	combos = list(product(specs,nums))
	sn = [c[0]+c[1] for c in combos]
	ns = [c[1]+c[0] for c in combos]
	return sn+ns

def genPW(password):
	variations = genVariations(password)
	suffixes = genSuffixes()
	pw = variations + [[v+s for v in variations] for s in suffixes]
	return pw 




