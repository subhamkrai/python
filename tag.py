from bs4 import BeautifulSoup as bs
import urllib2
import sys
h=raw_input()
hh =sys.argv[1]
w= urllib2.urlopen(h)
soup = bs(w.read(),"lxml")
x= soup."hh".text
print x
