#!/usr/bin/env python
from src.utils._request import HTTPConnection

from src.settings import BASE_DIR

from src.utils._debugger import debugger

import os
import codecs
import json
import time
import simplejson

class DesignerNamesScraper( object ):
	"""
	Program to scrap designer names from websites
	"""

	def __init__( self ):
		super(DesignerNamesScraper, self).__init__()

	def __str__( self ):
		return 'DesignerNamesScraper: {0}'.format( self )

	def initialization(self):
		"""
		Starts the scraper program
		"""

		# gets resources information from api about site
		data = HTTPConnection().getResourceApi()
	
		for i, key in enumerate(data):
			
			if key is not None:
				self.setUrl( key['resource_url'] )
				
				self.setName( key['resource_name'] )
				
				self.cssClassOrId( key['resource_parent_isCssOrId'] )
				
				self.setParent( key["resource_parent_name"] )
				
				self.setChildren( key["resource_children_tag"] )
				
				self.createJsonFiles()

				debugger(True, 'Scrapping resource {0}'.format(self.name))

	def setUrl( self, url ):
		if url is not None:
			self.url = url
			return HTTPConnection().getSoup( self.url )
		raise AttributeError( 'Url not added. Please add url' )
	
	def setName(self, name):
		if name is not None:
			self.name = name.lower()
			return self.name
		raise AttributeError( 'Resource name not added. Please add name!' )

	def cssClassOrId(self, boolean):
		if boolean is not None:
			self.boolean = boolean
			return self.boolean
		raise AttributeError( 'Not a boolean type.' )
	
	def setParent(self, parent):
		if parent is not None:
			self.parent = parent
			return self.parent
		raise AttributeError( 'Parent tag not added. Please add parent tag!' )

	def setChildren(self, children):
		if children is not None:
			self.children = children
			return self.children
		raise AttributeError( 'Children of parent tag not added. Please add vaild html tag!' )

	def getPages(self):
		# @TODO function to help If page has more than one page of designers
		# and needs to loop through
		pass
		
	def scrapData( self ):
		"""
		Algorithm to scrap names from the site
		"""
		if getattr(self, "url"):
			data = self.setUrl( self.url ) 

		# object to store information
		page_info = {}

		parent = None
		
		child = None
		
		scrapped_names = None

		unlabel_brand_names = None

		if getattr(self, "name"):	
			page_info['resource_name'] = self.name

		if getattr(self, "parent"): 
			
			if getattr(self, "boolean"):
				parent = data.find_all( id=[ "{0}".format( self.parent ) ] )  # finds all the divs that contain products
			else:
				parent = data.find_all( class_=[ "{0}".format( self.parent ) ] )  # finds all the divs that contain products
		
		else:
			parent = data.find_all('div') # if the parent isn't defined, just find all the divs

		parent = [x for x in parent if x is not None] # makes sure we don't have any Nones in our array

		parent = parent[0:1] # for testing, we only want one div

		for children in parent:
			
			if getattr(self, "children"):
	
				child = children.find_all( [ self.children ] )
		
				if not child:
					raise Exception('List is Empty. Please make sure you have added correct child tag.')
				else:
					
					scrapped_names = [ text.get_text(strip=True).encode('ascii', 'ignore') for text in child if text.get_text() ]
					
					if not scrapped_names:
						raise Exception('List is Empty. Please make sure you have added correct child tag.')
					else:
						
						scrapped_names = list( set( scrapped_names ) )

						page_info['designer_names'] = scrapped_names
			
						page_info['designer_count'] = len( page_info['designer_names'] )

		return page_info

	def createJsonFiles(self):
		"""
			Creates json files within the raw_data directory
			These are buckets filled with designer names scrapped
			from our resources
		"""
		data = self.scrapData()
		
		try:
			# @TODO create a helper to check if the data is healthy before procceding to scrap
			raw_data_directory = "{0}/src/buckets/raw_data/".format( BASE_DIR )

			raw_data_filenames = "raw_data_{0}.json".format( self.name )
			
			create_filenames = codecs.open(raw_data_directory + raw_data_filenames, 'w','ascii')

			create_filenames.write( simplejson.dumps( data ) )
		except Exception, e:
			raise e


		
