#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.LexiconCreator.designer_lexicon_generator import DesignerLexiconGenerator
from src.LexiconCreator.designer_lexicon_creator import DesignerLexiconCreator
from src.LexiconCreator.designer_lexicon_retrieval import DesignerLexiconRetrival

from src.GoogleScraper import scrape_with_config, GoogleSearchError 

def unlabel_algorithm_main( cmd ):
	
	if cmd == 'lexicon-creator':
		DesignerLexiconGenerator().initialization()
		DesignerLexiconCreator().initialization()
	
	elif cmd == 'search-engine-crawl':
		
		keywords = DesignerLexiconRetrival().getLexicon()
		
		# See in the scrape_config.py file for possible values
		config = {
		    'use_own_ip': True,
		    'keywords': keywords,
		    'search_engines': ['google','bing','yahoo','duckduckgo'],
		    'num_pages_for_keyword': 2,
		    'scrape_method': 'selenium',
	    	'sel_browser': 'chrome',
		    'do_caching': True,
		    'num_workers':20
		}

		try:
		    search = scrape_with_config(config)
		except GoogleSearchError as e:
		    print(e)
	else:
		raise Exception('Wrong argument entered')