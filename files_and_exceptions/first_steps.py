

f = open("ciic_3015_first_file.txt", "w")

f.write("Hello World\n")
f.write("Goodbye World\n")

f.close()

f = open("ciic_3015_first_file.txt", "r")

data = f.read()

print(data)

f.close()
