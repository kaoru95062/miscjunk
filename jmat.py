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


#----------------------------------------------------------------
#  ..... playing around Matrix (2D array) rotations ..... 
#        ( 90dig rotation ... Transpose and mirror image? )

class M(object):
   A = 'Antelope'; B = 'Bear';  C = 'Cat';   D = 'Deer';  E = 'Elk'; F = 'Fox';
   G = 'Giraffe'; H = 'Horse'; I = 'Ibx'; J = 'Jackal'; K = 'Kangaroo';
   L = 'Lama'; M = 'Monkey'; N = 'Newt'; O = 'Okapi';
   P = 'Puma'; Q = 'Quatzel'; R = 'Rodent'; S = 'Sloth'; T = 'Tiger';
   U = 'Ummm?'; V = 'Volture'; W = 'Wombat'; X = 'X?'; Y = 'Yak'; Z = 'Zebra';

   def __init__(self, N=4):
      self.Num = N
      self.Q1 = [[0 for i in xrange(N)] for i in xrange(N)]
      self.Q2 = [[0 for i in xrange(N)] for i in xrange(N)]
      self.Q3 = [[0 for i in xrange(N)] for i in xrange(N)]
      self.Q4 = [[0 for i in xrange(N)] for i in xrange(N)]
       
   def assign4(self):
      self.Q1[0][0] = self.A; self.Q1[0][1] = self.B; self.Q1[0][2] = self.C; self.Q1[0][3] = self.D; 
      self.Q1[1][0] = self.E; self.Q1[1][1] = self.F; self.Q1[1][2] = self.G; self.Q1[1][3] = self.H; 
      self.Q1[2][0] = self.I; self.Q1[2][1] = self.J; self.Q1[2][2] = self.K; self.Q1[2][3] = self.L; 
      self.Q1[3][0] = self.M; self.Q1[3][1] = self.N; self.Q1[3][2] = self.O; self.Q1[3][3] = self.P; 


   def show(self, Quad, quadname):
      print '\n=== M[y][x] %s ===' % quadname
      for i in range(self.Num):
	 s = ''
         for j in range(self.Num):
	    s = s + '[%d][%d]=%-8s ' % (i,j, Quad[i][j])
	 print s

   # formula/pattern: [y,x] ...  # newY = oldX; newX = Num-1 - oldY 
   # e.g. mt.rotateL90(fromQuad=mt.Q1, destQuad=mt.Q4, note="from Q1 to Q4")
   def rotateL90(self, fromQuad, destQuad, note):
      print '\n== %s Rotate Left 90 degree (or R 270): dest[Y,X] .. destY=fromX; destX=from(N-1-fromY)' % note 
      for y in range(self.Num):
         for x in range(self.Num):
            destQuad[y][x] = fromQuad[x][self.Num-1 - y] 
	    print 'dest[%d][%d] = from[%d][%d]' % (y,x, x,self.Num-1-y) 
	 print
       
   # formula/pattern: [y,x] ...  # newY = Num-1 - oldX; newX = oldY 
   # e.g. mt.rotateR90(fromQuad=mt.Q1, destQuad=mt.Q2,  note="from Q1 to Q2")
   def rotateR90(self, fromQuad, destQuad, note):
      print '\n== %s Rotate Right 90 degree : dest[Y,X] .. destY=fromX; destX=from(N-1-fromY)' % note
      for y in range(self.Num):
         for x in range(self.Num):
            destQuad[y][x] = fromQuad[self.Num-1 - x][y] 
	    print 'dest[%d][%d] = from[%d][%d]' % (y,x, self.Num-1-x, y) 
	 print


#----------------------------------------------------------------
#  ..... playing around for class inheritance .....
class Mini(object):
   miniA = 'miniA default constant'
   def __init__(self):
      print 'Mini.__init__() called'

class Test(object):
     defI = 3
     defJ = 5
     def __init__(self, i, j):
        print 'Test.__init__() called'
        self.i = i; self.j = j 
        self.mini = Mini()
     def showdef(cls):
        print "%s - defI=%d, defJ=%d" % (type(cls), cls.defI, cls.defJ)
     def show(self):
        print "self.i=%d, self.i=%d" % (self.i, self.i)
        print "... and self.defJ is %d" % self.defJ

class Test2(Test):
     defK = 7
     def __init__(self, i, j, k):
        super(Test2,self).__init__(i, j)
        print 'Test2.__init__() called'
        self.k = k
     def show(self):
        super(Test2,self).show()
        print "self.k=%d " % (self.k)
     def showdef(cls):
        super(Test2,cls).showdef()
        print "defK=%d" % (cls.defK)
     # pickling
     def pk(self, fname=''):
        #with open('c:/users/kaoru/Py/out1', 'rw') as f2
        with open(fname, 'w') as f:
           pickle.dump(self, f)


#----------------------------------------------------------------
# main
#

mt = M() # 4 x 4 ... demo
mt.assign4()
mt.show(mt.Q1, "Quad 1")
mt.rotateR90(fromQuad=mt.Q1, destQuad=mt.Q2, note="from Q1 to Q2")
mt.show(mt.Q2, "Quad 2")
mt.rotateR90(fromQuad=mt.Q2, destQuad=mt.Q3, note="from Q2 to Q3")
mt.show(mt.Q3, "Quad 3")
mt.rotateR90(fromQuad=mt.Q3, destQuad=mt.Q4, note="from Q3 to Q4")
mt.show(mt.Q4, "Quad 4")


mt.rotateL90(fromQuad=mt.Q1, destQuad=mt.Q4, note="from Q1 to Q4")
mt.show(mt.Q4, "Quad 4")

mt.rotateR90(fromQuad=mt.Q4, destQuad=mt.Q1, note="from Q4 to Q1")
mt.show(mt.Q1, "Quad 1")

sys.exit(0)




t2 = Test2(i=1, j=20, k=300)
t2.show()
t2.showdef()
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

sys.exit(0)



