
import sys
import os
import time
import array

import pdb
import itertools


# Description: from a given string, find the first char that is not repeated 
def findFirstUniqChar0(st):
   for i in st:
      if st.count(i) == 1:
         print "found: '%s'" % i
         break
   else:
      print "not found"


# Description: from a given string, find the first char that is not repeated 
def findFirstUniqChar00(st):
   try:
      rty = (a for a in st if st.count(a) == 1).next()
      print "found: '%s'" % rty
   except StopIteration:
      rty = '' # null'
      print "not found"


# Description: from a given string, find the first char that is not repeated 
# Using Set
def findFirstUniqChar1(st):
   dbg = 0 #dbg = 1 
   cs1 = set()
   cs2 = set()
   for i in st:
      if i in cs1:
	 cs2.add(i) # occured more than once
      cs1.add(i)    # all case (occured once or more)
   cs3 = cs1 - cs2  # occured only once
   if dbg: print cs3
   for i in st:
      if i in cs3:
	 print "found '%s'" % i
	 break
   else:
      print "not found :-("


# Description: from a given string, find the first char that is not repeated 
# 
def findFirstUniqChar2(st):
   dbg = 0 #dbg = 1
   d = dict() # to store each char as key, occurence num as value
   for i in st:
      try:
         d[i] += 1 # increment value occurence (already key existing case)
      except KeyError:
         d[i] = 1  # first time the key (char) is created
   if dbg: print d

   for i in st: # in the given order of string
      if d[i] == 1:
         print "found: '%s'" % i
	 return i # the char
         #break
   else:
      print "not found :-("
      return '' # null 



def EO1(ar):
   print ar

   # forward and backward index into the array
   fi = 0
   bi = len(ar) - 1

   while ( fi < bi ):
	   while ( fi < bi ):
	      print 'ar[', fi, ']', ar[fi],
	      if ar[fi] & 0x0001:
		 print 'odd fi=',fi # found need to exchange fi index
                 break
	      else:
		 print 'even ok',
		 fi = fi + 1
		 
	   while ( fi < bi ):
	      print 'ar[',bi,']', ar[bi],
	      if ar[bi] & 0x0001:
		 print 'odd ok',
		 bi = bi - 1
	      else: # 
		 print 'even bi=',bi # found need to exchange bi index
                 break

	   if ( fi < bi ):
              print 'exchange', 
	      t = ar[fi]
	      ar[fi] = ar[bi]
	      ar[bi] = t
	   else:
	      print 'done'
   print ar


'''
   EO() another implementation
   [Even | | | | |... | | | | |  Odd]
'''
def EO(ar):
   print 'EO begin', ar
   fi = 0; bi = len(ar)-1 # forward index, backward index into array
   while ( fi < bi ):
	   while ( fi < bi and (ar[fi] & 0x0001 == 0)): # even
              fi = fi + 1
	   while ( fi < bi and ar[bi] & 0x0001 ): # odd
	      bi = bi - 1
	   ar[fi], ar[bi] = ar[bi], ar[fi] # exchange them
   print 'EO end  ', ar


'''
   OE() 
   [Odd | | | | |... | | | | | Even]
'''
def OE(ar):
   print 'OE begin', ar
   # forward index and backward index into the array
   fi = 0; bi = len(ar) - 1
   while ( fi < bi ):
	   while ( fi < bi and ar[fi] & 0x0001 ): # odd
              fi = fi + 1 # odd next fi .. till find even
	   while ( fi < bi and (ar[bi] & 0x0001 == 0)): # even
              bi = bi - 1 # even .. next bi
           # exchange them
	   ar[fi], ar[bi] = ar[bi], ar[fi]
   print 'OE end  ', ar


#----------------------------------------------------------------

'''
   Fib(n) - print out fibonacci numbers for n iteration
'''
def Fib1(n):
   print 'Fib1(iteration n=',n,'): ',
   p = 0; c = 1
   ar = array.array('l') # integer array <-- much faster
   for i in range(n):
      #print c,  # <-- i/o takes time, so hold till later 
      ar.append(p)
      p, c = c, p + c
   print ar 
   return ar

'''
   Fib(till) - print out fibonacci numbers upto given number or less
'''
def Fib(till):
   print 'Fib(',till,'): ',
   ar = [] # list
   #ar = array.array('l') # integer array, faster than list
   p = 0; c = 1
   i = 0 # iteration count
   while (p <= till):
      i = i + 1
      ar.append(p)
      p, c = c, p + c
   print ar
   print 'iteration count i = ', i
   return ar


class WrapFibT():
   ''' recursion version. exponentially inefficient it seems
   '''
   def fibT(self, n):
	    if n == 0:
		return 0
	    elif n == 1:
		return 1
	    else:
		#print n,
		self.it = self.it + 1 # recursion count
		return self.fibT(n-1) + self.fibT(n-2)

   def T(self, n):
      self.it = 0
      print 'WrapFibT.T(', n , ')'
      t1=time.clock()
      m = self.fibT(n)
      print 'recursion count self.it = ', self.it
      print m 
      t2=time.clock()
      print (t2 - t1), 'sec'

#
# main
#



for func in [ findFirstUniqChar1, findFirstUniqChar2, findFirstUniqChar0 ]:
   findFirstUniqChar = func # alias
   print 'func = ', func

   t1=time.clock()
   findFirstUniqChar(st='geekforgeekhello geek hello geek hello geek hello') # expected 'f'
   testst='geekforgeekhello geek hello geek hello geek hello whatever it will be how long can we have this literal string length to keep saying nonsense hello to geeks without expletives whatever hola hola junk some long running on empty nonsense string without repeating a certain character we know o just testing \
   geekorgeekhello geek hello geek hello geek hello whatever it will be how long can we have this literal string length to keep saying nonsense hello to geeks without expletives whatever hola hola junk some long running on empty nonsense string without repeating a certain character we know o just testing \
   geekorgeekhello geek hello geek hello geek hello whatever it will be how long can we have this literal string length to keep saying nonsense hello to geeks without expletives whatever hola hola junk some long running on empty nonsense string without repeating a certain character we know o just testing \
   geekorgeekhello geek hello geek hello geek hello whatever it will be how long can we have this literal string length to keep saying nonsense hello to geeks without expletives whatever hola hola junk some long running on empty nonsense string without repeating a certain character we know o just testing' # expected 'f'
   print 'testst len = %d' % len(testst)
   findFirstUniqChar(st=testst)

   testst2= testst + 'cfdt now can you still find something'
   print 'testst2 len = %d' % len(testst2)

   findFirstUniqChar(st=testst2) #  expected None
   t2=time.clock()
   print (t2 - t1), 'sec'

sys.exit(0)


t1=time.clock()
a1 = Fib1(30)
t2=time.clock()
print (t2 - t1), 'sec'
print

t1=time.clock()
a = Fib(777777)
t2=time.clock()
print (t2 - t1), 'sec'
print; print

# test
wr = WrapFibT()
wr.T(29)
print; print

# --------  sys.exit(0)

EO(a)
a = [ 2, 5, 11, -3, 7, 8, 0, 9, 17, 12, 15 ]
b = [ 3, 2, -1, 7, 8, 14, -6, 5, 15, 31, 4 ] 
EO(a)
EO(b)
print('------------------------------')
OE(a)
OE(b)
print('------------------------------')

a1 = [ 2, 5, 11, -3, 7, 8, 0, 9, 17, 12, 15 ]
EO1(a1)

print 'main() a is ', a
a.sort()
b.sort()

seta = set(a)
setb = set(b)
print seta
print setb
setab = set(a) | set(b)
print setab
listab = list(setab)
listab.sort()
print listab


print('------------------------------')
#
b = []
EO(b)

print('------------------------------')
#
b.append(3)
b.append(5)
b.append(7)
b.append(4)
EO(b)

print('------------------------------')
#
b = []
b.append(4)
b.append(6)
EO(b)

print('------------------------------')
a = [ 2, 5, -1, 3, 7, -8, 0, -92, -17, 12, 15 ]
EO(a)

