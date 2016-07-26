#!/usr/bin/env python
from core.base import ScrapBase
from utils._request import HTTPConnection
import codecs
import json
import os

######################################################################
"""
@TODO This needs to be optimized and cleaned up.
"""
#########################################################################
abspath = os.path.abspath( os.path.join(os.pardir) )


def unlabel_brand_names(file_name):

	new_obj = {}
	data = HTTPConnection().getBrandApi()

	brand_names = [ name['brand_name'] for name in data  ]

	new_obj['designer_names'] = brand_names

	new_obj['resource_name'] = file_name

	out = codecs.open(abspath + "/src/buckets/raw_data/" + "raw_data_" + file_name + ".json", 'w','ascii')

	out.write( json.dumps( new_obj ) )



# # This runs and creates the json. 
if __name__ == "__main__":
	ScrapBase().initialization()
	unlabel_brand_names('unlabel')
	
	# scan the directory of json
	json_directory = "{0}/src/buckets/raw_data".format(abspath)
	json_files = [pos_json for pos_json in os.listdir(json_directory) if pos_json.endswith('.json')]

	# load all the objects within a new list
	all_data = []

	# get all the json information within the directory and append the objects to a new list
	for js in json_files:
		with codecs.open(os.path.join(json_directory, js),'r') as json_file:
			all_data.append(json.load(json_file))


	# create an empty dict to house the array of names and count of names
	output_data = {}
	
	# create an empty lists to store all the 
	# data of the names from all objects & resource names
	list_of_all_designer_names = []
	list_of_all_resources_names = []


	# find the keys within the list of objects
	for key in all_data:
		list_of_all_resources_names.append( key['resource_name'] )
		for scrapped_name in key['designer_names']:
			list_of_all_designer_names.append( scrapped_name )


	output_data['list_of_all_resources_names'] = list_of_all_resources_names
	output_data['list_of_all_designer_names'] = list(set(list_of_all_designer_names))	
	output_data['total_count_of_all_designers'] = len( output_data['list_of_all_designer_names'] )
		
	# use set(), to make sure the list is distinct and does not have two of the same names
	# # create new json with all the names
	out = codecs.open(abspath + "/src/buckets/sorted_data/" + "sorted_data" + ".json", 'w','ascii')
	out.write( json.dumps( output_data ) )