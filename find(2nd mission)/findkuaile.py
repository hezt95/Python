#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys;
import os;
import getopt;
import re;

# A function to print out usage and exit with exception.
def help():
	print """
Usage:
	find.py [--exec command] path [regex]
""";
	sys.exit(1);

if __name__ == "__main__":
	
	try:
		execCommand = None; # If not None, the command will be executed.
	
		opts, args = getopt.getopt(sys.argv[1:], "e:h", ["exec=", "help"]);
		#print "opts:", opts;
		#print "args:", args;
		
		for opt, arg in opts:
			if opt in ["-e", "--exec"]:
				execCommand = arg;
			if opt in ["-h", "--help"]:
				help();
			
		if args.count > 0: # Then we run.
			dir = args[0]; # We know it.
			for dirpath, dirnames, filenames in os.walk(dir): # We walk it.
				for filename in filenames: # Get every filename.
					regEx = None;
					if len(args) == 1: # If the regEx argument isn't given, use the default one.
						regEx = re.compile(".+");
					else:
						regEx = re.compile(args[1]);
						#regEx = re.compile(args[1][1:-1]); # 哪有参数里带中括号的，你逗我！
						
					if regEx.search(filename): # We find it!
						filepath = os.path.join(dirpath + os.sep, filename);
						if execCommand is not None:
							os.system(execCommand + " \"" + filepath + "\""); # The command's output will mix into Python's output.
						print filepath;
		else:
			help();
		
	except getopt.GetoptError, e:
		print e;
		help();
	
