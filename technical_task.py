def read_file():
    with open('a.txt', 'r') as f:
        words = []
        for line in f:
            for word in line.split():









def write_to_file(Login, Password):
    with open('a.txt', 'w') as f:
        f.write(f'{Login}')
        f.write('\n' f'{Password}')


def user_authorization():
    Login = str(input('Enter your Login'))
    Password = str(input('Enter your Password'))
    print(read_file())









def user_registration():
    Login = str(input('Enter your Login'))
    Password = str(input('Enter your password'))
    if len(Login) >= 3 and len(Login) <= 20 and len(Password) >= 4 and len(Password) <= 32:
        print(write_to_file(Login,Password))
        print('Registration passed successful!')

    else:
        print('Registration error!')
def user_start():
    user_choose = int(input('Type 1 for registration or 2 for authorization'))
    if user_choose == 1:
        print('Welcome to registration!')
        print(user_registration())
    elif user_choose == 2:
        print('Welcome to authorization!')
        print(user_authorization())
    else:
        print('The invalid meaning!')
print(user_start())







