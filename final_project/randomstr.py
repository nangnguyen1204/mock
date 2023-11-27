import random
import string

length = 2  # Độ dài của chuỗi
str1 = 'img28x28_6_'
str2 = '.jpg'
random_string = ''.join(random.sample(string.ascii_letters + string.digits, length))

img_name = str1 + random_string + str2

print(img_name)