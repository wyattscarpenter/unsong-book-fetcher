# this is both a valid Windows batch script and a unix shell script
# remake this dir just in case:
mkdir cache
pip3 install -r requirements.txt -qq && python3 get_unsong.py || python get_unsong.py
ebook-convert Unsong.html Unsong.epub --level1-toc="//h:h1" --level2-toc="//h:h2" --no-default-epub-cover --authors "Scott Alexander" --language en
