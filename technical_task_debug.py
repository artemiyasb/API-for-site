def user_authorization():
    login = str(input('Enter your Login'))
    password = str(input('Enter your Password'))
    with open('a.txt', 'r') as f:
        text = f.read().split('\n')
        for line in text:
            line = line.split()
            if line[0] == login and line[1] == password:
                print('Found!')
                print('Authorization completed!')
            else:
                print('Login or password not found!')

def write_to_file(login, password):
    with open('a.txt', 'w') as f:
        f.write(f'{login}')
        f.write(" " f'{password}')

def user_registration():
    login = str(input('Enter your Login'))
    password = str(input('Enter your password'))
    if len(login) >= 3 and len(login) <= 20 and len(password) >= 4 and len(password) <= 32:
        write_to_file(login, password)
        print('Registration passed successful!')
    else:
        print('Registration error!')

def user_start():
    user_choose = int(input('Type 1 for registration or 2 for authorization: '))
    if user_choose == 1:
        print('Welcome to registration!')
        user_registration()
    elif user_choose == 2:
        print('Welcome to authorization!')
        user_authorization()
    else:
        print('The invalid meaning!')
user_start()
