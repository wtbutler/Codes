import codeKeys
ek = codeKeys.ek
dk = codeKeys.dk
x='n'
while x!='y':
	if len(ek)==len(dk):
		q=""
		o=""
		while ((q!='e' and q!='E') and (q!='d' and q!='D')):
			q=input('Encode or Decode [e/d]: ')
			if q=='e' or q=='E':
				s=input('Encode: ')
				s=list(s)
				offset=2
				for i in range(0,len(s)):
					s[i]=ek[s[i]]
					offset=(1+offset+s[i])%len(ek)
					s[i]=dk[offset]
					o=o+s[i]
				print(o)
			if q=='d' or q=='D':
					s=input('Decode: ')
					s=list(s)
					offset=3
					for i in range(0,len(s)):
						s[i]=ek[s[i]]
						o=o+dk[s[i]-offset]
						offset=(s[i]+1)%len(ek)
					print(o)
	else:
		print("We are currently experiencing difficulties. Plese try again after maintenence")
	x=input("type y to exit: ")
