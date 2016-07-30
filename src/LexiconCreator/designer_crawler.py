#!/usr/bin/env python
from abstract_classes import AbstractBase


"""	

Variables to keep in mind:
(L=lexicon)
(Q=Query)
(kw=keywords)
(u=URLS)

The crawler needs to do...

1. Find more resources that have a tendency to house multiple emerging designers,for us to scrap the "designer names" to build our (L). 
We will use a few keywords(kw) to (Q) with

1. Grab words from our (L) stored in memory, reading the json file

2. Use our built (L) to find specific information about these designers, by cralwing various resources, mainly in particular search engines. 
We would (Q) then designers from our (L) retrieving multiple (u) from the results by ranking the best results that have the highest occurance 
of the designers name within the documents that the crawlwe retrieved.

Resources: 
	Google
	Yahoo
	Bing/BING API
	AOL
	DuckDuckGo
	( Add more .....)

retrieving (u) from these by ranking the importance based on a particular factor of relavance
the lexeme (Q) used from our (L).

*1 & 2 are independent of each other and can work in parllel to each other at the same time.









We need to create objects and store the data within the objects:
{
	designers_name:"",
	
	# This will be an object the that is suppose to be the (primary site) of the brand, 
	# using regex will try to capture the appropirate url, based on a few assumpations and patterns that brands typical
	# create their (home site) urls by. We then will scrap the site if we get a return, 
	# the (primary site) by scanning for categories at the first level
	# then scanning for products at the second level, getting some information
	
	primary_site:{
		url_retrieved:"",
		site_name:"",       
		products: {
			"product_image": ""
			"product_name": ""
			"product_price": ""
			"product_url": ""

        }
    }, 
	
	# Will be the top 10 results
	secondary_urls:[] 
	
	keywords:[]
	images:


	

	"brand_description": String, 
      "brand_feature_image": String,
      "brand_isActive": Boolean,
      "brand_name": String,
      "brand_city": String,
      "brand_location": String,
      "brand_category": String,
}
"""


class DesignerCrawler( AbstractBase ):
	"""
	Crawls various resources to get information based on a designers name
	"""

	def __init__( self ):
		super(DesignerCrawler, self).__init__()

	def __str__( self ):
		return 'Designer Crawler: {0}'.format( self )

	def initialization(self):
		pass
	
		
