#print('Hello Python')
'''
x = 0
if x < 0:
    x = 0
    print('change to Zero')
elif x == 0:
    print('Zero')
'''

'''
data = [1,2,3]
num = [d * 2 for d in data if d == 3]
print(num)
'''

'''
data = [1,2,3,4,5,6,7,8,9,10]
for d in range(1,10,2):
    print(d)
'''

'''
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
'''
'''
a = ['Mary', 'had', 'a', 'little', 'lamb']
for index,value in enumerate(a):
    print(index,value)
'''

'''
class MyFunction:
    pass
'''
'''
def initlog(args):
    print(args)
initlog(1)
'''

'''
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(10)
'''

'''
data = [1,3,5,7,9]
data2 = [2,4,6,8,10]
#data.append(data2)
#data.extend(data2)
data.pop()
print(data)
'''

#squares = list(map(lambda x: x+1, range(10)))
squares = [x+1 for x in range(10)]
print(squares)
