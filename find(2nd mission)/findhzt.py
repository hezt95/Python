#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import os
import sys
import os.path
import re
import getopt
def usage():  
    print """
Usage:
	./findhe.py [--exec command] /path/to/directory/ [regEx]
""";
files = [];
try:
	execCommand = None;
	opts,args = getopt.getopt(sys.argv[1:], "", ["exec="]);
	for opt, arg in opts:
			if opt in ["-e", "--exec"]:
				execCommand = arg;
			else:
				usage();
				sys.exit();
	if len(args) > 2:
		usage();
		sys.exit();
	elif len(args) == 2:
		path = args[0];
		regEx = re.compile( args[1][1:-1] + "$" );
		#print path
		print regEx
	elif len(args)==1:
		if re.search("[.*]",args[0]):
			usage();
			sys.exit();
		else:
			path = args[0];
			regEx = re.compile(".+");
	for dirpath, dirnames, filenames in os.walk(path):
		for filename in filenames:
			if re.search(regEx,filename):
				filepath = os.path.join(dirpath, filename);
				if execCommand is not None:
					os.system(execCommand + " \"" + filepath + "\"");
				files.append(filepath);
	if len(files) == 0:
		print 'Noting'
	for items in files:
		print items

except:
	usage();
	sys.exit();

