#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# smartify.py
#
# 2022-09-17 by Jeremy Cherfas
#
# Inspired by @drdrang's Smart Quotes in JavaScript
# https://leancrew.com/all-this/2010/11/smart-quotes-in-javascript/
#
#

import sys
import re

def smartify(a):

	a = re.sub("\n'","\n\u2018",a)    # opening single on new line
	a = re.sub("\"'","\"\u2018",a)    # opening single after double
	a = re.sub("\\('",'\\(\u2018',a)  # opening single after + before round bracket
	a = re.sub("'\\(","\u2018\\(",a)  # Tricky! double escape for escaped literal!
	a = re.sub("'","\u2019",a)        # closing single, apostrophe

	a = re.sub("\n\"","\n\u201c",a)   # opening double on new line
	a = re.sub("-\"","-\u201c",a)     # opening double after dash
	a = re.sub('\\(\"','(\u201c',a)   # opening double after + before round bracket
	a = re.sub('\"\\(','\u201c(',a)   # 
	a = re.sub("\"","\u201d",a)       # closing double

	a = re.sub("--","\u2014",a)       # dashes to em dash
	return a
	# not done square bracket, curly bracket, slashes

theSelection = sys.argv[1]

myReplacement = smartify(theSelection)

sys.stdout.write(myReplacement)
sys.stdout.flush()
