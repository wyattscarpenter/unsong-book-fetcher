# Unsong Book Fetcher

## Executive summary

This software project grabs the text of the book *Unsong* by Scott Alexander from [unsongbook.com](http://unsongbook.com) and makes an epub out of it.

If you would like one of these ebooks, please check out the files in the ebooks folder.

Please note that in order to get the finalized, revised version of Unsong — and to financially support its author — you must purchase the ebook (or regular book) from <https://www.amazon.com/Unsong-Scott-Alexander-ebook/dp/B0D84DLKZW> (or <https://www.amazon.com/Unsong-Scott-Alexander/dp/B0D57BYS3Y> for the paperback); the ebooks here are the story as it is presented on the freely-available <http://unsongbook.com>.

## Running the software, per se

The pre-made ebooks are in the ebooks folder. However, you may perhaps wish to run this software project yourself and thereby create the ebooks (someone must have done this at some point!) To use this project in that way:
- download this project if you don't already have it. The easiest way to do this is probably clicking the green "< > Code" above the file listing of this project on github, and then click "Download ZIP", and then once the zip file is downloaded, extract it and put the resulting folder somewhere convenient.
- install, or already have installed, Python 3. You can try running python on the command line to see if you have it, or just download it from https://www.python.org/downloads/
- install, or already have installed, Calibre, which you can download from here: <https://calibre-ebook.com/download>
- run `create_unsong_book.bat`.

(If you know what a package manager is, and you have one, you can try using that for the "install" steps, instead.)

I'm not sure what the earliest calibre version that will work is — 4.11 and 7.21.0 both worked for my purposes. Regardless, whatever calibre you get will *probably* be fine. It would be nice if we could just install calibre from pypi — it's even written mostly in python! But it's not on there, apparently. If I had infinite time on this finite earth I would bug the calibre person(s) to get it on there, I think.

All you have to do once everything is installed is run `create_unsong_book.bat`. This script has been cleverly engineered to be both a valid Windows batch file and POSIX shell file. This script installs python requirements with `pip install -r requirements.txt`, fetches the text and creates an HTML ebook with `get_unsong.py` (which will output `Unsong.html`), and converts the HTML to an epub with `ebook-convert` (which will output `Unsong.epub`).

## Testing

test_ebook_hash.py tests get_unsong.py for regressions, as best it can. It does this using file hashing. TODO: this test code is pretty good right now, but I'm making a lot of changes to the epub so the hardcoded file hashes may be much out of date.

## lcs.py

This file discovers the name of God. It is thus a spoiler for _Unsong_.
