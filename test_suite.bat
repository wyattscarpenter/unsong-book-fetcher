ruff check --no-cache
echo this test script barely works and TODO I will fix it more
python test_ebook_hash.py
call create_unsong_book.bat
ebook-convert Unsong.epub Unsong.epub.txt
# ebook-convert Unsong.epub Unsong.epub.html #converting to a .html is not actually supported by ebook-convert, huh
python test_ebook_hash.py
# Ideally we would use the calibre comparison tool if we need to examine the differences between two epubs. However, opening this view this doesn't seem scriptable. Probably the best you can do is `calibre old.epub new.epub`, and manually enter the comparison view.
