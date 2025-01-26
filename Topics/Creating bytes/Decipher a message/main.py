encoded_meassage = input()
key = int(input())

two_bytes = key.to_bytes(2, 'little')
sum_bytes = two_bytes[0] + two_bytes[1]
# code_point = ord(encoded_meassage)

list_of_ord_characters = [(ord(elem) + sum_bytes).to_bytes(1, byteorder='little').decode() for elem in encoded_meassage]
print("".join(list_of_ord_characters))

