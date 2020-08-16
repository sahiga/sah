.. link: 
.. description: 
.. tags: hip-hop + rap, python, text mining
.. date: 2013/05/18 18:32:32
.. title: Analyzing Rap Lyrics with Python
.. slug: analyzing-rap-lyrics-with-python

On Friday, my company held a personal project hack day. I used the opportunity to run a quick-and-dirty experiment based on a question I've had on my mind for months: **What's the most beloved car brand in hip-hop?**

In this post, I'll explain how I came up with a possible answer to that question. `To skip to the results, click here <https://www.stephaniehiga.com/cars.html>`_.

Why hip-hop / why cars
======================

Hip-hop is my favorite genre of music. On the road, I tune the radio to `93.5 KDAY <http://www.935kday.com/>`_; otherwise, I'm plugged into my Pandora account, which is heavy on Golden Age, Midwestern, East Coast, Bay Area, and (recently) indie rap. Rap is also lyrically dense, which makes it a great source for text mining.

I got curious about cars because rappers talk about them--a lot. So I decided to find out once and for all which brand they love the most, with **Chevy** (the brand I kept hearing) as my hypothesis.

The lyrics mining process
=========================

To find the answer, I needed a sizeable sample of car brand names, a searchable database of hip-hop lyrics, a script to search for the brands within the lyrics database, and a way of displaying the results. Fortunately, all the necessary tools were readily available:

- Python
- Wikipedia
- LibreOffice Calc
- `Rap Lyrics Database <http://research.blackyouthproject.com/raplyrics/>`_
- `Google Charts <https://developers.google.com/chart/>`_
- Bootstrap

Gathering the data
------------------

Wikipedia blocks web scrapers, understandably. So I manually downloaded all of Wikipedia's lists of car manufacturers and brands by country. To reduce the amount of HTML I would have to parse, I selected the `Mobile View <http://en.m.wikipedia.org/wiki/Main_Page>`_ for each page.

I downloaded ten files in total: a general list of car manufacturers plus individual lists for China, France, Germany, Italy, Japan, Spain, Sweden, the United Kingdom, and the United States.

Cleaning the data
-----------------

Wikipedia's Mobile View pages contain search bars at the top and the usual "See also," "References," and "Read in another language" links. I started by erasing these (manually again), reducing the files to structural markup and the lists themselves.

With the Python `Beautiful Soup <http://www.crummy.com/software/BeautifulSoup/>`_ library, I extracted the brand name tags by selecting all list elements. Then I used `NLTK <http://www.nltk.org>`_ to remove the HTML tags and regular expressions to remove excess whitespace and text (such as notes about the brand, the brand's years of operation, etc.). This is what I came up with::

	def clean_wikilist(filename):
	    # open saved html file
	    html = open(filename).read()
    
	    # collect bulleted items only
	    bullets = SoupStrainer("li")

	    # make soup out of the bulleted items
	    soup = BeautifulSoup(html, 'lxml', parse_only = bullets).prettify()

	    # remove html from soup
	    raw = nltk.clean_html(soup)

	    # remove extra lines
	    raw = re.sub(r'\n \n \n \n \n', r'\n', raw)
	    raw = re.sub(r'\n \n \n', r'\n', raw)

	    # create and clean tokens
	    tokens = raw.split('\n')
	    tokens = [re.sub(r'^\s+(?=[\S]+)', r'', token) for token in tokens]
	    tokens = [token for token in tokens if not re.findall(r'\[[0-9]+\]|\([\S\s]+[\(\)]?|^\s+$|^[\s\[\]\(\)0-9]+$', token)]
	    tokens = list(set(tokens))

	    return tokens

After running my script on all ten lists, I had a whopping **2599 brand names**. So I decided to limit the set to Germany, Japan, the UK, and the US. The pages for Germany, the UK, and the US separate current brands from defunct brands, so for those countries I used current brands only. The Japan page mixes current and defunct brands into one list; to save time, I used all of them.

These four pages have slightly different structures. The ``clean_wikilist()`` script worked nicely for Japan, but captured too much information on the others, so I wrote three additional scripts. Here's the one for Germany::

	def autos_ge():
		# open saved html file
		html = open('autos-ge.html').read()

		# create soup object
		soup = BeautifulSoup(html)

		# select current major manufacturers
		majors = soup.select('span.mw-headline')
		majors = [w for w in majors if w.parent.parent.previous_sibling.contents[0]['id'] == 'Current_major_manufacturers']
		major_tokens = [nltk.clean_html(str(w)) for w in majors]
		major_tokens = [re.sub(r'\[\s\S\s\]', r'', token) for token in major_tokens]

	   	# select current minor manufacturers
    		minors = soup.select('li')
    		minors = [w for w in minors if w.parent.parent.previous_sibling.contents[0]['id'] == 'Current_minor_manufacturers']
  		minor_tokens = [nltk.clean_html(str(w)) for w in minors]
  		minor_tokens = [re.sub(r'\s\(\S+\)', r'', token) for token in minor_tokens]

  		# combine lists
  		tokens = list(set(minor_tokens + major_tokens))

   		return tokens  

One notable difference between this and the original script is the usage of Beautiful Soup. In ``clean_wikilist()``, the desired elements are selected first, with SoupStrainer, and then used to create a list of the matching HTML tags in unicode format. ``autos_ge()``, on the other hand, creates a Beautiful Soup object out of the entire page; the desired elements are selected via DOM traversal.

The number of brand names from this limited dataset? Just 178.

Analyzing the data
------------------

The Rap Lyrics Database contains lyrics for all of Billboard Music's rap songs from 1989 through 2009. It's the only searchable database of hip-hop lyrics (exclusively).

The result pages share the same URL, with the search term appended to the end: *http://research.blackyouthproject.com/raplyrics/results/?all/1989-2009/*. This made it much easier to automate the search and saving process.

::

	def rap_search(auto_list):
	    # search for each brand name
	    for brand in auto_list:
	        url = 'http://research.blackyouthproject.com/raplyrics/results/?all/1989-2009/' + word

        	# save the search results page
	        results_html = urllib2.urlopen(url).read()

        	# save it as a file named after the brand
	        results = word + '.html'

        	with open(results, 'w') as results_file:
	            results_file.write(results_html)

This saved 178 HTML pages, each named after the appropriate brand search term, onto my computer. I also searched for known nicknames of the brands (e.g., "Bimmer/Beemer/Beamer" for BMW and "Chevy" for Chevrolet).

I used Beautiful Soup again to count the number of results on each page::

	def count_rap_results():
		# for all html files in current directory
  		for filename in os.listdir('.'):
	        if filename.endswith('html'):

        	# select song titles
           	html = open(filename).read()
		soup = BeautifulSoup(html)
	        songs = soup.select('.title')

        	# count number of song titles
	        count = len(songs)
        
        	# write brand names and number of songs into a text file
           	with open('count_rap_autos.txt', 'a') as counter_file:
                	counter_file.write('%s%15d\n' % (filename[:-5], count))

This got me a pretty messy-looking text file of each brand and the number of songs in which it was mentioned:

	Lea-Francis |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| 1

	Ewing |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| 0

	Efini |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| 0

	Scion |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| 0

	Tommy Kaira |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| 15

	...

It turned out that the Rap Lyrics Database doesn't recognize spaces. So, a search for "Art and Tech" became a search for "Art"--which of course is a popular word that is often used in a non-automobile context. I removed ambiguous names from the list and combined the results from brands and their nicknames. LibreOffice Calc was helpful in fixing the columns and sorting the results.

The final number of usable brands came out to 153.

Who won?
========

**Mercedes-Benz**, with **93 song mentions**--and remember, that's only counting a small segment of rap songs between 1989-2009.

Jeep came in second, at 34 songs. Then came Cadillac with 25 songs, and finally Chevy at 24.

So, Chevy isn't as popular as I expected. But the biggest shocker is Jeep. I can't recall a single song that mentions Jeep.

To display the results, I made a `graph <http://stephaniehiga.com/cars.html#results>`_ with Google Charts. (I'd add them here, but I've yet to learn how to embed JavaScript into reStructuredText.)

Pain points
===========

I'm new to programming. While I enjoy it very much, I spend about 90% of my time immersed in pain. The text analysis took me four nights (Monday through Thursday) to complete. On the actual hack day, I made the graph and web page, with a lot of help from Bootstrap. Along the way, I encountered many problems:

- Selecting specific subsets of HTML tags with no classes or ids.
- Accidentally passing list items with the newline character to the ``rap_search()`` script, resulting in 178 filenames split off from their extensions. Fortunately there was an easy fix::

	for filename in os.listdir("."):
		if '\n' in filename:
		os.rename(filename, re.sub(r'\n', r'', filename))

- Reformatting the final list of brands into an HTML table.
- Reformatting the final list of brands into a list of dictionaries to create a graph with `JavaScript InfoVis Toolkit <http://philogb.github.io/jit/>`_.
- Not knowing how to build a non-stacked bar graph with the InfoVis Toolkit.
- Switching to Google Charts and reformatting the final list of brands into a list of lists to create a Google Charts graph.

Notes for the future
====================

More complete data
------------------

I slashed the set of brand names to less than 7% of its original size and conflated "car manufacturers" with "car brands." Wikipedia also has a lengthy `list of automobile marques <https://en.wikipedia.org/wiki/List_of_automobile_marques>`_, which I didn't even touch.

I'd like to go deeper than brands, into the actual names of cars, and match them against an even bigger database of lyrics. `RapGenius <http://www.rapgenius.com>`_ and the `Last.fm API <http://www.last.fm/api>`_ are possible alternatives to the Rap Lyrics Database. RapGenius has an excellent database, but it contains a significant amount of lyrics from non-hip-hop artists as well.

Semantic orientation
--------------------

I equated "beloved" to "number of songs mentions." This is obviously not always the case, as rappers name-drop plenty of things they dislike. It's true that rappers generally mention cars in a positive manner, but a more accurate experiment would take into account not just how many times the brand was used, but in what way the brand was used--i.e., the semantic orientation of the brand. A `sentiment analysis <https://en.wikipedia.org/wiki/Sentiment_analysis>`_ might be the way to go.

Multi-word brands
-----------------

The Rap Lyrics Database turns up blank if you search for, say "Aston Martin" (with the quotes and the space), even though Aston Martin is mentioned in a few songs. So multi-word brands with spaces in them turned up short. (Mercedes-Benz doesn't have this issue because it has a hyphen, not a space.)

If I were to use the Rap Lyrics Database again, I'd have to search for "Aston" and "Martin" separately and compare the songs on each results page. Otherwise, RapGenius seems to do spaces nicely.

Nicknames and duplicates
------------------------

I searched for "Mercedes-Benz" as well as just "Mercedes" and "Benz." However, again, because I didn't compare song names, I ended up nixing the counts for the nicknames to minimize the possibility of duplicates. I also missed some nicknames--for instance, I completely neglected "Caddy" and "Lac" (sorry, Cadillac), "Lex," etc.

Misspellings, plurals, etc.
---------------------------

I did search for "Beamer" and "Beemer," but there's also "Bima" and probably countless other misspellings of "Bimmer" and other car brands. I ignored plurals, whether spelled correctly ("Bimmers") or not ("Bimaz").

Disambiguation
--------------

Many car brands double as common words or unrelated proper names, e.g., Prince, Radical, Ram, MINI, Oakland. I discarded these instead of determining whether or not they were referring to the car brand.

Last thoughts
-------------

A few months ago, when I first got the idea for this project, I thought it would be ridiculously hard. I envisioned building a large corpus of hip-hop lyrics and determining the classification, meaning, and orientation of each word to uncover the truth.

After going about this somewhat backwards, I think my initial impression remains correct. I'm happy I finally took a stab at the project, and I'm excited to continue working on it. This is just the first of a long series of experiments (and blog posts)!

`Source files on GitHub <https://github.com/sahiga/rap-analysis>`_

.. |nbsp| unicode:: U+00A0
	:trim:
