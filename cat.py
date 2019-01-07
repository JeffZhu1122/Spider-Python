# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import re
from xlwt import *
myfile=open("cat.csv","w+")
r=requests.post("https://www.mypetwarehouse.com.au/cat")
urlPattern=re.compile('''<div class="item-grid-inner thumbnail">
            <a href="(.*?)">''')
urlResult=urlPattern.findall(r.text)
p=1
for url in urlResult:
	i=0
	while True:
		i+=1
		ntr=requests.post("https://www.mypetwarehouse.com.au"+url+"?page={}".format(i))
		namePattern = re.compile('''<h4 class="list-item-heading">  (.*?)  </h4>''')
		nameResult = namePattern.findall(ntr.text)
		pricePattern = re.compile('''<div class="lead list-item-.*?">(.*?)</div>''')
		priceResult = pricePattern.findall(ntr.text)
		if len(nameResult)==0:
			break
		for k in range (len(nameResult)):
			print(str(p)+","+nameResult[k]+","+priceResult[k])
			myfile.write(str(p)+","+nameResult[k]+","+priceResult[k]+"\n")
			myfile.flush()
			p+=1
myfile.close()