#!/bin/bash

mkdir -p cache

echo Fetching book
python3 get_unsong.py $*

echo Making ebook
ebook-convert Unsong.html Unsong.epub \
    --level1-toc="//h:h1" \
    --level2-toc="//h:h2[re:test(., 'chapter|interlude', 'i')]" \
    --no-chapters-in-toc --no-default-epub-cover \
    --authors "Scott Alexander" --language en \
    --chapter /

echo Done in Unsong.epub
