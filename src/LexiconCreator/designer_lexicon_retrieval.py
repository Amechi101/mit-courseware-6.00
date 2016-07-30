#!/usr/bin/env python
from src.LexiconCreator.abstract_classes import AbstractBase

from src.LexiconCreator.settings import BASE_DIR, DATE_INFO

from src.LexiconCreator.utils._debugger import Debugger

import codecs
import simplejson
import datetime
import os


class DesignerLexiconRetrival( AbstractBase ):
	"""docstring for LexiconGetter"""
	def __init__(self):
		super(DesignerLexiconRetrival, self).__init__()

	def __str__( self ):
		return 'Designer Lexicon Retrieval: {0}'.format( self )

	def initialization(self):
		Debugger(True, 'Getting Lexicon...').logger()
		self.getLexicon()
		

	def getLexicon(self):
		lexicon_directory = "{0}/LexiconCreator/buckets/sorted_data/".format( BASE_DIR )

		lexicon_json_file = [json for json in os.listdir( lexicon_directory ) if json.endswith('{0}.json'.format(DATE_INFO))]

		lexicon = []

		# get all the json information within the directory and append the objects to a new list
		for data in lexicon_json_file:
			with codecs.open(os.path.join(lexicon_directory, data),'r') as json_file:
				designer_names = simplejson.load(json_file)['list_of_all_designer_names']
				
				for name in designer_names:
					lexicon.append(name)

		return lexicon








