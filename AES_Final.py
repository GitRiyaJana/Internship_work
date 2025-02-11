import numpy as np

def shift_rows(sub_mat):
	shifted_matrix = []
	num_cols = len(sub_mat[0])  
	for i, row in enumerate(sub_mat):
		shift_amount = i  # Shift amount is equal to the row index
		shifted_row = row[shift_amount:] + row[:shift_amount]  # Perform the shift
		shifted_matrix.append(shifted_row)  # Add the shifted row to the shifted matrix
	print("\nAfter performing Shift row:")
	for row in shifted_matrix:  # Print the shifted matrix
		print(*row)
	return shifted_matrix

def sub_nib(matrix1):
	s = []
	for row in matrix1:
		row_s = []  # Initialize a row for the s matrix
		for elem in row:
			row_s.append(sub_nib_list[elem])  # Access sub_nib_list using the value in elem
		s.append(row_s)  # Append the row to the s matrix
	print("\nAfter Performing sub_nib:")
	for row in s:  # Print the result after performing sub_nib
		print(*row)
	return s

matrix = [[0x0, 0x0], [0x0, 0x0]]
ki = [[0x0, 0x0], [0x0, 0x0]]
o = np.bitwise_xor(matrix,ki)
matrix1=o.tolist()
print("Initial state:",matrix1)

sub_nib_list = [0xe, 0x4, 0xd, 0x1, 0x2, 0xf, 0xb, 0x8, 0x3, 0xa, 0x6, 0xc, 0x5, 0x9, 0x0, 0x7]

'''print("\nInput Ciphertext:")
for row in matrix1:
	print(*row)'''



#mix_mat = [[0x0, 0x0], [0x0, 0x0]]

def gf_mult(a, b):
	p = 0
	for _ in range(4):  # Assuming 4-bit values
		if b & 1:
			p ^= a
		hi_bit_set = a & 0x8
		a <<= 1
		if hi_bit_set:
			a ^= 0x13  # Divisible by x^4 + x + 1
		b >>= 1
	return p

def mix_column(shift_mat):
	mix_matrix = [[3, 2], [2, 3]]
	result = [[0, 0], [0, 0]]  # Initialize the result matrix
	print("After performing mix column operation:")
	for i in range(2):
		for j in range(2):
			for k in range(2):
				# Accumulate the results in the result matrix
				result[i][j] ^= gf_mult(mix_matrix[i][k], shift_mat[k][j])
	print(result)
	return result

def generate_subkeys(ki, sub_nib_list):
	subkeys = [] # list to store subkeys
	l = int(len(ki)) - 1 #length of key matrix
	r_cons = 0x1 # initial round constant

	while r_cons <= 0x10:  # Continue until the round constant exceeds 0x10 (16)
		a = sub_nib_list[ki[l][l]]  # apply sub_nibble 
		ar = a ^ r_cons # xor with round cons 
		for j in range(len(ki)):
			for m in range(len(ki)):
				r = (ki[m][j] ^ ar) # xor each element 
				if r <= 0xf: # if r <16 then simply assign
					ki[m][j] = r
				else:  # else xor with primitive polynomial
					ki[m][j] = r ^ 0x13
				ar = ki[m][j]
		r_cons <<= 1 # increase round cons times 2
        
        # Make a deep copy of the current ki matrix to store it as a subkey
		subkey_copy = [row[:] for row in ki]
		subkeys.append(subkey_copy)
	#print("subkey is: ",subkeys)
	return subkeys
	

# Example usage


subkeys = generate_subkeys(ki, sub_nib_list)


# Example state
for i in range(5):
	sub_mat = sub_nib(matrix1)
	shift_mat = shift_rows(sub_mat)
	if(i<4):
		mixed=mix_column(shift_mat)
	else:
		mixed=shift_mat	
	subkey =subkeys[i]
	print("subkey:",subkey) 
	m=np.array(mixed)
	k=np.array(subkey)
	state=np.bitwise_xor(m,k)
	matrix1=state.tolist()
	if(i<4):
		print("\nround",i+2,"initial state:",matrix1)
print("output:",matrix1)	
	

