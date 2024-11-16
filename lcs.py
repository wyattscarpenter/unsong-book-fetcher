#!/usr/bin/env python3
"""Parses the text of Unsong, and the list of chapter initials, and finds 
longest common subsequences. The idea here is that if the notarikon formed 
by the first letter of each chapter conceals a secret message, then perhaps 
parts of that message have already been revealed in the book... so if there 
were "NIEAC" is somewhere in the list of chapter initials, then that probably 
stands for "Nothing Is Ever A Coincidence", as per the many times that phrase 
is mentioned. Idea from 75thTrombone at
https://www.reddit.com/r/unsong/comments/69k1im/preemptive_final_exam_suggestion/
This script calculates those substrings. The answers are not all that promising.

It requires a file, Unsong.html, which is the text of the book with fairly plain
formatting. This file is created by Unsong Book Fetcher, which lives at
https://github.com/wyattscarpenter/unsong-book-fetcher.
"""

from bs4 import BeautifulSoup
import re
import difflib

def load_soup():
    fp = open("Unsong.html", encoding='utf8')
    data = fp.read()
    fp.close()
    soup = BeautifulSoup(data, "html.parser")
    return soup

def get_initials():
    bi = []
    ci = []
    soup = load_soup()
    chapter_headings = soup.find_all("h2")
    print("Extracting chapter initials...")
    for ch in chapter_headings:
        if "Chapter" not in ch.text:
            continue
        content = ch.parent.find_all("div", "pjgm-postcontent")
        if not content:
            continue
        # remove all blockquotes, which begin chapters
        for bq in content[0].find_all("blockquote"):
            bq.extract()
        # remove all font tags (this is a bit of a bodge, but it 
        # removes the dates at the start)
        for fnt in content[0].find_all("font"):
            fnt.extract()
        # remove all paragraphs which just have I. or II. in them (subchapter headers)
        for p in content[0].find_all("p"):
            for rn in ["I.", "II.", "III.", " – Reb Wiki"]:
                if p.text.startswith(rn):
                    p.extract()
                    break
        citxt = content[0].text[0:100].strip().upper()
        citxt = re.sub(r"[^A-Z]", "", citxt)
        ci.append(citxt[0])
        print(ch.text[:20] + "...", "->", citxt[:20], "->", citxt[0])

        bitxt = " ".join([c.text.strip() for c in content])
        bitxt = bitxt.replace("\n", " ").replace("…", " ")
        bitxt = re.sub(r"[^A-Za-z'’ ]", "", bitxt)
        initials = [(x[0].upper(), x, ch.text) for x in bitxt.split()]
        bi += initials

    print()
    return (ci, bi)

def find_lcs(ci, bi):
    print("Longest common subsequences...")
    cistr = "".join(ci)
    bistr = "".join([x[0] for x in bi])
    # we have to put the longer one first
    s = difflib.SequenceMatcher(None, bistr, cistr)
    for m in sorted(s.get_matching_blocks(), key=lambda a: a[2], reverse=True):
        bistart, cistart, length = m
        if length < 3:
            continue
        cicombined = cistr[:cistart] + " >" + cistr[cistart:cistart+length] + "< " + cistr[cistart+length:]
        bisubstr = []
        for i in range(bistart, bistart+length):
            bisubstr.append(bi[i][1])
        bisubstr = " ".join(bisubstr)
        bichapter = bi[bistart][2]
        print('%s\n%s\n"%s"' % (
            bichapter, cicombined, bisubstr
            ))
        print()

if __name__ == "__main__":
    chapter_initials, book_initials = get_initials()
    find_lcs(chapter_initials, book_initials)
