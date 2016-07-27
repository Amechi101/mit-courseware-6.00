#!/usr/bin/env python
from abstract_classes import AbstractBase


"""	
Resources to crawl or get information: 

Google
Yahoo
Bing/ BING API
AOL
DuckDuckGo
Instgram API
.
"""


class DesignerCrawler( AbstractBase ):
	"""
	Crawls various resources to get information based on a designers name
	"""

	def __init__( self ):
		super(DesignerCrawler, self).__init__()

	def __str__( self ):
		return 'Designer Crawler: {0}'.format( self )

	def initialization(self):
		pass
	
		
