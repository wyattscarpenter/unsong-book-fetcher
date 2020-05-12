**NOTE: this is an old version. For an updated version, with a bunch of useful changes, you want to be looking at [wyattscarpenter/unsong-book-fetcher](https://github.com/wyattscarpenter/unsong-book-fetcher) instead!**

### Unsong book fetcher

Grabs the text of the book UNSONG by Scott Alexander from [unsongbook.com](http://unsongbook.com) and makes an epub out of it.

Requires Python 3 and PIL. Creates a folder `cache` which caches the downloaded text and images so it can be re-run again later and be a lot quicker. Requires Calibre's `ebook-convert` to actually do the conversion to epub.

Install python requirements with `pip install -r requirements.txt`
Run `bash create_unsong_book.sh`, which will output `Unsong.epub`.
