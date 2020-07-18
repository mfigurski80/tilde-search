import os

file = open('./users.txt')

def discover_sites_for(user):
    user_dir = f'/home/{user}/public_html/'
    found_files = []
    found_paths = ['']
    cur_path = None

    while len(found_paths) > 0:
        cur_path = found_paths.pop()
        names = os.listdir(user_dir + cur_path)

        for n in names:
            if os.path.isdir(user_dir + cur_path + n):
                found_paths.append(cur_path + n + '/')
            else:
                found_files.append(cur_path + n)
    return found_files

if __name__ == '__main__':
    print(discover_sites_for('mikofigs'))
