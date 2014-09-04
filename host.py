#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author kenvinwei
# @date 2014/09/04
# python v3.4.1
import os,string
basedir="C:/Users/david/Desktop/hosts"
hostpath="C:/Windows/System32/Drivers/etc/hosts"
def readDir(dirs):
	return os.listdir(dirs)
def warnString():
	listfile = readDir(basedir)
	warnstr=""
	for i in range(0,len(listfile)):
		warnstr += "["+str(i+1)+"]:"+listfile[i]+"\n";
	return warnstr;
def writeHost(filepath):
	 file1 = open(filepath,'r');
	 content = file1.read()
	 file2 = open(hostpath,"w")
	 file2.write(content)
	 file1.close()
	 file2.close()
	 print("write content:!\n"+content+"\n success!")
select_host = int(input("please select hosts file:\n"+warnString()))
file_len = len(readDir(basedir))+1;
if(select_host>0 and select_host<file_len):
	files = readDir(basedir);
	filenames = basedir+"/"+files[int(select_host)-1]
	writeHost(filenames)
else:
	print("error index to select!");
