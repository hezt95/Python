#!/usr/bin/env python2
import os
import sys
import re
import getopt

def usage():
	
	print "usage:find options dir regex"

	print "options:"

	print "  -h --help:show help message"

	print "  -e --exec command:run the results with command"

	print "dir: the dir you want to search in,current dir as defualt"

	print "regex: .* as defualt"

def searchdir( item , results ,regx ):
	
	try:
	
		sub_item = os.listdir(item)
	
	except:
	
		pass
	
	else:
	
		for objs in sub_item:
		
			path = os.path.join( item , objs )
			
			if regx.search( objs ):
			
				results.append( path )
			
			if os.path.isdir( path ):
			
				searchdir( path , results ,regx )

def show( results ):
	
	for items in results:
	
		print items
			

def execute( results , execer):
	
	for items in results:
	
		if os.system( execer+" "+items ) != 0:
		
			print execer + " "  + item + " Returned -1"
		
		else:
		
			print execer + " "  + items + " Return Normally"


results = [];

isexec=False

root=os.getcwd()

shortargs="e:h"

longargs=["exec=" , "help"]

regx=re.compile(".*")

try:

	opts, args = getopt.getopt( sys.argv[1:] , shortargs , longargs)

except getopt.GotoptError:

	usage()

	quit()


if len( args ) > 2:

	print "Para Mismatch"

	quit()
	
elif len( args ) == 2:
	
	root=args[0]

	regx=re.compile( args[1][1:-1] + "$" )

elif len( args ) == 1:

	if re.search( "\[.*\]" , args[0] ):

		print args[0][1:-1]

		regx=re.compile( args[0][1:-1] + "$" )
	
	else:
		
		root=args[0]

for opt , arg in opts:

	if opt in ( "-h" , "--help" ):
	
		usage()
		
		sys.exit()

	elif opt in ( "-e" , "--exec" ):
		isexec=True

		execer=arg



searchdir( root , results , regx )

show( results )

if isexec:

	execute( results , execer )
