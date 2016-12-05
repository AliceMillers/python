my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "r+")

for i in my_list:
    my_file.write("%d%s" % (i, "\n"))

my_file.close()
print(my_file)