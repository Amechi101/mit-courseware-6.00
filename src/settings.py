import os
import datetime

now = datetime.datetime.now()

#Base directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#Current Date 
DATE_INFO = now.strftime("%Y_%m_%d")