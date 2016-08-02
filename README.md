# Unlabel Scrap & Crawl Program v2.0.0

### Problem:
So right now our competitors all do something similar to us they try incorporating having different and many emerging/independent designers, with seemingly great selection and quality. Some are more broad in the designers they curate, others are more specific in their curation and in many cases resources contain the same designers as other resources with just some slightly different products or how they position themselves in the market to sell to the users they seek. But lets face it we all seem to be in the same vertical nonetheless. 

However, this creates some fragmentation within the web as you search for resources to find new designers, being that the ultimate goal is finding something new. The time and effort it takes is extremely time consuming when getting mixed search results surfing the web trying to find the best available resource to explore or sometimes not even knowing where to start your search in finding new designers or at this point on the frustration ladder anything new. 

So typical the user just defaults to shopping on Zara, Asos, [Enter another mainstream fast fashion brand here..], its just so dam easy...we know...we do the same thing...

This begs the questions:

For Us:
- **What is it that the user exactly wants?** 
- **How can we help the user get exactly what they want?** 
- **How can we help users filter and find something cool, unique [insert more buzz words here...] with limited effort?**

For The User:
- **Where do I even start my search?** 
- **Who has the most organized and plentiful amount of data to extract what I need that is readable accessible?** 
- **Why would I choose this resource to shop and discover new designers over the others?**
- **Which data will I value the most?** 
- **Can I depend on this resource to always show me what I want?**

So the problem can be summed up as their is not one detailed resource that is cohesive enough to easily find emerging and independent designers for the fashion conscious user who may or may not be in the know.


### Current Solution:
So currently our solution is finding and hand selecting designers from various resources, adding them to an excel sheet to filter which ones we like or dont like and then eventually add them to our Brand DB to expose them via a Brand API, to be consumed via (IOS, Web). 

This fine and one of the more beautiful aspects of what we do, but it is far from an efficient means of continuing this course as we seek to become a powerful tool for users to search and find designers.

**So what we need to do:**
Make our backend robust enough to automate a better curation process so that users continuously get the best data possible at a high rate. This will help answer the questions (*For The User*)


### Proposed Enhanced Solution:

Build a word bank(Lexicon) of designers from multiple resources (including our existing `Brand DB`) by hand selecting and adding the resources to our `Resource DB` and/or automating the process of looking for new resources via the web to further analyze so we can to scrap names to build our lexicon of designers to begin extracting and analyzing information about them to automate curation onto our app at a high level, without of course sacrificing quality . 


### The Scrap & Crawl Program

**Current Steps:**

(1) In the terminal enter `python startup.py` in the main directory after you have entered in the argument of the `unlabel_algorithm_main` function either 'lexicon-creator' starting the program (steps 2 - 4) to add to our lexicon by scraping names from various resources that we have added into our resources DB( exposed via our [Resources API](https://unlabel.us/resources-api/v1/resources/) ) and getting a copy of the latest labels we have added into our Brand DB( exposed via our [Brand API](https://unlabel.us/unlabel-network/unlabel-network-api/v1/labels/) ) or 'search-engine-crawl' to begin crawling and getting information via various search engines (Google, Yahoo, Bing, DuckDuckGo) entering names from our current lexicon as the query (see step 5). 

(2) The program after scrapping the site will create a json file with the `raw_data_name_of_the_resource.json` and add it within the `src/LexiconCreator/buckets/raw_data` directory. Within the file a object will be created to dump the data within. The object below: 
```python
{
designer_names:["",""...],
designer_count:Integer,
resource_name:String
}
```
(3) Make a call the [Brand API](https://unlabel.us/unlabel-network/unlabel-network-api/v1/labels/) to create a json file `raw_data_unlabel_api.json` and add it too `src/LexiconCreator/buckets/raw_data` directory

(4) Scan all of `src/LexiconCreator/buckets/raw_data` directory and get all the information from each json file and dump that data inside a new folder `src/LexiconCreator/buckets/sorted_data` creating a new json file `lexicon_year_month_day.json` with the object representation below with all the names, duplicates of names taken out and text formated. 
```python
{
list_of_all_resources_names:["",""...],
list_of_all_designer_names:["",""...],
total_count_of_all_designers:Integer
}
```

(5) We then use the `Search Engine Crawl Program` called [GoogleScraper](https://github.com/NikolaiT/GoogleScraper) originally created by [NikolaiT](https://github.com/NikolaiT), but has been added to out program suite to be modified and do our biding the way we need. This program takes the `list_of_all_designer_names` list within the `src/LexiconCreator/buckets/sorted_data` and programmatically inputs all the names within multiple browser sessions and crawls each search engine we add within the `config.py` collecting links, small excerpts and other data and stores the information in the [Unlabel Search Engine Crawler DB](https://www.adminium.io/dashboard). 

**Extra Notes**

But what is the true difference between us and the other resources. We simlple just like you know the designers names upfront first, sort of like looking up a word in the dictionary but a more colorful one. The goal is to let users filter through categories/keywords and locations seamlessly so they can find new designers and really start to get in the know of some fresh new designers they may not have heard of. 

We still at the end of the day will have quality control on what designers are displayed on the app to our user. We are just lazy and prefer 95% of it to be automated :)

To add or look at resources to scrap check the: [Admin](https://unlabel.us/unlabel-network/admin/applications/crawlresource/)

**Questions**

- How can we improve the Scrap & Crawl Program?

- How can we hook the Unlabel Search Engine Crawler DB into our Brand DB to build a search engine on top of the Brand DB that will maximumly help our users filter our curated designers to get what they want. This will help answer the questions (*For Us*)

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

