#!/usr/bin/env python
from src.LexiconCreator.settings import BASE_DIR

from src.LexiconCreator.utils._request import HTTPConnection
from src.LexiconCreator.utils._debugger import Debugger

import os
import codecs
import simplejson


class UnlabelApiNames( object ):
	def __init__(self):
		super(UnlabelApiNames, self).__init__()

	def getUnlabelApiNames(self):
		brand_names = HTTPConnection().getBrandApi()

		unlabel_api_brand_names = [ name['brand_name'] for name in brand_names  ]

		return unlabel_api_brand_names

	def createUnlabelApiJson(self):

		# object to store unlabel api information
		unlabel_api_obj = {}

		raw_data_directory = "{0}/LexiconCreator/buckets/raw_data/".format( BASE_DIR )
		raw_data_filename = "raw_data_unlabel_api.json"

		Debugger(True, 'Creating Unlabel Json File').logger()

		unlabel_api_brand_names = self.getUnlabelApiNames()

		unlabel_api_obj['designer_names'] = unlabel_api_brand_names 
		unlabel_api_obj['designer_count'] = len( unlabel_api_obj['designer_names'] )
		unlabel_api_obj['resource_name'] = 'unlabel_api'

		out = codecs.open( raw_data_directory + raw_data_filename, 'w' )

		out.write( simplejson.dumps( unlabel_api_obj ) )

	
		



