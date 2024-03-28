#Random Password Generator

import random
import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# print(random.choice("Hello"))
# val = random.choice(['a','b','c','d'])
# print(val)

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

# print(charValues)

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)
# print("your random password is :",password)    

#with use of list comptrehension [ function for i in range(n)]

possword = "".join([random.choice(charValues) for i in range(pass_len)])
print("Your random password is :",possword)