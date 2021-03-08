x = 3
print(id(x))   

y = x
print(id(y))



x += 6
print(id(x))

print(y)

print(id(y))

'''
runfile('C:/Users/h3cvdiuser/Desktop/untitled0.py', wdir='C:/Users/h3cvdiuser/Desktop')
8791514804032
8791514804032
8791514804224
3
8791514804032
'''
