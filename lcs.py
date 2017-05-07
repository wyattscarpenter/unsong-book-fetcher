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
formatting. This file is created by my epub builder for Unsong, which lives at
https://github.com/stuartlangridge/unsong-book-fetcher.
"""

from bs4 import BeautifulSoup
import re
import difflib

def load_soup():
    fp = open("Unsong.html")
    data = fp.read()
    fp.close()
    soup = BeautifulSoup(data, "lxml")
    return soup

def get_initials_of_chapters():
    ci = []
    soup = load_soup()
    chapter_headings = soup.find_all("h2")
    print("Extracting chapter initials...")
    for ch in chapter_headings:
        if "Chapter" not in ch.text: continue
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
            if p.text in ["I.", "II.", "III."]:
                p.extract()
        txt = content[0].text[0:100].strip().upper()
        txt = re.sub(r"[^A-Z]", "", txt)
        ci.append(txt[0])
        print(ch.text[:20] + "...", "->", txt[:20], "->", txt[0])
    print()
    return ci

def get_initials_of_book():
    bi = []
    soup = load_soup()
    chapter_headings = soup.find_all("h2")
    for ch in chapter_headings:
        if "Chapter" not in ch.text: continue
        content = ch.parent.find_all("div", "pjgm-postcontent")
        if not content:
            continue
        # remove all blockquotes, which begin chapters
        for bq in content[0].find_all("blockquote"):
            bq.extract()
        # remove all font tags (this is a bit of a bodge, but it removes the dates at the start)
        for fnt in content[0].find_all("font"):
            fnt.extract()

        # now, get all text

        txt = " ".join([c.text.strip() for c in content])
        txt = txt.replace("\n", " ").replace("…", " ")
        txt = re.sub(r"[^A-Za-z'’ ]", "", txt)
        initials = [(x[0].upper(), x, ch.text) for x in txt.split()]
        bi += initials
    return bi

def find_lcs(ci, bi):
    print("Longest common subsequences...")
    cistr = "".join(ci)
    bistr = "".join([x[0] for x in bi])
    # we have to put the longer one first
    s = difflib.SequenceMatcher(None, bistr, cistr)
    for m in sorted(s.get_matching_blocks(), key=lambda a: a[2], reverse=True):
        bistart, cistart, length = m
        if length < 3: continue
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
    chapter_initials = get_initials_of_chapters()
    book_initials = get_initials_of_book()
    find_lcs(chapter_initials, book_initials)
