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
import pickle
import random
import pdb


class Mini(object):
   miniA = 'miniA default constant'
   defMini = 77
   def __init__(self):
      print 'Mini.__init__() called'

class Defs(object):
   defI = 33333
   defJ = 55555
   defK = 77777

class Test(object):
     defI = 3; defJ = 5
     yesno = False 

     def __init__(self, i, j):
        print 'Test.__init__() called'
	self.i = i; self.j = j; self.mini = Mini()

     def showdef(cls):
	print "%s - defI=%d, defJ=%d" % (type(cls), cls.defI, cls.defJ)
	print "%s - Test.defI=%d, Test.defJ=%d" % (type(cls), Test.defI, Test.defJ)

     def show(self):
	print "self.i=%d, self.i=%d" % (self.i, self.i)
	print "... and self.defJ is %d" % self.defJ

     def stop(cls): # can we change value?
	if cls.yesno:
	   cls.yesno = False
	   print "yesno was True -> False"
	else:
	   cls.yesno = True
	   print "yesno was False -> True"
	

class Test2(Test):
     defK = 7 
     '''
     def __init__(self, i, j, k):
        super(Test2,self).__init__(i, j) 
        print 'Test2.__init__() called'
	self.k = k
     '''

     # providing class default values as parameters ... to create
     #def __init__(self, i=Test.defI, j=Test.defJ, k=Mini.defMini): # =Test2.defK):
     def __init__(self, i=Defs.defI, j=Defs.defJ, k=Defs.defK): # =Test2.defK):
        super(Test2,self).__init__(i, j) 
        print 'Test2.__init__() called'
	self.k = k


     def show(self):
        super(Test2,self).show()
	print "self.k=%d " % (self.k)
     def showdef(cls):
        super(Test2,cls).showdef()
	print "defK=%d" % (cls.defK)
	print "Test2.defK=%d" % (Test2.defK)

     def pk(self, fname=''):  # picklin'
	#with open('c:/users/kaoru/Py/out1', 'rw') as f2
	with open(fname, 'w') as f:
	   pickle.dump(self, f)
	

#-----------------------------------------------------------------------------

def mkbrick(sm, bg, goal):
    ''' small brick is 1 inch long, big brick is 5 inch long.
        can we make a row of goal inches w/ given number of bricks?
      e.g.   mkbrick(sm=3, bg=1, goal=8) => True
      e.g.   mkbrick(sm=3, bg=1, goal=9) => False
      e.g.   mkbrick(sm=3, bg=2, goal=10) => True
    '''
    # a bit efficient combination
    print '\ngiven (sm=%d, bg=%d, goal=%d)' % (sm,bg,goal)

    # PDB Debug
    pdb.set_trace()

    # basic check - go or no go
    if (bg * 5 + sm * 1) < goal:
       print 'False: can not do'
       return False

    res = 0;
    for i in range(bg): 
       res += 5
       print '(dbg) res=%d ' % res
       if goal == res:
	  print 'True: exact 5 * %d makes it' % (i+1) 
          return True
       if goal < res:
	  res -= 5 # undo last
	  break

    res2 = res
    for j in range(sm):
       res2 += 1
       print ' (dbg) res2=%d ' % res2
       if goal == res2:
	  print 'True: 5 * %d + %d makes it' % (res / 5, j+1) 
          return True

    print 'False: did not meet'
    return False



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
		m = self.fibT(n-1) + self.fibT(n-2)
		#print m,
		return m

   def T(self, n):
      self.it = 0
      print 'WrapFibT.T(', n , ')'
      t1=time.clock()

      m = self.fibT(n)
      print 'recursion count self.it = ', self.it
      print 'final result = ', m 

      t2=time.clock()
      print (t2 - t1), 'sec'

#
# main
#


print Test.defI, Test.defJ
print Test2.defK
print Test2.yesno
Test2.yesno = True
print Test2.yesno

#sys.exit(0)


t2 = Test2(i=1, j=20, k=300)
t2.show()
t2.showdef()
t2.stop() # yesno
t2.stop() # yesno

print '\n~~~~~~ w/ all default ~~~~~~~~~~~~~~~'
t3 = Test2() # (i=1, j=20, k=300)
t3.show()
t3.showdef()


sys.exit(0)

fname='C:\Users\kaoru\Py\out1'
t2.pk(fname=fname)

print '-- in main --'
with open(fname, 'r') as f:
   t22 = pickle.load(f)
   print t22 
with open(fname, 'r') as f:
   t20 = pickle.load(f)
   print t20 

t22.show()
t20.show()

'''
mkbrick(sm=3, bg=1, goal=8) # => True
mkbrick(sm=3, bg=1, goal=9) # => False
mkbrick(sm=3, bg=2, goal=10)#  => True
mkbrick(sm=6, bg=2, goal=11)#  => True
mkbrick(sm=6, bg=1, goal=11)#  => True
mkbrick(sm=16, bg=0, goal=11)#  => True
mkbrick(sm=7, bg=0, goal=8)#  => True
mkbrick(sm=7, bg=2, goal=18)#  => True
sys.exit(0)
'''



# PDB Debug
pdb.set_trace()

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
wr.T(11)
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

