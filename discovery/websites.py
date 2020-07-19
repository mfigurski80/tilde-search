import os


def discover_sites_for(user):
    user_dir = f'/home/{user}/public_html/'
    found_files = []
    found_paths = ['']
    cur_path = None

    while len(found_paths) > 0:
        cur_path = found_paths.pop()
        names = os.listdir(user_dir + cur_path)

        for n in names:
            if os.path.isdir(user_dir + cur_path + n) and not n.startswith('.'):
                found_paths.append(cur_path + n + '/')
            elif n.endswith('.html'):
                found_files.append(cur_path + n)
    return found_files


def discover_sites():
    users = open('./users.txt').readlines()
    sites_file = open('./sites.txt', 'a+')
    for user in users:
        user = user.rstrip()
        print(f'Discovering: {user}')
        try:
            sites = discover_sites_for(user)
            sites = [f'http://tilde.club/~{user}/{site}' for site in sites]
            sites_file.write('\n'.join(sites))
            sites_file.write('\n')
        except OSError as e:
            print(f'Failed to discover: {e}')
    sites_file.close()


if __name__ == '__main__':
    discover_sites()
