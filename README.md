# Unlabel Algorithm v1

### Problem:
So right now our competitors all do something similar to us they try and incorporate and have a resource of emerging designers. Some are more broad in the designers they curate, others are more specific in their curation, but the general notation is their and all seem to be in the same vertical.

However, this creates some fragmentation within the web and in searching for designers or resources to find designers. When searching the web it becomes a tedious and redundant task when after you query for a resource or particular designer you get mixed search results and are surfing the web to find the best resource to explore, while having to try and remember the resource/name or either bookmark the information. 

So the problem can be summed up as their is no one detailed resource that is cohesive enough to find designers, but more specifically emerging and independent designers as they already hard to search and find.


### What we do currently:
So currently our solution is finding and hand selecting designers from specific resources, adding them to an excel sheet and then eventually our database to then show within our API. 

This fine for now but far from an efficient means of continuing this course as we seek to become a powerful tool for users to search and find designers.


### Proposed Enhanced Solution:
We need to make finding these designers as efficient as possible, limit redundancy (meaning not include names we already have in our database) and increase the amount of data we can share with our users, and make it useful for them to find these emerging and independent designers easier.

Above all break this fragmentation within the market and become the defacto resource of independent/emerging designers around the world. 

The curation part then comes when we add additional information about the designers once we have found them in the first place. 


**Here is the a proposed list of algorithm steps:**

```python
#ResourceName( url, name, *args, **kwargs ).createJson()

# url = url of resource to scrap from
# name = name of resource begin scrapped
# *args = list of elements to scrap
# **kwargs = name of css `class` or `id` the *args will be filtered against (choose a **kwargs before looking for *args to filter)


#Example:
from core.base import ScrapBase

class Garmentory( ScrapBase ):
    """
    In case you need to override or add any methods you can just do so within the newly Class,
    as it inherits from the ScrapBase Class
    
    Remove the pass statement 
    	...to add or alter any method below.
    """
	pass
	
Garmentory( "http://www.garmentory.com/designers", "Garmentory", [{"_class":"brand"}, 'a'], id=["brands-list"] ).createJson()
```

1. Create a file `resource_name.py` within the src/sites directory and within the file create a new class the inherits from the `ScrapBase` Class. Name the class with the name of the Resource, call the class and add arguments within the call.

2. To scrap an individual site run `python resource_name.py` in the terminal within the `src/sites` directory. To scrap all sites within the directory run the command `sh sites.sh` in the terminal. Either command will start the program to scrap each site and retrieve the names of designers. 


3. The algorithm after scrapping the site will create a `json file` and add it within the `src/sites/output_data` directory. Within the file an object will be created to dump the data within. The object will have `name (key) ==> list_of_names (value)`, `count (key) ==> total_number_of_designers_scraped (value), resource_name (key) ==> name_of_resource used (value)`. 

4. Scan all of `output_data` folder and get all the information from the `resource_names.json` files and create a new `object` with a `list_of_all_resources_names `, `list_of_all_designer_names` and a `total_count_of_all_designers` within the `list_of_all_designer_names`. When getting `list_of_all_designer_names` run check to see if the names are duplicate before adding to `list_of_all_designer_names` If the name does exist it will not add to the list, if the name does not exist it will add the new name to the list. Create a new `all_designers.json` file.

5. Call the `[Brand API](https://github.com/Amechi101/unlabelapp)` to compare the names in the `all_designers.json` file to check what names are already exist within our API. If the name doesn't exist add the name into a temporary list. After the check is complete. Dumb the list into the DB to create a new records of `brand_names`. 

6. **Note: This part is still hypothetical and needs to be discussed** The we will then add a `Crawl Program` in addition to our Scrap Program and then call our `Brand API` to use the `brand_names` key and crawl the  web to find the relevant information correlated to the `brand_name` and begin to store that information in a separate DB/Server. It will either crawl (a search engine like e.g. Google,Yahoo or something else???) to query their search boxes with our `brand_names` or something else?? This is the data mining aspect, where we can later use the information to study trends and gather new information on our labels, or even been to automate some of the or curation with the stored information.

**After thoughts & Notes..**

We will still at the end of the day will have quality control on what brands are displayed on the app to our user. 

To look or add resources to scrap from look on the `Admin`: `https://unlabel.us/unlabel-network/admin/applications/crawlresource/` or `Resource API`: `https://unlabel.us/unlabel-network/unlabel-network-api/v1/resources/`


### Programming Language 
+ Python

### Tools:
+ http://scrapy.org/
+ https://www.crummy.com/software/BeautifulSoup/bs4/doc/

### Resources For Information Helpful To Read Up On:
+ https://en.wikipedia.org/wiki/Data_mining
+ http://res.cloudinary.com/hqz2myoz0/raw/upload/v1468526035/Algorithms_3rd_b6qtz2.pdf
+ https://en.wikipedia.org/wiki/Web_search_engine
+ https://en.wikipedia.org/wiki/Vector_space_model
+ http://res.cloudinary.com/hqz2myoz0/raw/upload/v1468526775/googleFinalVersionFixed_kvzp9s.pdf
+ http://stackoverflow.com/questions/1085425/how-is-linear-algebra-used-in-algorithms
+ https://www.quora.com/How-to-build-a-search-engine-from-scratch

