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

import pdb

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ is Eleph

import itertools

def weed(p, dbg=0):
   # e.g. p = 1260
   ps = str(p)
   if p < 0 or len(ps) % 2: # odd number
      print 'No %d' % p
      return False
   if p % 1000 == 0: # can't both x,y end with 0
      print "No %d (both ends 0?)" % p
      return False
    
   print '.... given p = %d' % p
   lp = list()  # e.g. lp = [1,2,6,0]
   for i in ps:
      lp.append(int(i))

   # can't both x, y end with 0
   #if (i[len(i)/2 - 1]==0) and (i[len(i) - 1]==0):
   #   if dbg > 0: print 'both can not end w/ 0: x=%d * y=%d = p=%d' % (x,y,p)

   #perm = list(itertools.permutations(lp,4))
   # e.g. perm = [(1,2,6,0), (1,2,0,6), (1,6,2,0), ... ]
   perm = list(itertools.permutations(lp,len(lp)))
   if dbg > 0: print perm

   for i in perm:
      x = 0; y = 0
      for j in range(0, len(i)/2):
	 x = x * 10 + i[j]
      for j in range(len(i)/2, len(i)):
	 y = y * 10 + i[j]
      if dbg > 0: print "   (dbg) x=%d y=%d" % (x,y)

      if x * y == p:
         print 'Yes! x=%d * y=%d = p=%d' % (x,y,p)
	 return True

   print 'No %d' % p
   return False




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ gen Eleph

#def mul2(n):  # multiply 2 numbers, check if it's eleph
def mul2(n, ctrl=1, ifrom=0, itill=0, jtill=0):

   posz = 2 * n  # posision idx to track array's size
   if ifrom==0: # default then we calculate
      ifrom = 1
      for i in range(n-1):
         ifrom = ifrom * 10
   if itill==0: # default then we calculate
      itill = ifrom * 10

   print "ctrl=%d" % ctrl
   print "ifrom=%d itill=%d posz = %d" % (ifrom, itill, posz)
   if jtill==0:
      jtill = itill / 2
      #jtill = itill # ? j till = itill / 2

   #pdb.set_trace()

   t1 = 0; t2 = 0; t3 = 0; # tracking total calculation

   for i in range (ifrom, itill):
      si = str(i)

      for j in range (ifrom, jtill):
         t1 += 1 # stats

         p = i * j
         sj = str(j)
         sp = str(p)
	 if len(sp) % 2: # odd number
	    continue;

         #... extra step to speed up weeding out ...
         noway = False
	 if ctrl==1:
	    for k in range(len(si)):
               if (si[k] not in sp) or (sj[k] not in sp):
	          noway = True 
         if noway:
            continue

         t2 += 1 # stats % (i, t1, t2)

	 # pos = list()
	 pos = array.array('l') # integer array <-- faster
         for xi in range(0,posz):
	    pos.append(0) # [xi] = 0  # init

	 expcnt = 1  # expected cnt init before generate it
	 for xi in range(0,posz):
            expcnt = expcnt * 2 # expected total count to be
	    if pos[xi]==0 and si[0]==sp[xi]:
	       pos[xi] = 1
               continue
	    if pos[xi]==0 and sj[0]==sp[xi]:
	       pos[xi] = 2 
               continue
	    if len(si) < 2: # same for len(sj)
	       continue

	    if pos[xi]==0 and si[1]==sp[xi]:
	       pos[xi] = 4 
	       continue
	    if pos[xi]==0 and sj[1]==sp[xi]:
	       pos[xi] = 8 
	       continue
	    if len(si) < 3: # same for len(sj)
	       continue

	    if pos[xi]==0 and si[2]==sp[xi]:
	       pos[xi] = 16 
	       continue
	    if pos[xi]==0 and sj[2]==sp[xi]:
	       pos[xi] = 32 
	       continue
	    if len(si) < 4: # same for len(sj)
	       continue

	    if pos[xi]==0 and si[3]==sp[xi]:
	       pos[xi] = 64 
	       continue
	    if pos[xi]==0 and sj[3]==sp[xi]:
	       pos[xi] = 128
	       continue
            # ...

	 expcnt = expcnt - 1 
         cnt = 0
	 for xi in range(posz):
	    cnt = cnt + pos[xi]
	 if cnt == expcnt:
	    print "%d x %d = %d " % ( i, j, p )
            t3 += 1 # stats
      
   print 'i=%d) stats: t1=%d, t2=%d, t3=%d' % (i, t1, t2, t3)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

# n is len(x) or len(y) to be
weed(p=312975)
weed(p=31297500)
weed(p=361989)
sys.exit(0)
'''
weed(p=12340)
weed(p=1234)
weed(p=1260)
weed(p=1435)
weed(p=2187)
weed(p=1827)
weed(p=1395)
'''
weed(p=125264)
weed(p=134725)
weed(p=125460)

weed(p=16947328)
weed(p=12546000)
weed(p=31980627)
weed(p=61342879)
weed(p=61342897)

#sys.exit(0)

t1=time.clock()
mul2(n=2, ctrl=1)
mul2(n=3, ctrl=1)
t2=time.clock()
print (t2 - t1), 'sec'
print '~~~~~~~~~~~~~~~~~'

t1=time.clock()
#mul2(n=4, ctrl=1) # too long so...
mul2(n=4, ctrl=1, ifrom=3100, itill=4300, jtill=4300)
t2=time.clock()
print (t2 - t1), 'sec'
print '~~~~~~~~~~~~~~~~~'

slowok = True # <== False
if slowok: # just to show
  t1=time.clock()
  mul2(n=2, ctrl=0)
  mul2(n=3, ctrl=0)
  t2=time.clock()
  print (t2 - t1), 'sec'

sys.exit(1)


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

