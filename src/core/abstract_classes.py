#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class AbstractScraperBase( object ):
	"""
	Abstract class for scraper. 
	"""
	__metaclass__ = ABCMeta

	@abstractmethod
	def __str__( self ):
		pass
	
	@abstractmethod
	def initialization(self):
		pass

	@abstractmethod
	def createJson(self):
		pass


class AbstractScraper( AbstractScraperBase ):
	"""
	Abstract class for scraper. 
	"""
	__metaclass__ = ABCMeta

	@abstractmethod
	def __str__( self ):
		pass
	
	@abstractmethod
	def scrapData(self):
		pass




