phonebook = {'matt':5073891348, 'ashley':12345}
print(phonebook)

# add to a dictionary, we use name_of_dict [ key ] = value

phonebook[' waters '] = 789
print(phonebook)

# to look up a value in a dictionary we use name_of_dict[ key ]
print( phonebook['matt'] )
#print(phonebook ['martensen'] ) doesnt exist

for person in phonebook:
    print(person, phonebook[person])


def string_to_dictionary(word):
    string_as_list = word.split()
    word_dictionary - {}
    for word in string_as_list:
        word_dictionary[word] = 'in word'