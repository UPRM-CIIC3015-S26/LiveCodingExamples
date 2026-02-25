

# Write a function that receives a valid password and allows
# a user to enter it at most n times.  The function returns
# true if the user enter the valid password and false otherwise.
def get_password(valid_password, attempts):
    cnt = 0
    user_password = ''
    while user_password != valid_password and cnt < attempts:
        cnt += 1
        user_password = input(f"Please enter your password (attempt {cnt}): ")
    if user_password == valid_password:
        return True
    else:
        return False

result = get_password('foobar', 7)
print(result)



