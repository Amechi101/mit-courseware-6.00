#!/usr/bin/env python
from utils._request import HTTPConnection

import sys, os
import json
import time
import re


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

	def find(self, element, steps):
		for i, step in enumerate(steps):
			
			try:
				if type(step) is dict:
					element = element.find(**step)
					
				elif type(step) is str:
					index = step.find('[')
					print(index)
					if step.startswith('.'):
						element = eval("element" + step)
					elif (index == -1): #not found
						element = element.find(step)
					else:
						pos = step[index+1:step.find(']')]
						if (pos == 'all'):
							return [self.find(x, steps[i+1:]) for x in element.find_all( step[:index] )]
						pos = int(pos)
						element = element.find_all(step)[pos]

			except Exception, e:

				#print exception type, file name, and line number
				exc_type, exc_obj, exc_tb = sys.exc_info()
				fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
				print(exc_type, fname, exc_tb.tb_lineno)
				print "on step", step, "in", steps
				print "element == None:", element == None
				if element is not None:
					print "element was a", element.name, "with", element.attrs
				
				return None

		return element
		
	#  method to scrap and return data 
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

			# print(item)
			if getattr(self, "name"):
				page_info['resource_name'] = self.name
			if getattr(self, "elements"):
				page_info['designer_names'] = self.find(item, self.elements).get_text()

		return page_info
	
		


anthom = ScrapBase("http://www.shopanthom.com/")
name = anthom.setName("Anthom")
container = anthom.setContainer(id=["queldoreiNav"])
elements = anthom.setElements([ {"class_":"level1"},'a','span'])

data = anthom.getData()

print(name, data)

