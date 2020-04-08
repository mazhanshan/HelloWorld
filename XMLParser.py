#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 08 Apr 2020
# Solution for question 2. This module parses the provided XML file, looks for the specific node and returns the values in the node
import logging
import xml.etree.ElementTree as ET


# This function receives the message to be processed, it looks for the nodes by tag name, then checks if its attributes value to see
# if it is the requested one. If it is, it retrieves the child node's value.
# Parameter: file_name: XML file to parse
# Parameter: target_node_name: the target node's tag name
# Parameter: target_node_attri_name: name of the attributes to check in the target node
# Parameter: attrib_match_list: a list of values, which the target nodes should have.
# Parameter: target_node_child_node_text: tag name of the child node of the target node.
# Return value: 2D array which hold the attribute value and the child node value of the target nodes.
def parse_xml(file_name, target_node_name, target_node_attri_name, attrib_match_list, target_node_child_node_text):
	target_node_attri_and_value_list = []
	try:
		tree = ET.parse(file_name)
		root = tree.getroot()
	except ET.ParseError as e:
		logging.exception('There is an error during pasring the file '+ file_name)
		return;

	for target_node in root.iter(target_node_name):
		if target_node_attri_name in target_node.attrib:
			if target_node.get(target_node_attri_name) in attrib_match_list:
				attribute_value=target_node.attrib.get(target_node_attri_name)
				child_node_value =target_node.find(target_node_child_node_text).text
				target_node_attri_and_value_list.append([attribute_value, child_node_value])
	return target_node_attri_and_value_list;
		

# Testing code.
if __name__=='__main__':
	logging.basicConfig(level=logging.INFO)
	attris_and_vals=parse_xml('SampleXML.xml', 'Reference', 'RefCode', ['MWB', 'TRV', 'CAR'], 'RefText')
	if attris_and_vals is None: 
		logging.info ("No result")
	else:
		for l in attris_and_vals:
			logging.info(l[0]+ ':::::'+ l[1])

# output: 
# MWB:::::586133622
# CAR:::::71Q0019681
# TRV:::::1
