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
 for ch  in xmlroot.getchildren():
  print ch.tag
  dbs={}
  #dbmass={}
  #выбираем базы за год
  dbs['year']=ch.tag
  for chh in ch.getchildren():
   #dbmass={} 
   #перебор атрибутов
   for ch2 in chh.attrib.keys():
    print ch2
    dbs[ch2]=chh.attrib[ch2]
   dbm.append(dbs)
  #dbm[ch.tag]=dbmass
 print dbm,len(dbm)
 print 'TEST CONN'
 for pp in dbm:
  print pp['year']
  try:
   con = fdb.connect (host=pp['host'], database=pp['db'], user='SYSDBA', password=pp['password'],charset='WIN1251')
   print  pp['host'],pp['db'],'OK' 
  except  Exception, e:
   print pp['host'],pp['db'],pp['password'],'FAIL',e
 #main_dbname=main_database.find('dbname').text
if __name__ == "__main__":
    main()

