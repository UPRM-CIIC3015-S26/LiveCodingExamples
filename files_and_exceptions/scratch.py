def file_open_exception_example():
    file_found = False
    while not file_found:
        filename = input('Enter filename: ')
        try:
            file = open(filename, 'r')
            file_found = True
            print(f"Successfully opened file {filename}")
        except FileNotFoundError as e:
            print('File not found, try again')

file_open_exception_example()