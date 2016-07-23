#!/usr/bin/env python
from utils._request import HTTPConnection

import sys, os
import json
import time

class ScrapBase( object ):

	def __init__( self, mainUrl ):
		super(ScrapBase, self).__init__()
		self.mainUrl = mainUrl

	def __str__( self ):
		return 'ScrapBase: {0}'.format( self.mainUrl )
	
	def setName(self, name):
		if name:
			self.name = name
			return self.name
		raise AttributeError( 'Resource name not added. Please add name!' )
	
	def setContainer(self, **container):
		if container is not None:
			self.container = container
			return self.container
		raise AttributeError( 'Container not added. Please add container!' )

	def setElements(self, elements):
		self.elements = elements
		
	def getData( self ):

		data = HTTPConnection().getSoup( self.mainUrl )

		html_container = None

		if self.container:
			html_container = data.find_all( **self.container )  # finds all the divs that contain products
		else:
			html_container = data.find_all('div') # if the container isn't defined, just find all the divs

		html_container = [x for x in html_container if x is not None] # makes sure we don't have any Nones in our array

		html_container = html_container[0:1] # for testing, we only want one div

		page_info = {}
		
		for item in html_container:

			if getattr(self, "name"):
				page_info['resource_name'] = self.name
			
			if getattr(self, "elements"):
				
				elements = item.find_all(self.elements)

				designer_names = [text.get_text().encode('ascii') for text in elements]

				page_info['designer_names'] = designer_names

				page_info['designer_count'] = len(page_info['designer_names'])

				
		return page_info

