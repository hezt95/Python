#!/usr/bin/env python2
# -*-coding:utf-8 -*-
import os,sys,re

def _Find_Conf(path,string):
    """遍历给定目录，搜寻conf目录或文件"""
    ilist=os.listdir(path)
    for item in ilist:
        itemsrc = os.path.join(path, item) #将文件连入目录
        if os.path.isdir(itemsrc):
            _Find_Conf(itemsrc,string)             # 递归进入子目录
        elif _End_With(item,string):
            print itemsrc

def _End_With(s,*endstr):
    """匹配后缀名"""
    array = map(s.endswith,endstr)
    if True in array:
        return True
    else:
        return False

def usage():
    print '帮助命令 ./find.py -h'
    print '执行命令 ./find.py /path/to/directory/file --exec command'
    print '搜索命令 ./find.py /path/to/directory/ [".*.typename"]'
    print '======================错误信息概览============================'
    print ' -1：检索过程错误      0：command参数表达式错误'
    print ' 1：command执行错误  2：检索表达式错误'

if __name__=='__main__':
    """主函数部分"""
    if len(sys.argv)>=2:
        path=sys.argv[1]
    else:
        print "Invalid format! Use -h to get help! return -2"
        sys.exit(-2)

    if os.path.exists(path):                    #检查路径是否正确
        if sys.argv[2].startswith("--exec") and len(sys.argv)>2:  #检查是否需要command运行
            try:
                os.system("%s %s"%(sys.argv[3],path))
            except:
                print "Invalid format! Use -h to get help! return 1"
        elif re.search(r'(\[.+\])',sys.argv[2])!=None and len(sys.argv)==2:   #检查需检索的文件是否合格
            try:
                istr=re.search(r'(\*)(.+)(\])',sys.argv[2]).group(2)
                _Find_Conf(path,istr)
            except:
                print "Invalid format! Use -h to get help! return -1"
        else:                                                       #不合格的检索表达式将产生错误信息
            print "Invalid format! Use -h to get help! return 0"
    elif sys.argv[1].startswith("-h"):               #检查是否输入提示帮助
        usage()
    else:
        print "Invalid format! Use -h to get help! return 2"
