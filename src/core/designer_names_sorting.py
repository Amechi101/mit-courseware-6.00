#!/usr/bin/env python
from designer_names_scraper import DesignerNamesScraper

from src.settings import BASE_DIR

from src.utils._debugger import debugger
from src.utils._request import HTTPConnection
from src.utils._unlabel_api_names import UnlabelApiNames

import codecs
import simplejson
import datetime
import os

now = datetime.datetime.now()
date_time_info = now.strftime("%Y_%m_%d")

class DesignerNamesSorting( object ):
	def __init__(self):
		super(DesignerNamesSorting, self).__init__()


	def initialization(self):
		self.storeSortedData()
		debugger(True, 'Storing Data...')
	
	def scanJsonFiles(self):

		UnlabelApiNames().createUnlabelApiJson()
		
		# scan the directory of json
		raw_data_directory = "{0}/src/buckets/raw_data".format(BASE_DIR)
		
		raw_data_json_files = [json for json in os.listdir( raw_data_directory ) if json.endswith('.json')]

		# load all the objects from the .json files within a new list
		raw_data = []

		# get all the json information within the directory and append the objects to a new list
		for data in raw_data_json_files:
			with codecs.open(os.path.join(raw_data_directory, data),'r') as json_file:
				raw_data.append(simplejson.load(json_file))

		return raw_data

	def getRawDataFromJson(self):
		raw_data = self.scanJsonFiles()

		return raw_data

	def sortRawData(self):
		raw_data = self.getRawDataFromJson()
	
		# create an empty dict to house the array of names and count of names
		sorted_data = {}

		# create an empty lists to store all the 
		# data of the names from all objects & resource names
		list_of_all_designer_names = []
		
		list_of_all_resources_names = []

		# find the keys within the list of objects
		for key in raw_data:
			list_of_all_resources_names.append( key['resource_name'] )
			for scrapped_name in key['designer_names']:
				list_of_all_designer_names.append( scrapped_name )

		sorted_data['list_of_all_resources_names'] = list_of_all_resources_names
		sorted_data['list_of_all_designer_names'] = list(set(list_of_all_designer_names))	
		sorted_data['total_count_of_all_designers'] = len( sorted_data['list_of_all_designer_names'] )

		return sorted_data

	def storeSortedData(self):

		sorted_data = self.sortRawData()

		sorted_data_directory = "{0}/src/buckets/sorted_data/".format( BASE_DIR )

		sorted_data_filename = "sorted_data_{0}.json".format(date_time_info)
		
		# create new json with all the names filterd and sorted
		out = codecs.open(sorted_data_directory + sorted_data_filename, 'w','ascii')
		out.write( simplejson.dumps( sorted_data  ) )



