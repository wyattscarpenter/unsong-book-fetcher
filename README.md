# Unsong book fetcher

Grabs the text of the book *Unsong* by Scott Alexander from [unsongbook.com](http://unsongbook.com) and makes an extremely manly 320-page PDF out of it. This is notable as most copies of *Unsong* are around 700 pages, and do not even include the author's notes.

Requires Python 3 and PIL. Uses a folder `cache` which caches the downloaded text and images so it can be re-run again later and be a lot quicker. Requires Calibre's `ebook-convert` to actually do the conversion to pdf.

Install python requirements with `pip install -r requirements.txt`.

Fetch the text and create an HTML ebook with `get_unsong.py`, which will output `Unsong.html`.

Convert the HTML to a PDF with `convert_html_to_pdf.bat`, which will output `Unsong.pdf`. This script has been cleverly engineered to be both a valid Windows batch file and POSIX shell file, by eschewing unnecessary features such as line breaks.

Much is owed to Stuart Langridge, who did most of the hard work in creating his original [Unsong book fetcher](https://github.com/stuartlangridge/unsong-book-fetcher).