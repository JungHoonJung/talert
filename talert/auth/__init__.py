import os


def auth_user():
    '''user identifying.'''
    global users
    #refer  configure of home
    home = os.path.expanduser('~')
    if os.path.isfile(os.path.join(home, '.talert','config')):
        with open(os.path.join(home, '.talert','config')) as f:
            name = f.readline().rstrip()
    else:
        name = input("Please let me know your chat_id : ")
        os.makedirs(os.path.join(home, '.talert'), exist_ok = True)  # make configure folder
        with open(os.path.join(home, '.talert','config'),'w') as f:   # save user name
            f.write(name)



    return name, users[name]

def set_id(chat_id):
    name = input("Please let me know your chat_id : ")
    os.makedirs(os.path.join(home, '.talert'), exist_ok = True)  # make configure folder
    with open(os.path.join(home, '.talert','config'),'w') as f:   # save user name
        f.write(name)
