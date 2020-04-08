#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 08 Apr 2020
# Solution for question 1. This module read out the EDIFACT data from the file SampleTextOne. It splits the text by 
# end delimiter(which by default as single quote), into segments. Then split the designated segments into elements 
# with plus sign as delimiter. It populate the elements from the required positions in the segments into a 2D array.


# Note 08 Apr 2020:
# If the size of the EDIFACT message text is huge, consider to load into a database table first, convert into JSON or XML file
# so that it wouldn't cause isseu for the memory.
# Here in this example, it is assumed to be managable size of string.

import sys 
import logging

# This function receives the message to be processed, the end delimiter for spliting segments and delimiter for spliting
# elements in the segment. And return an array of elements on the required positions in the segment.
# Parameter:  message_text: The message text to be processed.
# Parameter: positions: the required positions on each segment where the element are retrieved
# Parameter: segment_name: the specific segment looked for, LOC by default
# Parameter: delimiter: delimiter for spliting the segments into elements, plus sign by default
# Parameter: end_delimiter: delimiter for spliting the text message into segments, single quote sign by default
# Return value: 2D array which hold the elements on the required positions in the specific segments.

def pass_in_message_text(message_text, positions, segment_name='LOC', delimiter='+', end_delimiter="'"):
	element_seeked = []
	
	for segment in message_text.split(end_delimiter):
		# To make sure this is only LOC segment, not LOCXXXX etc.
		if segment.strip().startswith(segment_name + '+'):
			elements = segment.split(delimiter)
			elements_list = []
			for n in positions:
				elements_list.append(elements[n-1])
			element_seeked.append(elements_list)
	return element_seeked			

# Testing code.
if __name__=='__main__':
	with open('SampleTextOne', 'r') as f:
		sample_text=f.read().replace('\n', ' ').replace('\r', '')
		logging.basicConfig(level=logging.INFO)	
		retrieve_positions =[2,3]
		logging.info(pass_in_message_text(sample_text, retrieve_positions))

# output: [['17', 'IT044100'], ['18', 'SOL'], ['35', 'SE'], ['36', 'TZ'], ['116', 'SE003033']]

