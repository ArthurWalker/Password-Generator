import random
import string

"""Generate a random password """
randomSource = string.ascii_letters + string.digits + string.punctuation
password = ''
for i in range(8):
    password += random.choice(randomSource)

print (password)
