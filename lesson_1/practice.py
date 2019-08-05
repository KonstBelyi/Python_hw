print("Hello World!")
print('Hello \'World!\'')
print("Hello \"World!\"")
print('Hello \n"World\b"!')

'''
\a  - alert
\n  - new line
\b  - backspace
\'  
\"  
\\  
\t  - horizontal tab

'''

print("===================")
print(45)
print(34 + 5)
print("===================")
a = 12
b = 23
i = a + b
# print("Result of sum " + str(a) + " and " + str(b) + ":", i)
# print(i)
print("Result of sum {A} and {B}: {I}".format(B=b, I=i, A=a))
print("Result of sum {0} and {1}: {2}".format(a, b, i))
print("Result of sum {} and {}: {}".format(a, b, i))
