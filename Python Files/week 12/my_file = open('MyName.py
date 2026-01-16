my_file = open('MyName.txt', 'w')
my_file.write('Seth')
my_file.close()


my_file = open('MyName.txt', 'r')
name = my_file.read()
print(name)
my_file.close()

my_file = open('MyName.txt', 'r')
name = my_file.read()
for i in range(len(name)):
    print(name[i])

my_file = open('myname.txt', 'w')
my_file.write('Seth')
my_file.close

my_file = open('Myname.txt' , 'r')
name = my_file.read()
print(name)
my_file.close