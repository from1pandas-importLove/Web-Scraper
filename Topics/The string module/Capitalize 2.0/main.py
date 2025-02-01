import string

# put your code here
string1 = input()
string2 = input()

string1_splitted = string1.split()
first_word = string.capwords(string1_splitted[0])
result =  [first_word] + string1_splitted[1:]
string1_result = ' '.join(str(x) for x in result)
string2_cup = string.capwords(string2)

print(string1_result)
print(string2_cup)