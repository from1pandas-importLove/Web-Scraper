import string

# put your code here
name = input()
my_template = string.Template('Dear $username! It was really nice to meet you. Hopefully, you have a nice day! See you soon, $username!')
my_str = my_template.substitute(username=name)
print(my_str)