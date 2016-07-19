# Unlabel Algorithm v1

### Problem:
So right now our competitors all do something similar to us they try and incorporate and have a resource of emerging designers. Some are more broad in the designers they curate, others are more specific in their curation, but the general notation is their and all seem to be in the same vertical.

However, this creates some fragmentation within the web and in searching for designers or resources to find designers. When searching the web it becomes a tedious and redundant task when after you query for a resource or particular designer you get mixed search results and are surfing the web to find the best resource to explore, while having to try and remember the resource/name or either bookmark the information. 

So the problem can be summed up as their is no one detailed resource that is cohesive enough to find designers, but more specifically emerging and independent designers as they already hard to search and find.


### What we do currently:
So currently our solution is finding and hand selecting designers from specific resources, adding them to an excel sheet and then eventually our database to then show within our API. 

This fine for now but far from an efficient means of continuing this course as we seek to become a powerful tool for users to search and find designers.


### Proposed Solution:
We need to make finding these designers as efficient as possible, limit redundancy (meaning not include names we already have in our database) and increase the amount of data we can share with our users, and make it useful for them to find these emerging and independent designers easier.

Above all break this fragmentation within the market and become the defacto resource of independent/emerging designers around the world. 

The curation part then comes when we add additional information about the designers once we have found them in the first place. 


**Here is the a proposed list of algorithm steps:**

1. Give the algorithm different resources by letting it interacting with a "Resource API" that has a collection of urls. (format --> JSON) **Should the "Resource API" be an exact clone of the Brand API in terms of information fields?**

2. Begin to scrap the sites to analyze and retrieve appropriate data. 

3. The algorithm when analyzing results will check the "Resource API" and if the name don't match, save them to the "Resource Api" if the name already exist do not add the name. **Do we get any other type of information from these resources? Should we relate each name with associated information related to the names in an effort to create tags for each name?**

4. The Algorithm will use the names within our "Resource API" and query the web (a search engine e.g. "Google" or something else???) to find the specific information correlated to the name that is begin queried to match fields within the "Resource API". **Is this possible? If not..Do we still continue to hand curate O(n) designers once we have the names? In terms of the web, we are talking in the thousands if not millions of designers. Is this what must be done?**

5. Once the "Resource API" has had the new information from all the urls at this point it would merge with our current DB adding new information and not adding things that are similar. After the merge the "Resource API" would index the data for next time. In an effort to make the process faster. **Is this even possible?, If so is this efficient**

**After thoughts..**

We will still at the end of the day will have some quality control on what brands are displayed on the app to our user. **The question undoubtedly is we should ask ourselves is How do we automate the process and make it as efficient as possible?** 

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

