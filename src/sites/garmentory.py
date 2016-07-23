#!/usr/bin/env python
from core.base import ScrapBase


class Garmentory( ScrapBase ):
	pass

Garmentory( "http://www.garmentory.com/designers", "Garmentory", [{"_class":"brand"}, 'a'], id=["brands-list"] ).createJson()


