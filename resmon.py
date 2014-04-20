'''
Python Coding ... task given by Nutanix

The task is to write a resource monitoring class that computes and maintains
resource usage statistics for a set of resources on a machine over time. For
each resource i being monitored, the class should maintain a configurable simple
moving average (i.e., a moving average based on a window of Mi samples with a
sample taken every Ti seconds) that reflects resource usage for the given
resource.

  http://en.wikipedia.org/wiki/Moving_average

For this task, the class should support two resources (CPU and I/O bandwidth)
and three named statistics will be exported:

  1. Aggregate CPU % (0 to 100). stat_name: "cpu"
  2. I/O read bandwidth (in kB/s). stat_name: "io-rkbps"
  3. I/O write bandwidth (in kB/s). stat_name: "io-wkbps"

'''

#-----------------------------------------------------------------------------
#
# Name: Kaoru Takahashi
# Date: 9/10/2013
#


import sys
import os
import time
import threading
import random

# class Resource()
# @description: base class for Resource to be monitored
#       it keeps the measured sampling data in a queue.
# Note: __samplingMethod__() is resource type specific and to be 
#       implemented in the extended class
#
class Resource(object):
   unit  = '?' 
   def __init__(self, name, qsize):  # qsize (N recent measured data)
      print 'dbg Resource.__init__() '
      self.name  = name     # resource stat_name 
      self.qsize = qsize 
      self.Q = []  # to hold measured sampling data
      self.drop = None # oldest data to drop from Q
      self.SMA = 0 # latest simple moving average

   # performance measuring method, extended class should implement.
   # @returns measured data (unit could be usage %, could be bpts, etc.)
   def __samplingMethod__(self):
      print 'dbg Resource.sampling(): Not Impelemented Error'
      return 0

   # keeps the sampled data in the queue in oldest to newest
   # if full drop the oldest data to make space
   def sampleData(self):
      if len(self.Q) >= self.qsize:
         self.drop = self.Q.pop(0) # the oldest data to drop
	 #
	 #print 'dbg self.drop = %f' % self.drop

      # __samplingMethod__() call is a virtual method
      self.Q.append(int(self.__samplingMethod__()))  # <- readability for testing
      #self.Q.append(self.__samplingMethod__())      # float 
      print self.Q  # DEBUG


   # calculate simple moving average
   # as per http://en.wikipedia.org/wiki/Moving_average
   def calc(self):
      if len(self.Q) == 0:
	 return 0
      if len(self.Q) <= self.qsize: # initially not enough sampling data
         ttl = 0  
	 for data in self.Q:
	    ttl += data
         self.SMA = ttl / len(self.Q) # just a regular average	
      else: # thereafter ... use SMA calculation 
         self.SMA = self.SMA - self.drop / self.qsize + self.Q[-1] / self.qsize


#------------------------------------------------------------------------------

class CpuResource(Resource):
   unit = 'aggregated cpu usage %'   # <-- cls var.
   def __init__(self, name, qsize):  # qsize (N recent measured data)
      super(CpuResource, self).__init__(name, qsize)
      print 'dbg CpuResource.__init__() '
   def __samplingMethod__(self):
      print 'dbg CpuResource.__sampling__():  TBD '
      # TBD - pls replace with a real sampling logic
      return random.uniform(0,100) # <-- FAKE returns 0 ~ 100 (%)

class CpuResourceEach(CpuResource):
   unit = 'each cpu usage %'   # <-- cls var.
   def __init__(self, name, qsize):  # qsize (N recent measured data)
      super(CpuResourceEach, self).__init__(name, qsize)
      print 'dbg CpuResourceEach.__init__() '
   def __samplingMethod__(self):
      print 'dbg CpuResourceEach.__sampling__():  TBD '
      # TBD - pls replace with a real sampling logic
      return random.uniform(0,100) # <-- FAKE returns 0 ~ 100 (%)


class IoRkbpsResource(Resource):
   unit = 'I/O read Kbyte/sec'
   def __init__(self, name, qsize):  # qsize (N recent measured data)
      super(IoRkbpsResource, self).__init__(name, qsize)
      print 'dbg IoRkbpsResource.__init__() '
   def __samplingMethod__(self):
      print 'dbg IoRkbpsResource.__sampling__():  TBD '
      # TBD - pls replace with a real sampling logic
      return random.uniform(0,1000) # <-- FAKE returns 0 ~ 1000 (kbps)


class IoWkbpsResource(Resource):
   unit = 'I/O write Kbyte/sec'
   def __init__(self, name, qsize):  # qsize (N recent measured data)
      super(IoWkbpsResource, self).__init__(name, qsize)
      print 'dbg IoWkbpsResource.__init__() '
   def __samplingMethod__(self):
      print 'dbg IoWkbpsResource.__sampling__():  TBD '
      # TBD - pls replace with a real sampling logic
      return random.uniform(0,1000) # <-- FAKE returns 0 ~ 1000 (kbps)



#------------------------------------------------------------------------------


class ResourceMonitor(object):
  torun = False
  emergencybreak = False
  MAXloop = 111  # just in case it exceeds, emergency break stop
  thName = '' # thread name

  # @param freq  : frequency for sampling, e.g. every 5 seconds
  # @param nsamp : max recent number of sampled data per resource to keep
  def __init__(self, freq=5, nsamp=10): 
     self.freq = freq  
     self.reslist = []
     # [0] - Aggregate CPU % (0 to 100). stat_name: "cpu"
     self.reslist.append(CpuResource(name='cpu', qsize=nsamp))
     # [1] - I/O read bandwidth (in kB/s). stat_name: "io-rkbps"
     self.reslist.append(IoRkbpsResource(name='io-rkbps', qsize=nsamp))
     # [2] - I/O write bandwidth (in kB/s). stat_name: "io-wkbps"
     self.reslist.append(IoWkbpsResource(name='io-wkbps', qsize=nsamp))
     # [3] - CPU 0 % (0 to 100). stat_name: "cpu0"
     self.reslist.append(CpuResourceEach(name='cpu0', qsize=nsamp))

     # to lookup via stat_name as key
     self.resd = dict() # monitored resource instance as value
     for r in self.reslist:
        self.resd[r.name] = r

  def startMon(self):
     j = 0
     while self.torun:
        print "\n===== Thread: %s   j=%d :-)" % (self.thName, j)

        for res in self.reslist:
            res.sampleData()
            res.calc() # to keep latest data
        time.sleep(self.freq)
	j += 1 
	# just in case, out of control and can not stop this thread...
	# indicate to get out when j reached a max limit, 
	if j > self.MAXloop: # TEST <=== 
           print ' startMon() reached MAXloop, Getting out of here! Bye '
           self.torun = False
           self.emergencybreak = True # <-- main() caller has to see this
	   return

  def Start(self):
      self.torun = True 
      print 'Start: torun=' + str(self.torun)
  def Stop(self):
      self.torun = False
      print 'Stop: torun=' + str(self.torun)

  # Get the latest value (moving average) for the statistic 'stat_name'.
  def GetStatistic(self, stat_name):
      res = self.resd[stat_name]
      print 'dbg stat_name %s simple moving average=%2f (%s)' % (stat_name, res.SMA, res.unit)
      return res.SMA


#-----------------------------------------------------------------------------
# main
#

if __name__ == '__main__':

   # configurable. just for testing.
   # resmon = ResourceMonitor(freq=1, nsamp=7)
   resmon1 = ResourceMonitor(freq=1, nsamp=5)
   resmon2 = ResourceMonitor(freq=1, nsamp=8)
   t1 = threading.Thread(target=resmon1.startMon) # <== 
   t2 = threading.Thread(target=resmon2.startMon) # <== 

   # now keeping given thread names in each instance
   resmon1.thName = t1.getName() + "(woof)";
   resmon2.thName = t2.getName() + "(peep)";

   # just init var, NOT like starts running 
   resmon1.Start()
   resmon2.Start()
   print 'resmon.MAXloop is ', resmon1.MAXloop 


   t1.start() # <== this actually starts running the thread
   t2.start() # <== this actually starts running the thread

   for i in range(5):
      resmon1.Start() # resume / start again
      resmon2.Start() # resume / start again
      try:
         time.sleep(5)
      except KeyboardInterrupt: # catch here before Thread ignores it
         resmon1.Stop()
         resmon2.Stop()
	 print '...  User wants to stop. bye'
	 sys.exit(0)

      resmon1.Stop()
      resmon2.Stop()
      print "t1 name: ", t1.getName();
      resmon1.GetStatistic(stat_name='cpu')
      resmon1.GetStatistic(stat_name='io-rkbps')
      resmon1.GetStatistic(stat_name='io-wkbps')
      resmon1.GetStatistic(stat_name='cpu0')
      print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
      print "t2 name: ", t2.getName();
      resmon2.GetStatistic(stat_name='cpu')
      resmon2.GetStatistic(stat_name='io-rkbps')
      resmon2.GetStatistic(stat_name='io-wkbps')
      resmon2.GetStatistic(stat_name='cpu0')
      print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

      if resmon1.emergencybreak or resmon2.emergencybreak:
         print ' ... Emergency Break!! ...'
	 sys.exit(1)
         

   t1.join()
   t2.join()
   print 'main says thank you "resmon thread". bye'
