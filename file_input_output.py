#1st example
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "r+")

for i in my_list:
    my_file.write("%d%s" % (i, "\n"))

my_file.close()
print(my_file)

#2nd example
read_file = open("text.txt", "r")


write_file = open("text.txt", "w")

write_file.write("Not closing files is VERY BAD.")

write_file.close()


print (read_file.read())
read_file.close()

#3rd example
with open("text.txt", "w") as my_file:
    my_file.write("It's wonderful!")