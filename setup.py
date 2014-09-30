#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author kenvinwei
# @date 2014/09/04
# python v3.4.1
import sys;
from cx_Freeze import setup, Executable;
build_exe_options = {
    "packages"  : ["sys","os","string","shutil","stat"],
    #"includes" : ["PIL"],
    "include_files" : [".\\hosts"],
    #"icon"      : "host.jpg",  
};
base = None;
if sys.platform == "win32":
	base = "Win32GUI"
setup(name = "hello",
	  version = "0.1",
	  description = "script",
      options = {"build_exe": build_exe_options},
      executables = [Executable("host.py")])