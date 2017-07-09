import string
import feedparser
import os

while 1:
  print'.',
  d = feedparser.parse('http://www.ansa.it/sito/ansait_rss.xml')
  idx = len(d['items'])
  if idx > 0:
    break

tmp_path="/tmp/"

if ( idx < 10):
  myidx=idx
else:
  myidx=10
  
while( myidx):
  idx1 = 0
  e = d['items'][ myidx]

  titolo=e['title']

  descrizione=e['description']

  myfile=tmp_path+"ansa_news-"+str(myidx)+".txt"

  fansa = open(myfile, 'wb+')
  titolo_out = titolo.encode('utf-8')
  fansa.write( " "+titolo_out+". ")

  descrizione_out = descrizione.encode('utf-8')
  fansa.write( " "+descrizione_out+".\n")
  fansa.close()

  print titolo_out
  print " "+descrizione_out+"\n"

  myidx=myidx-1

