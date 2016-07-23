#!/usr/bin/env python
from core.base import ScrapBase

def anthom():
	anthom = ScrapBase("http://www.shopanthom.com/")

	name = anthom.setName("Anthom")

	main_container = anthom.setContainer(id=["queldoreiNav"])

	elements = anthom.setElements(['span'])

	data = anthom.getData()

	return data


if __name__== "__main__":

	print( anthom() )

