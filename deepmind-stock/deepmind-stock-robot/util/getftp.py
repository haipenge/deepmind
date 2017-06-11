#!/usr/bin/env python
#-*- coding:utf-8 -*-
from ftplib import FTP
import os
import socket



def getfile(remoteIp,port):
        port=int(port)
        cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        cs.connect((remoteIp,port))
        cs.send('1')
        filename=cs.recv(1024)
	#print filename
        flist=filename.split()
	return flist





def ftp_down(remoteIp,port,filename):
	os.chdir('/usr/appbak')
	ftp=FTP()
	ftp.set_debuglevel(2)
	ftp.connect(remoteIp,port)
	print "aa"
	ftp.login('appbak','sfc_appbak')
	print "bbb"
	#ftp.cwd('xxx/xxx/')
	bufsize = 1024
	#filename = "20120904.rar"
	file_handler = open(filename,'wb').write
	ftp.retrbinary('RETR %s' % os.path.basename(filename),file_handler,bufsize)
	ftp.set_debuglevel(0)
	#file_handler.close()
	ftp.quit()
	print "ftp down OK"

flist=getfile('202.105.131.228','7777')
print flist
for fi  in flist:
	ftp_down('202.105.131.228','21',fi)
