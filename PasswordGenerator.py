import random
import string
import os
import json
import time

def info():
    print ('Your new default password will include:')
    print ('1. Your minimum length is 8')
    print ('2. Your maximum length is 11')
    print ('3. Must contain at least 1 lower case letter')
    print ('4. Must contain at least 1 upper case letter')
    print ('5. Must contain at least 1 digit')
    print ('6. Must contain at least 1 special character')

def edit_option():
    print ('Do you want to customize your choices ? (y/n): ',end='')
    optimize = input()
    if optimize == 'y':
        print('You want to change some option ?')
        print('1. Edit options')
        print('2. Delete options')
        print('3. Nothing')
    else:
        pass
    return optimize

class Password:
    def __init__(self,term=[''],min_length=8,max_length=11,delete_rule=['']):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digit = string.digits
        self.punctuation = string.punctuation
        self.delete_rule = delete_rule
        self.website = ''
        self.time = ''
        if (min_length >=8):
            self.min_length = min_length
            self.max_length = max_length
            self.term = term
            self.password = ''
            self.list_option = ['lowercase', 'uppercase', 'digit', 'punctuation']
        else:
            print ('Minimum is 8 characters')


    def check_option(self,option):
        if option == 'lowercase':
            return self.lowercase
        elif option == 'uppercase':
            return self.uppercase
        elif option == 'digit':
            return self.digit
        elif option == 'punctuation':
            return self.punctuation
        else:
            return option

    def change_term(self,term):
        self.term = term

    def shuffle(self,password):
        passwordList = list(self.password)
        random.SystemRandom().shuffle(passwordList)
        self.password = ''.join(passwordList)

    def fill_the_rest(self,temp_choices,min_length,max_length):
        for i in range(random.randint(min_length-len(self.password),max_length-len(self.password))):
            self.password+=random.choice(temp_choices)

    def create_important_part(self,option):
        temp_choices= ''
        for i in option:
            choice = self.check_option(i)
            temp_choices+=choice
            self.password += random.choice(choice)
        return temp_choices

    def default_rule(self):
        temp_choices=self.create_important_part(self.list_option)
        self.fill_the_rest(temp_choices,self.min_length,self.max_length)
        self.shuffle(self.password)
        self.time = time.ctime()

    def rules_delete(self,list_delete):
        temp = ['lowercase', 'uppercase', 'digit', 'punctuation']
        for i in list_delete:
            self.list_option.remove(temp[i-1])
        if len(self.list_option) ==0:
            self.list_option=['lowercase']

    def customize_rule_remove(self,list_delete):
        self.rules_delete(list_delete)
        self.default_rule()

    def customize_rule_edit(self,list_edit):
        pass

    def print(self):
        print ('Your password: ',self.password)

    def write_file(self):
        file_name= ('/'.join(str(os.getcwd()).split('\\')) + '/Password.json')
        if not os.path.isfile(file_name):
            data = {self.website: [[self.password,self.time]]}
            with open(file_name, 'w') as fp:
                json.dump(data, fp)
        else:
            with open(file_name,'r') as feedsjson:
                feeds = json.load(feedsjson)
            if self.website in feeds:
                feeds[self.website].append([self.password,self.time])
            else:
                feeds[self.website] = [self.password,self.time]
            with open(file_name, 'w') as fp:
                json.dump(feeds, fp)

def main():
    info()
    optimize = edit_option()
    if optimize == 'y':
        print ('Your option: ',end='')
        option = input()

        print('Length of inputs:', end='')
        numb = int(input())

        if option == '1':
            print('Edit options: ', end='')
            list_edit = [input() for i in range(numb)]
        elif option == '2':
            print('Delete options: ', end='')
            list_delete = [input() for i in range(numb)]
    print ('Number of passwords: ',end='')
    numb_choice = int(input())
    while numb_choice > 0:
        # Default option
        password = Password()
        if optimize=='y':
            choice = (input())
            if (choice == '1'):
                password.customize_rule_edit(list_edit)
            elif (choice == '2'):
                password.customize_rule_remove(list_delete)
            else:
                pass
        else:
            password.default_rule()
        password.print()
        password.write_file()
        numb_choice -=1

if __name__=='__main__':
    main()

