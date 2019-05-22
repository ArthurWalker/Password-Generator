def info():
    print ('Your new default password will include:')
    print ('1. Your minimum length is 8')
    print ('2. Your maximum length is 11')
    print ('2. Must contain at least 1 lower case letter')
    print ('3. Must contain at least 1 upper case letter')
    print ('4. Must contain at least 1 digit')
    print ('5. Must contain at least 1 special character')

def edit_option():
    print ('Do you want to customize your choices ? Y/N')
    optimize = input()
    if optimize == 'Y':
        print ('Add a condition or change some condition ? add/change')
        condition = input()
        if condition == 'add':
            print ('Do you want password to contain some term ?')
            print ('1. All terms')
            print ('2. Terms are splited or some will not be used')
        else:
            print ('You want to change some option ?')
            print ('1. Delete options')
            print ('2. Edit options')
            print ('3. Nothing')

def main():
    info()
    edit_option()


if __name__=='__main__':
    main()