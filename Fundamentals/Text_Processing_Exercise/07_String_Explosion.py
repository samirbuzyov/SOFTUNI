# text = input()
# explosion = 0
# final_string = ''
# start_idx_explosion = 0
#
# index = 0
# previous_explosion = 0
#
# while index < len(text):
#     if text[index] == '>':
#         final_string += '>'
#         start_idx_explosion = index + 1
#         explosion = int(text[index + 1]) + previous_explosion
#         stop_idx_explosion = start_idx_explosion + explosion
#
#         for i in range(start_idx_explosion, stop_idx_explosion):
#             if text[i] != '>':
#                 index = i
#                 continue
#             else:
#                 previous_explosion = stop_idx_explosion - i
#                 break
#
#
#
#
#     else:
#         final_string += text[index]
#
#     index += 1
#
#
# print(final_string)
text = input()
explosion_strength = 0
final_string = ''

for index in range(len(text)):
    if text[index] == '>':
        final_string += '>'
        explosion_strength += int(text[index + 1])
    elif explosion_strength > 0:
        explosion_strength -= 1
    else:
        final_string += text[index]



print(final_string)
