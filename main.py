test_file = open('test.txt', 'w')

test_file.write("First string\n")
test_file.write("Second string\n")
test_file.close()

test_file = open('test.txt', 'r')
print(test_file.read())
