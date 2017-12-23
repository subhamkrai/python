#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
import time
import  commands
print "content-type:text/html"
print ""

webdata=cgi.FieldStorage()
name=webdata.getvalue('u')
size=webdata.getvalue('p')

check=commands.getstatusoutput("sudo lvcreate --name "+name+" --size "+size+" cloudvg")

if check[0]  == 0 :
	print  "successfully created drive "+name
	print  "formating your drive "
	print  "plz wait"
	time.sleep(2)
	print  commands.getoutput('sudo mkfs.xfs  /dev/cloudvg/'+name)
	print  "mounting your drive!!"
	commands.getoutput("sudo mkdir /var/www/html/"+name)
	commands.getoutput("sudo mount  /dev/cloudvg/"+name+" /var/www/html/"+name)
	print  "plz wait sharing your drive with NFS "
#	print "<meta http-equiv='refresh' content=0;http://127.0.0.1/saas.html>"
        
else :
	print  "drive name already taken by someone plz try another name"
	print "<meta http-equiv='refresh' content=5;http://192.168.10.87/index.html>"


