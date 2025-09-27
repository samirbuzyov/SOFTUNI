from calendar import different_locale

length = int(input())
width = int(input())


total_pieces = length * width
pieces_taken = 0
command = input()

while command != 'STOP':
    piece_per_guest = int(command)
    pieces_taken += piece_per_guest

    if pieces_taken > total_pieces:
        break

    command = input()

diff = total_pieces - pieces_taken

if command == 'STOP':
    print(f"{abs(diff)} pieces are left.")
else:
    print(f"No more cake left! You need {abs(diff)} pieces more.")
