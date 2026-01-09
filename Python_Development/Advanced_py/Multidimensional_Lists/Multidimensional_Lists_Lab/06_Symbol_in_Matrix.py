n = int(input())

matrix = []
for _ in range(n):
    string = input()
    lst = [ord(char) for char in string]
    matrix.append(lst)

char = input()
is_found = False
for row_idx  in range(n):

    for col_idx in range(n):
        if matrix[row_idx][col_idx] == ord(char):
            coordinates = (row_idx, col_idx)
            is_found = True
            break
        if is_found:
            break
if is_found:
    print(coordinates)
else:
    print(f"{char} does not occur in the matrix")
