#!/usr/bin/env python
from core.base import ScrapBase
import json

def anthom():
	anthom = ScrapBase("http://www.shopanthom.com/")

	name = anthom.setName("Anthom")

	main_container = anthom.setContainer(id=["queldoreiNav"])

	elements = anthom.setElements(['span'])

	data = anthom.getData()

	out = open("sites/output_data/" + name + ".json", 'w')

	out.write( json.dumps( data ) )



if __name__== "__main__":
	anthom() 

