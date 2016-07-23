#!/usr/bin/env python
from core.base import ScrapBase


class Anthom( ScrapBase ):
	pass

Anthom( "http://www.shopanthom.com/", "Anthom", ['span'], id=["queldoreiNav"] ).createJson()

