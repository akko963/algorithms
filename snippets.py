
#Each tiblets should be documented

import itertools
import random
import math
from collections import OrderedDict
from random import randint
def isqrt (n):
    res = 0
    bit = 1<<256
    while (bit > n):
        bit = bit >> 2
    while (bit != 0):
        if (n>= (res + bit)):
            n= n- ( res+bit)
            res= bit *2 + res
        res = res >>1
        bit = bit>> 2
    return res

# print("sqrt : ",isqrt(10**76))
# bit = 1<< 14;
# while (bit > 81):
#     bit = bit >> 2
# print('binary test',bin(128), bin(bit),(1<<4),bin(27-16),0b1001110001)
# test= 934032
#
# for i in range(math.ceil(str(test).__len__()/2)):
#     print(str(test)[i*2:i*2+2])
# i=2
# pre = int(str(test)[:i*2])
# post = int(str(test)[2:4])
# print("pre post", pre, post)
#
# a = 13 % 5
# print(a)

def divide(n, div: int, inc =0):
    start = div
    print(n," to divide ", div)
    i=0
    while ((i+1)* (div+i+1)  <= n ):
        print("divisible by ? ", i* div+i)
        i += 1
    print(n," divide ", div+i, "times ", i)
    return (i, n% (div+i) )


# this is a bad approach ; there is also an obvious bug in there. Not a good start for code exercise.
# binary algorithm is probably better
def sq(n):
    if str(n)[:3]!="100":
        pre = int(str(n)[:2])
        post = str(n)[2:]
    else:
        pre = 100
        post = str(n)[3:]
    div = 3
    while  div*div  <= pre :
        div+=1
    div-=1
    total_div = div
    div = div*div
    remainder = pre % div
    print("pre post rem", pre, post, remainder)
    while(len(post)>0):
        pre = int(post[:2])
        div,remainder = divide(remainder*100 +pre,total_div * 20)
        print('rem :',remainder)
        total_div = total_div * 10 + div
        post = str(post)[2:]
    print("square root of ","{0:,}".format(n), " is ","{0:,}".format(total_div))

# print(math.sqrt(3*10**5))
# a = [randint(0, 100) for _ in range(0, 21)]
#
# #x = list(map(sum, zip(a[::2], a[1::2])))
# b = list(map(sum, zip(a[::2], a[1::2])))
# x= [all(sum(i) ==90 for i in  zip(a[::2], a[1::2]) )]
# print(x)
# print(a)
# print(b)
# print(len(list(map(sum, zip(a[::2], a[1::2])))),len(a))
# print(next ((i for i in [1,6,3,9,4] if i == 0),-1))
# print('list gen test')
# print(len(a))
# for x in range (1,len(a)):
#     print('creating',x)
#     print([a[i::1+x] for i in range(x+1)])
#
# for i in range(9):
#     print(randint(0,1))
#
#
# print("test",-1*3)
# print(type({}))
#
# swapper = lambda x,y : (y,x)
# print(type(swapper))
# (a,b)=swapper(3,9)
# print(swapper(3,9))
# print('swap test', a,b)
#
# a=b= 0
# b = 3

# print(a,b)
# print('floor',3.2//1)
# print(1%1)
# print('ceil',-(-1.2//1))

def fn(arg):
    print(arg)
    arg[:] = [1,3]


ls = [1,2,3,4]
#print(ls[0:2],ls[2:4])

# test: result: map obj is an interable
fn = lambda x: x*3.2
#print([i for i in map(fn, [3,4,5])])
test = ['a']
#print(id(test))
test2= test.copy()
#print(id(test),id(test2))
x=4
y=z=0
n = 4
def towerHanoi ( x, y, z, n):
    if n>1:
        x,y,z= towerHanoi(x,y,z, n-1)
    #z.append(x[-1])
    print('n value',n)
    x-=1
    z+=1
    #x[:] = x[0:-1]
    if n> 1:
        x,y,z=towerHanoi(y,x,z,n-1)
    print('x,y,z',x,y,z)
    print('cur solution:',x,y,z)
    return x,y,z
towerHanoi(x,y,z,4)
print('end solution:', x, y, z)


def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks:
        hanoi(ndisks - 1, startPeg, 6 - startPeg - endPeg)
        print(
        "Move disk %d from peg %d to peg %d" % (ndisks, startPeg, endPeg))
        hanoi(ndisks - 1, 6 - startPeg - endPeg, endPeg)


hanoi(ndisks=4)

# checking passing by reference  if [] is used in assignment, it will be overwritten
def mv(y,x):
    if len(x)> 0 and x[-1] < y[-1]:
        print('error.')
        return y,x
    x.append(y[-1])
    y[:] = y[0:-1]
    return y,x


def hanoi2(start,end,temp,n):
    print('n is',n)
    if (n>0):
        hanoi2(start,temp,end,n-1)
        hanoi2(temp,end,start,n-1)
        start,end= mv(start,end)
        print(start,end,temp)
        # break
        # start,temp,end = hanoi2(start,temp,end)
        # temp,start,end = hanoi2(temp,start,end)
        return start,end,temp,n
    else:
        return
# hanoi2([4,3,2,1],[],[],4)



# char '0' is not False Nor would it evaluate to false
print('0'==False)

# element from for _ in list: can be checked right in the list comprehension
test= [(i,0) for i,x in enumerate([0,3,2,0,3,0,13,3]) if x==0]
print(test)


test0=[]
test=True if test0 else False
# empty list is neither true nor False in direct value checking
# but when evaluated, it is False (ABOVE)
print([]==False,[]==True,test)


print(set(['',1,5,3,1]))
#print(ord('X'),ord('O'))
#print(ord('a'))

# list.discard(element) can throw away unwanted element. It doesn't complaint. .remove() will throw error
a= set([3,5])
if a.discard(5) or 3 in a:
    print (a)

# empty space : '' and None are not the same
print (''==None)  # returns false

# choice will return one value from a list
print(random.choice([1,3]))

# chained assignment. A SINGLE 'SAME' value/object is assigned to BOTH
tmp = tmp2 = [5]
tmp2.append(3)   # expect 3 to be removed from BOTH tmp and tmp2
print(tmp)  # print 5    . In tmp, 3 is also gone

# chained assignment doesn't seem to work on variables
a=b=3
print(a,b)
b=1
print(a,b)  # each has its own value


##################################################
def fn_list_assignment_plain(test):
    test = [6,7]
def fn_list_assignment_with_index(test):
    test[0] = 'overwritten in function'

test = [1,3]
#if there are no assignments using
fn_list_assignment_plain(test)
print (test)  # preserve the test's original values before passing

fn_list_assignment_with_index(test)
print (test)  # function overwrote the original list because it used []
##################################################

# booleans can be used with sum . It means summing statements  value == 99 can be evaluated and added
print('Summing booleans: ',sum([random.choice([True,False]) for _ in range(3)]))

# when using 'in' on a dictionary, the value you are finding actually uses dictionary's key. Not its value.
dtest =  {0:10, -1:20}
if -1 in dtest:
    print('yes -1 is seen with "in"')
if 10 in dtest:
    print('yes 10 is seen with "in"')

# adding element to a dictionary using list's addressing. and appending to a dictionary key's array/list
dtest[5] = []
dtest[5].append(50)
print("yes, a new keypair can be added using int as index.",dtest[5])
print("yes you can add an array and append to a key's array",dtest)

# appending a list to another list and altering it. List are appended in reference.
test = [-1,-3]
test_list = [5,6,1]
test_list.append(test)
test.append(-5)
print(test_list)  #expect the test_list to contain 5,6,0,[-1,-3] but altering the element altered the appeneded list

# numbers don't join() into str
# print(list(''.join(x) for x in [1,2,3]))

#combinations, permutation, product
product = list(''.join(x) for x in itertools.product('ABCD', repeat=2))	 # AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
permute = list(''.join(x)for x in itertools.permutations('ABCD', 2))	 	 # AB AC AD BA BC BD CA CB CD DA DB DC
combine = list(''.join(x)for x in itertools.combinations('ABCD', 2))	 	 # AB AC AD BC BD CD
combine_replace = list(''.join(x) for x in itertools.combinations_with_replacement('ABCD', 2))
print(product,'\n',permute,'\n',combine,'\n',combine_replace)

permute4 = list(''.join(x)for x in itertools.permutations('ABCD', 4))
print(permute4,'\nlength:',len(permute4),'\n4!=4*3*2*1 :',math.factorial(4))

print(math.factorial(8))

#shuffle is in-place ; return none
l3= random.shuffle([2,5,7])
print(l3)
l3 = list('123456789')
random.shuffle(l3)
print(l3)

# chaining list comprehension;
# nested for loops for nested lists; hypothetical
# should be nested 4 times. as [[ [[],[],[]],  [[],[],[]], [[],[],[]] ],    []  ]
animals = []
output = [ humans for animalList in animals for mammals in animalList for primates in mammals for humans in primates]



def permutate(board =['2','1','3','5','4']):
    head = []
    print(board,len(board))
    random.shuffle(board)
    print(board,len(board))
    for i in range(1,len(board)+1,1):
        print(i)
        head.append(list(''.join(x) for x in itertools.permutations(board, i)))
    for i in head:
        print(i)
    for i in head:
        print(len(i))
    return head
# notice the last 2 are repeated . this is the nature of permutations
permutate()

def genGame(board =['2','1','3','5','4']):
    random.shuffle(board)
    compiledList =[]
    print('cpl',compiledList)

    for i in range(1,len(board)+1,1):
        print(i)
        compiledList+= list(''.join(x) for x in itertools.permutations(board, i))

    print('cpl',len(compiledList))
    print(compiledList)
genGame()
#genGame()


# list -1 test
ls = [3,4,5]
# list except last element
print(ls[:-1])
# list's last element
print(ls[-1])

print(ls[:2])

# empty list for in loop
for i in []:
    print('empty list print test',i)

# convert str to chr list by list('abcd')
ls = '456'
print('you can convert a str into a list of characters',list(ls))
print('adding a str to a list',ls+'str' )

# some set properties:  subtraction and union
print(len(set()))
st =  set(list('214856'))
st2 = st- set(list('156'))
print('union sets', st2, type(st2))  # also set resulted from sets' subtraction. need to typecast it

ls= list('456')
ls2 = list('34567')
# ls3 = ls2 - ls
print('ls3: subtracting lists wont work')

if set(list('3345')) < set(list('23456')):
    print('list to set operations. what it does to duplicates')
elif set(list('345')) < set(list('23456')):
    print('list to set operations. works with dupes')

test = list('345')
test2 = str(test2)
print('from char list to a str', test,str(test2))
# correction
print('from char list to a str', test,''.join(x for x in test))

# set removal from using another set
s1 = {1,2,3,4,5,6}
s2 = {2,4,6}
s3 = s1-s2
print('discard a set from another',s3)

# install a package from within python console
import pip
args = ['param1', 'param2']
version = 0.1
package = ['some_package=={}'.format(version)]
#pip.main(['install'] + args + package)

ls = [1,2,3,4,5,6,7,8,9]
#print ( 'list custom',ls [8,4,2])
print(len([x for x in itertools.permutations([1,2,3,4],3)]))

s = '''\
import random
st1 = set(random.sample(range(10000),1000))
st2 = set(random.sample(range(100000),10000))
st2-st1
'''
s2 = '''\
import random
st1 = list(random.sample(range(10000),1000))
st2 = set(random.sample(range(100000),10000))
st3 = [x for x in st1 if x in st2]
'''

import timeit
print(timeit.timeit(stmt=s,number=10))
print(timeit.timeit(stmt=s2,number=10))

print([''.join(triplet) for triplet in itertools.permutations(list('123'),3)] )
ls = [x for x in '456']
print(ls)

win_triplets = ['123', '456', '789', '147', '258', '369', '159', '357']
print([''.join(x) for win in win_triplets for x in itertools.combinations(win,2)])

def checkImminentWin(game):
    if len(game) <1 or len(game) > 9:
        raise ValueError("Invalid game. Extra moves.")
    anchor = game[-1]
    if len(game) <3:
        return 0
    hops = game[::-2][1:]
    print(anchor,hops)
checkImminentWin(list('159763'))
print('set for a str. str works both set and list ()', set('159763') )
print('true false check-in- for str','5'in '159763')
print(sum(1 for x in range(0,15,2)))

print('overshot',sum(1 for x in range(4,2,1)))
