def shift_rows(s):
    shifted_matrix = []
    num_cols = len(s[0])  # Get the number of columns in the matrix
    for i, row in enumerate(s):
        shift_amount = i  # Shift amount is equal to the row index
        shifted_row = row[shift_amount:] + row[:shift_amount]  # Perform the shift
        shifted_matrix.append(shifted_row)  # Add the shifted row to the shifted matrix
    print("\nAfter performing Shift row:")
    for row in shifted_matrix:  # Print the shifted matrix
        print(*row)
    return shifted_matrix

def sub_nib(matrix):
    s = []
    for row in matrix:
        row_s = []  # Initialize a row for the s matrix
        for elem in row:
            row_s.append(sub_nib_list[elem])  # Access sub_nib_list using the value in elem
        s.append(row_s)  # Append the row to the s matrix
    print("\nAfter Performing sub_nib:")
    for row in s:  # Print the result after performing sub_nib
        print(*row)
    return s

matrix1 = [[0x1, 0x3], [0x4, 0x7]]

sub_nib_list = [0xe, 0x4, 0xd, 0x1, 0x2, 0xf, 0xb, 0x8, 0x3, 0xa, 0x6, 0xc, 0x5, 0x9, 0x0, 0x7]

print("\nInput Ciphertext:")
for row in matrix1:
    print(*row)

sub_mat = sub_nib(matrix1)
shift_mat = shift_rows(sub_mat)

mix_mat = [[3, 2], [2, 3]]

def mixed_column(s_matrix, mix_mat):
    print("\nMixed Column matrix:")
    for row in mix_mat:
        print(*row)
    
    n = len(s_matrix)
    mixed = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mixed[i][j] ^= (mix_mat[i][k] & s_matrix[k][j]) % 0x13
    
    print("\nAfter performing Mixed Column operation:")
    for row in mixed:
        print(*row)

mixed_column(shift_mat, mix_mat)

