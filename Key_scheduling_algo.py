ki = [[0x0, 0x0], [0x0, 0x0]]

sub_nib_list = [0xe, 0x4, 0xd, 0x1, 0x2, 0xf, 0xb, 0x8, 0x3, 0xa, 0x6, 0xc, 0x5, 0x9, 0x0, 0x7]

l=int(len(ki))-1

#print(ar)
'''k1=ar^ki[0][0]
print(k)'''
#k= [[0 for _ in range(len(ki))] for _ in range(len(ki))]
r_cons=0x1
n=int(input("How many subkey required:\n"))
for i in range (n):
	a=sub_nib_list[ki[l][l]]
	if(r_cons>15):
		r_cons^=0x13
	ar=(a^r_cons)
	for j in range (len(ki)):
		for m in range (len(ki)):
			r=(ki[m][j]^ar)
			if(r<=0xf):
				ki[m][j]=r
			else:
				ki[m][j]=r^0x13	
			ar=ki[m][j]
	r_cons<<=1
	print("Subkey Matrix:")
	for row in ki:
		#print(''.join(hex(element) for element in row))
		print(*row)				

	
