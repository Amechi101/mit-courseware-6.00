#!/usr/bin/env python
from __future__ import print_function # For python 2.x

from src.core.designer_names_scraper import DesignerNamesScraper
from src.core.designer_names_sorting import DesignerNamesSorting

if __name__ == "__main__":

	DesignerNamesScraper().initialization()
	DesignerNamesSorting().initialization()
		
		
