#!/bin/bash
# this is both a valid batch script and a valid bash script
mkdir cache
pip3 install -r requirements.txt && python3 get_unsong.py || python get_unsong.py
ebook-convert Unsong.html Unsong.epub --level1-toc="//h:h1" --level2-toc="//h:h2" --no-default-epub-cover --authors "Scott Alexander" --language en --search-replace replacements.txt