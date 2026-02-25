

password = ''
while password != 'helloworld':
    password = input('Password?')
    if password == 'helloworld':
      print('Access granted!')
    else:
      print('Wrong password.')