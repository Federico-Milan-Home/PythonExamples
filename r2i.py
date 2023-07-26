x = 'MMXX'#'MMDCLXXIV'
l = len(x)
i =0

R2I= {}
R2I['I'] = 1
R2I['V'] = 5
R2I['X'] = 10
R2I['L'] = 50
R2I['C'] = 100
R2I['D'] = 500
R2I['M'] = 1000

action = 1
Nold = 0
Nnew = 0
sum = 0


while i < l:
	Nnew = R2I[x[-1 - i]]
	if Nold > Nnew: 
		action = -1
	else:
		action = 1
	Nold = Nnew
	sum += Nnew*action
	#print(N)
	#print(sum)
	i = i + 1
print(x)
print(sum)