
def change_list(l, index, value):
    """ Modifies parameter to have given value at given index """
    l[index] = value

def main():
    arg_list = [1,2,3,4,5,6,7,8,9,10]
    change_list(arg_list, 4, -1)

main()

