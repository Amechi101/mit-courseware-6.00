#!/usr/bin/env python
from core.base import ScrapBase


class SwordsSmith( ScrapBase ):
	pass

SwordsSmith( "http://swords-smith.com/pages/designers", "Swords & Smith", [{"class_":"column-container"},'a'], id=["page-text"] ).createJson()

