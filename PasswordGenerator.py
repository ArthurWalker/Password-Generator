import random
import string

def info():
    print ('Your new default password will include:')
    print ('1. Your minimum length is 8')
    print ('2. Your maximum length is 11')
    print ('2. Must contain at least 1 lower case letter')
    print ('3. Must contain at least 1 upper case letter')
    print ('4. Must contain at least 1 digit')
    print ('5. Must contain at least 1 special character')

def edit_option():
    print ('Do you want to customize your choices ? (y/n): ',end='')
    optimize = input()
    if optimize == 'y':
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
    else:
        pass

def generate_default_password():
    randomSource = string.ascii_letters+string.digits+string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    for i in range(random.randint(8,11)):
        password += random.choice(randomSource)
    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password

def main():
    info()
    edit_option()

    print ('Number of passwords: ',end='')
    numb_choice = int(input())
    while numb_choice > 0:
        # Default option
        password = generate_default_password()
        print('Your password:', password)
        numb_choice -=1


if __name__=='__main__':
    main()