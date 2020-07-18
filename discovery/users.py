import os


def save_users_file():
    with open('./users.txt', 'w') as f:
        names = os.listdir('/home')
        f.write('\n'.join([n for n in names if os.path.isdir(f'/home/{n}')]))
        f.close()


if __name__ == '__main__':
    save_users_file()
