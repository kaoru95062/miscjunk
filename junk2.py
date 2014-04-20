#
# some comments to be ignored 
# 
# 2012ca540 Miy......  
# Jal jbm 4983693 hash....
#

import sys
import os
import time
import array


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

t1=time.clock()
a1 = Fib1(26)
t2=time.clock()
print (t2 - t1), 'sec'
print
for i in range(26):
   print a1[i],
print; print

t1=time.clock()
a = Fib(77777)
t2=time.clock()
print (t2 - t1), 'sec'
print; print

# test
wr = WrapFibT()
wr.T(25)

# --------  sys.exit(0)

a = Fib(5555)
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
print 'set(a)= ', seta
print 'set(b)= ', setb
setab = set(a) | set(b)
print 'union... set(a) | set(b) is ', setab
print 'intersection... set(a) & set(b) is ', set(a) & set(b)
print 'xor... set(a) ^ set(b) is ', set(a) ^ set(b)
seta_b = set(a) - set(b)
print 'only in set(a)... set(a) - set(b) is ', seta_b
setb_a = set(b) - set(a)
print 'only in set(b)... set(b) - set(a) is ', setb_a

print('------------------------------')


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

