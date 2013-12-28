#!/usr/bin/python2
# -*- coding: utf-8 -*- 
import os
import getopt
import sys
import re
def findit(rootDirectory,content,pathlist):
#搜索函数
    try:  
        listsdir = os.listdir(rootDirectory)
        for lists in listsdir: 
	        path = os.path.join(rootDirectory, lists)  
	        if content.search(path) :
                 print path
                 pathlist.append(path)
	        if os.path.isdir(path): 
	             findit(path,content,pathlist)
    except:
	    pass
def usage():
    print '''Help Information:
            -h: Show help information
            You should wirte your parameter in this way:
                findit /path/to/directory/ [".*"]
            HOW TO USE --exec TO OPEN WHAT YOU FOUND WITH THE COMMAND YOU ORDERED:
                findit /path/to/directory/ [".*"] --exec command'''


if __name__=='__main__':
    #set default values
    x=1
    y='y'
    pathlist =[]
    try:
        opts,args=getopt.getopt(sys.argv[1:],'hx:y:d')
        #opts 是带-选项的参数
        #args 是没有选项的参数
        #h表示使用-hlen,h选项没有对应的值
    except getopt.GetoptError:
        #打印帮助信息并退出
        usage()
        sys.exit(2)
    for o in opts:
        if o == '-h':
            usage()
            sys.exit()
    try :
        if len(sys.argv)>=2 :
            print sys.argv[2]
            print args[1]
            rootDirectory = args[0]
            content = re.compile(args[1][1:-1] + '$')
            findit(rootDirectory,content,pathlist)
            try:
                for a in args:
                    if a== '--exec':
                        command_ = args[3]
                        print command_
                for found in pathlist:
                        os.system(command_+' '+found)
            except : pass
        else :
            print args
            rootDirectory = "./"
            content = re.compile(".*") 
            findit(rootDirectory,content,pathlist)
    except :
        usage()
        sys.exit()


