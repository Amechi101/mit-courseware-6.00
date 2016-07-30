# -*- coding: utf-8 -*-

"""
I switched my motto; instead of saying "fuck tomorrow"
That buck that bought a bottle could've struck the lotto.
"""

__author__ = 'Nikolai Tschacher'
__updated__ = '30.11.2015'  # day.month.year
__home__ = 'incolumitas.com'

from src.GoogleScraper.proxies import Proxy
from src.GoogleScraper.config import get_config
import logging

"""
All objects imported here are exposed as the public API of GoogleScraper
"""

from src.GoogleScraper.core import scrape_with_config
from src.GoogleScraper.scraping import GoogleSearchError, MaliciousRequestDetected

logging.getLogger(__name__)
