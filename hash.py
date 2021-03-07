import py_compile
import os

os.system('clear')
print('Your File :')
os.system('ls')

print('-'*100)

hash=input('Enter File name\n====>')

py_compile.compile(hash)


