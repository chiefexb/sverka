#!/usr/bin/python
#coding: utf8
from lxml import etree
import sys
from os import *
import fdb
import logging
import datetime
import timeit
import time
from odsmod import *
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        #print "Elapsed time:",time.time() - self._startTime # {:.3f} sec".form$
        st=u"Время выполнения:"+str(time.time() - self._startTime) # {:.3f} sec$
        print st
        logging.info(st)
def quoted(a):
 try:
  st=u"'"+a+u"'"
 except:
  st='Null'
 return st
def main():
 logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s',level = logging.DEBUG, filename = './logging.log')
 fileconfig=file('./sverka.xml')
 xml=etree.parse(fileconfig) 
 xmlroot=xml.getroot()
 print xmlroot.tag
 #conf=xmlroot.find('config')
 #dbmass={}
 dbs={}
 dbm=[]
 #выбираем годы
 if len(sys.argv)<=1:
  print ("getfromint: нехватает параметров\nИспользование: sverka.py sverka 2007,2008")
  sys.exit(2)
 print sys.argv[2],sys.argv[3]
 dbm=[]
 for d  in xmlroot.getchildren():
  print d.tag
  #dbs={}
  #dbmass={}
  #выбираем базы за год
  #dbs['year']=d.tag
  print len(d.getchildren())
  for a in d.getchildren():
   print a.tag
   #перебор атрибутов
   dbs={}
   dbs['year']=d.tag
   dbs['alias']=a.tag
   for itms in a.attrib.items():
    dbs[itms[0]]=itms[1]
   dbm.append(dbs)
 print dbm,len(dbm)
 print 'TEST CONN'
 i=0
 for pp in dbm:
  i+=1
  print i,pp['year'],pp['alias'],pp['db']
  try:
   con = fdb.connect (host=pp['host'], database=pp['db'], user='SYSDBA', password=pp['password'],charset='WIN1251')
   con.close()
   print  pp['host'],pp['db'],'OK' 
  except  Exception, e:
   print pp['host'],pp['db'],pp['password'],'FAIL',e
if __name__ == "__main__":
    main()

