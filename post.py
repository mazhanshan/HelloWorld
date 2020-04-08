#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 08 Apr 2020
# Solution for question 3. This module consumes the API on the server.
# It open the sample xml file and pass the xml data by post for parsing and retrieve the returned status code.
import requests
import json
import logging

# The function opens the local xml file, read the content and post the data to server side API for parsing
# Parameter: xml_location: the xml file to be parsed.
# Parameter: host: the server host addss
# Parameter: porter: porter of the webservice listening to 
# Parameter: directory: the directory of the webservice which is routed to the function to parse the xml data
# Return value: the status code; or the failure message of calling the webservice function
def do_request(xml_location, host, porter, directory):

    xml_file = xml_location
    headers = {'Content-Type':'text/xml; charset=\"UTF-8\"' }

    # Open the XML file.
    try :
        with open(xml_file) as xml:
            # Give the object representing the XML file to requests.post.
            url='http://'+host+':'+porter+directory
            resp = requests.post(url, headers=headers, data=xml)
    except EnvironmentError: 
        logging.exception('There is an error when read the fil: '+xml_location)
    
    logging.info(resp.content)
    if resp.status_code == 200:
        logging.info("Success called the webservice")
        data = json.loads(resp.text)
        status_code = data['status_code']
        return status_code
    else:
        Return ("Failure in processing the xml file") 

# Testing code.
if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    HOST = "127.0.0.1"
    PORTER ='5000'
    API_URL = "/processxml"
    status_code = do_request("SampleXML2.xml", HOST, PORTER, API_URL)
    logging.info(status_code)

# test output   
###########################################
# Scenario 1) Well structured xml, SiteID is DUB and Command is DEFAULT
# 0 
###########################################
# Scenario 2) XML Parsing Error: 
# X
###########################################
# Seenario 3) Well structured xml, Command is not DEFAULT
# -1
##########################################
# Seenario 4) Well structured xml, Command is DEFAULT, SITEID is not DUB
# -2
##########################################