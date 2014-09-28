#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author kenvinwei
# @date 2014/09/04
# python v3.4.1
import sys,os,string,shutil,stat
basedir="C:/Users/david/Desktop/hosts"
hostpath="C:/Windows/System32/Drivers/etc/hosts"
version = "1.10";
def readDir(dirs):
	return os.listdir(dirs)
def warnString():
	#print(oct(os.stat(hostpath).st_mode)[-3:]); #获取文件权限 oct十进制转化为八进制
	listfile = readDir(basedir)
	warnstr=""
	for i in range(0,len(listfile)):
		ext = os.path.splitext(listfile[i])[1]
		if(ext == ".hosts"):
			warnstr += "\t["+str(i+1)+"]:"+listfile[i]+"\n";
	return warnstr;
def writeHost(filepath):
	 #添加可写权限
	 os.chmod( hostpath , stat.S_IWOTH+stat.S_IWUSR+stat.S_IWGRP );
	 shutil.copy(filepath, hostpath)
	 print("copy\t"+filepath+"\tsuccess!")
def get_version():
	return 'author by kenvinwei '+version;
def cat_host():
	host_txt = "";
	f = open(hostpath,'r');
	while True:
		line = f.readline();
		if len(line)==0:
			break;
		host_txt += line;
	f.close();
	return host_txt;
def clear_host():
	f = open(hostpath,'w');
	f.write('127.0.0.1 localhost');
	f.close();
	return 'reset success';
def do_default():
	return  False;
def add_host():
	if sys.argv[2:]:
		f = open(hostpath,'a');
		f.write("\n"+"\t".join(sys.argv[2:]));
		f.close();
		return "\t".join(sys.argv[2:])+'\tsuccess';
	return False;
def command_do():
	do = "".join(sys.argv[1:2]);
	if(do):
		result = {
			'-version' : get_version, #获取当前版本
			'-V' : get_version,  #获取当前版本
			'-cat' : cat_host, #查看当前 host 内容
			'-clear' : clear_host, #清楚 host 内容
			'-add' : add_host, #在当前的host文件上追加内容
		}
		res = result.get(do,do_default)();
		return res;
def run():
	#开始解析命令
	result = command_do();
	if result:
		print(result);
		exit();
	#default and select
	select_host = int(input("please select hosts file:\n"+warnString()))
	file_len = len(readDir(basedir))+1;
	if select_host>0 and select_host<file_len:
		files = readDir(basedir)
		filenames = basedir+"/"+files[int(select_host)-1]
		writeHost(filenames)
		#清空dns(仅用于win系统下)
		os.system("ipconfig/flushdns")
	else:
		print("error index to select!");
if __name__=="__main__":
	run();