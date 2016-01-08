import sys

def ReplaceUnderscoreWithSpace(kelime):
	sitr = list(kelime)
	newstr = ""
	for i in range(len(sitr)):
		if i == 0:
			newstr = sitr[i]
			continue
		elif i == (len(sitr)-1):
			newstr = newstr + sitr[i]
			continue
		elif sitr[i] == "_":
			newstr = newstr + " "
		else:
			newstr = newstr + sitr[i]
	return newstr

if __name__=='__main__':
	kelime = "_asiye_bilen_"
	print("yeni kelime = " + ReplaceUnderscoreWithSpace(kelime));
