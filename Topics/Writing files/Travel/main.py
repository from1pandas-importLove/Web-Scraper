# add Turkey to countries.txt
list_of_countries = ['Turkey\n']
file = open('countries.txt', 'a', encoding='utf-8')
file.writelines(list_of_countries)
file.close()