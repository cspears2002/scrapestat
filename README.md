# Purpose:

Creating this script to scrape stats from this URL: 
http://www.westcoastroasting.com/.

# Dependencies:

Requires Scrapy (http://scrapy.org/)

Developed using my scrapestat virtual environment.

# Instructions:

1) Enter the scrapestat environment:
$> workon scrapestat

2) Go to $HOME/PyDevel/scrapestat/westcoastroasters and run the
spider:
$> scrapy crawl wcr

3) If you want to export to json:
$> scrapy crawl wcr -o top_selling_beans.json -t json