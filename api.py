#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 08 Apr 2020
# Solution for question 3. This module create a REST API serving as webservice using flask
# It receives the XML data and parses the data.
# Status code is returned to indicate the status of the XML data.
import flask
import xmltodict
from flask import request, jsonify
import xml
import logging

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Set the index page to check the host running properly
@app.route('/', methods=['GET'])
def home():
    return '''<h1>XML Parser</h1>
<p>Post to /processxml to get the xml parsed.</p>'''

# The post method to processxml is routed to the process_xml function, which parses the request xml data
# use xmltodict class to parse the xml data, and then convert the data into dict type. Then look through
# the dict for the required nodes and check the attributes and values.

# The function returns 0 if it's correct structured xml (by default returns X if it's incorrect); 
#-1 if declaration's command attribute value isn't DEFAULT
# -2 if SiteID in DeclarationHeader is not DUB and Declaration's Command is DEFAULT.
@app.route('/processxml', methods=['POST'])
def process_xml():

	status_code = 'X'
	try: 
		doc = xmltodict.parse(request.data)
	except xml.parsers.expat.ExpatError as e:
		print('XML Parsing Error')
		logging.exception(e)
	else:
		logging.info('XML structure correct')
		status_code = '0'

		if doc['InputDocument']['DeclarationList']['Declaration']['@Command'] !='DEFAULT':
			logging.info('Command is not DEFAULT')
			status_code = -1
		elif doc['InputDocument']['DeclarationList']['Declaration']['DeclarationHeader']['SiteID'] != 'DUB':
			logging.info('SiteId is not DUB')
			status_code = -2		


	# return in json so that it's eaiser to expand later.
	# return status_code
	result_dict = {'status_code' : status_code}
	return jsonify(result_dict)
	

# Testing code
if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	logging.info('Service started')
	app.run()


# TestOutput:
# Service started
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# * Restarting with stat
# Service started
# * Debugger is active!
# * Debugger PIN: 680-896-800
###########################################
# Scenario 1) Well structured xml, SiteID is DUB and Command is DEFAULT
# XML structure correct
###########################################
# Scenario 2) XML Parsing Error: xml.parsers.expat.ExpatError: mismatched tag: line 14, column 3
###########################################
# Seenario 3) Well structured xml, Command is not DEFAULT
# Command is not DEFAULT
##########################################
# Seenario 4) Well structured xml, Command is DEFAULT, SITEID is not DUB
# SiteId is not DUB
##########################################