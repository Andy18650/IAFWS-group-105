print('importee\'s __name__ is:',__name__)

if __name__ == '__main__':
    print('I, the importee, is actually running as a standalone program!')
elif __name__ == 'importee':
    print('I am being imported!')
else:
    print('I don\'t know what is going on here...')


def someFunction():
    print('This is a function of the importee!')
