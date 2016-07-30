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
		    'use_own_ip': 'True',
		    'keywords': keywords,
		    'search_engines': ['google','yandex', 'bing', 'yahoo', 'baidu', 'duckduckgo'],
		    'num_pages_for_keyword': 3,
		    'scrape_method': 'selenium',
	    	'sel_browser': 'chrome',
		    'do_caching': True,
		    'num_workers':10,
		    'output_filename': 'designer_info.json',
		}

		try:
		    search = scrape_with_config(config)
		except GoogleSearchError as e:
		    print(e)

		for serp in search.serps:
		    print(serp)
		    for link in serp.links:
		        print(link)
	else:
		raise Exception('Wrong argument entered')