#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class AbstractBase( object ):
	"""
	Abstract class for program. 
	"""
	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__( self ):
		pass

	@abstractmethod
	def __str__( self ):
		pass
	
	@abstractmethod
	def initialization(self):
		pass
