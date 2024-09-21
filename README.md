# Unsong Book Fetcher

Grabs the text of the book *Unsong* by Scott Alexander from [unsongbook.com](http://unsongbook.com) and makes an epub out of it.

Requires Python 3 and PIL. Uses a folder `cache` which caches the downloaded text and images so it can be re-run again later and be a lot quicker. Requires Calibre's `ebook-convert` to actually do the conversion to epub.

All you have to do is run `create_unsong_book.bat`.
This script has been cleverly engineered to be both a valid Windows batch file and POSIX shell file.
This script will install python requirements with `pip install -r requirements.txt`,
fetch the text and create an HTML ebook with `get_unsong.py`, which will output `Unsong.html`,
and convert the HTML to an epub with `ebook-convert`, which will output `Unsong.epub`.

TODO: (among other things) discuss the lineage of this project (steal from my releases page summaries?), discuss how this is Version 1 as opposed to Amazon's Version 2 (sub-version-1 changes can be found tracked in https://github.com/florolf/unsong-scrape), also give a shout out to unsong-scraper which is a lot like this project but in ruby. Uhhh make a cover image in yellow and a title page in white. Possibly add this readme as a foreword?
