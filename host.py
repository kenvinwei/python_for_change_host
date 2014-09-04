#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author kenvinwei
# @date 2014/09/04
# python v3.4.1
import os,string,shutil
basedir="C:/Users/david/Desktop/hosts"
hostpath="C:/Windows/System32/Drivers/etc/hosts"
def readDir(dirs):
	return os.listdir(dirs)
def warnString():
	listfile = readDir(basedir)
	warnstr=""
	for i in range(0,len(listfile)):
		ext = os.path.splitext(listfile[i])[1]
		if(ext == ".hosts"):
			warnstr += "["+str(i+1)+"]:"+listfile[i]+"\n";
	return warnstr;
def writeHost(filepath):
	 shutil.copy(filepath, hostpath)
	 print("copy\t"+filepath+"\tsuccess!")
def run():
	select_host = int(input("please select hosts file:\n"+warnString()))
	file_len = len(readDir(basedir))+1;
	if(select_host>0 and select_host<file_len):
		files = readDir(basedir);
		filenames = basedir+"/"+files[int(select_host)-1]
		writeHost(filenames)
	else:
		print("error index to select!");
if(__name__=="__main__"):
	run()

