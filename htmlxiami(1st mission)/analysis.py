# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import urllib2
import re
html=urllib2.urlopen("http://www.baidu.com/s?wd=seo&rn=100").read()
soup=BeautifulSoup(html)
results = soup.find_all(class_=re.compile("result"))
for links in results:        
         print links.h3.get_text()
         print links.span.get_text()