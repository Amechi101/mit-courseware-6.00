#!/usr/bin/env python
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError

import sys, os
import requests
import json
import time


class HTTPConnection( object ):
	"""
	Class for making HTTP request
	"""
	
	def getHttp( self, url ):
		"""
		Method to get HTTP Access to the websites
		"""
		api_key = 'ApiKey unlabel_us_api:f54c309313f3bb0f28322f035cfc169c8631faf9'
		
		headers = {
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		    'Accept-Encoding': 'none',
		    'Accept-Language': 'en-US,en;q=0.8',
		    'Connection': 'keep-alive',
		    'Authorization': api_key
		}
		
		response = requests.get( url, headers=headers )
		
		try:
			
			response_content = response.content
			
			return response_content
		
		except ConnectionError:

			time.sleep(15)

			response_content = response.content

			return response_content

	def getSoup( self, url ):
	
		try:
			soup = BeautifulSoup( str( self.getHttp( url ) ), 'lxml' )
			
			return soup
		
		except ConnectionError:

			time.sleep(1)
			
			soup = BeautifulSoup( str( self.getHttp( url ) ), 'lxml' )
			
			return soup

	def getBrandApi( self ):
		json.loads( self.getHttp('https://unlabel.us/unlabel-network/unlabel-network-api/v1/labels/') )

	
	def getResourceApi( self ):
		getUrls = json.loads( self.getHttp('https://unlabel.us/unlabel-network/unlabel-network-api/v1/resources/') )
	
		resource_list = getUrls['resource_list']
		
		resource_urls = [ resource['resource_url'] for resource in resource_list ]

		return resource_urls




		

		

