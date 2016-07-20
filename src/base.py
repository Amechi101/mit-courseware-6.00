#!/usr/bin/env python
import sys, os
import scrapy
import json



# Interact with our "Resource Api" that has a collection of urls. (format --> JSON)
# Begin to scrap the sites
# Search the website for "names" of designers
# Hook our existing "Brand Api" and if the names dont match, save them to the DB if the name already exist do not add the name
# Use the names as a search index point to finding specific information related to the names based on some factors so the algorithm doesn't return junk but close related information to the name that matches what we need. 



