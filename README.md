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

1. Give the `Crawling Program` the `Resource API` to request the resources. The call of resources will be returned in json format.

2. Start to crawl each site and retrieve the names of designers. 

3. The algorithm after scrapping each site will create a `json file`. Within the file a object will be created to dump the data within. The object will have `name (key) ==> list_of_names (value)`, `count (key) ==> total_number_of_designers_scraped (value)`. 

4. If the json file already exist, it will check to see if the names begin scrapped already exist within the `list_of_names`. If the name exist it will not add it to the list, if the name does not exist it adds the new name to the list. If a file does not exist already, skip step 4.

5. Call the `Brand API` to compare the names to the `json file` to check what names are already existing within our API. If the name doesn't exist add the name into a temporary list. After the check is complete. Dumb the list into the DB to create a new records of `brand_names`. 

#### This part is still hypothetical

6. The `Crawl Program` will then call our `Brand API` to use the `brand_names` and crawl the  web to find the relevant information correlated to the `brand_name` and begin to store that information in a separate DB/Server. It will either crawl (a search engine like e.g. Google,Yahoo or something else???) to query their search boxes with our `brand_names` or something else?? This data mining aspect, where we can later use the information to study trends and gather new information on our labels

**After thoughts..**

We will still at the end of the day will have quality control on what brands are displayed on the app to our user. 

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

