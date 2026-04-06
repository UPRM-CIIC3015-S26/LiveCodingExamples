
# Writes sequen from 0 to n-1 to a file
def write_numbers(filename, n):
    archivo = open(filename,"w")
    for i in range(n):
        archivo.write(str(i)+"\n")
    archivo.close()

write_numbers("numbers_0_to_99.txt", 100)

