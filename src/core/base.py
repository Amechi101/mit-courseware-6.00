#!/usr/bin/env python
from utils._request import HTTPConnection

import codecs
import json
import time
import os

path = os.path.abspath( os.path.join(os.pardir) )

class ScrapBase( object ):

	def __init__( self ):
		super(ScrapBase, self).__init__()

	def __str__( self ):
		return 'ScrapBase: {0}'.format( self )

	def initialization(self):
		data = HTTPConnection().getResourceApi()
	
		for i, key in enumerate(data):
			
			if key is not None:
				self.setUrl( key['resource_url'] )
				
				self.setName( key['resource_name'] )
				
				self.cssClassOrId( key['resource_parent_isCssOrId'] )
				
				self.setParent( key["resource_parent_name"] )
				
				self.setChildren( key["resource_children_tag"] )
				
				self.createJson()

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

	# If page has more than one page of designers
	def getPages(self):
		pass
		
	def scrapData( self ):
		
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

	def createJson(self):
		data = self.scrapData()
		
		try:
			out = codecs.open(path + "/src/buckets/raw_data/" + "raw_data_" + self.name + ".json", 'w','ascii')

			out.write( json.dumps( data ) )
		except Exception, e:
			raise e


		
