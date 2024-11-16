#!/usr/bin/env python3

from hashlib import sha256 as s
from pathlib import Path as P
from typing import NoReturn
from subprocess import run, DEVNULL as nul
from shutil import rmtree, move
from sys import argv


def h(file_name: str) -> str:
    return s(P(file_name).read_bytes()).hexdigest()


def a(x, y) -> None | NoReturn:
    print(x, "(actual)", "≟", y, "(expected)", x == y)
    if not x == y:
        print("Hash check failed! Do a diff of old-ebooks/ and ebooks/ , I guess...")
        exit(17)


def f(file_name_of_actual_file: str, expected_hash_hexdigest: str) -> None | NoReturn:
    print(file_name_of_actual_file)
    a(h(file_name_of_actual_file), expected_hash_hexdigest)


html_file_name = "ebooks/Unsong.html"
txt_file_name = "ebooks/Unsong.epub.txt"
html_hardcoded_hash = "905caec08c3d3ede586f2ecef837b20bf17ba31f9637283cd0eef43b608e9adf"
txt_hardcoded_hash = "c7e34ef4e8e46230f7aa81028885cc3c6b74c636ef7218a1d6e32ee86cab5fed"


def compare() -> None | NoReturn:
    f(html_file_name, html_hardcoded_hash)
    # We can't use the hash method for epub; I guess calibre's ebook-convert is probably not bit-exact/deterministic/reproducible https://bugs.launchpad.net/calibre/+bug/1998328 #given infinite time on this finite earth, this would be a thing to go fix. #But given that we don't have infinite time, and there's no other reason to care about this, particularly, we use a different method: converting to txt and comparing those, since text output actually is bit-exact.  #converting to a .html is not actually supported by ebook-convert, either
    run("ebook-convert ebooks/Unsong.epub ebooks/Unsong.epub.txt", stdout=nul)
    f(txt_file_name, txt_hardcoded_hash)


def main() -> None | NoReturn:
    print("::::comparing extant files")
    compare()
    print("::::generate new files (moving the old files to old-ebooks)")
    rmtree("old-ebooks", ignore_errors=True)
    move("ebooks", "old-ebooks")
    run("create_unsong_book.bat", stdout=nul)
    print("::::comparing newly-generated files")
    compare()
    # Ideally we would use the calibre comparison tool if we need to examine the differences between two epubs. However, opening this view this doesn't seem scriptable. Probably the best you can do is `calibre old.epub new.epub`, and manually enter the comparison view.


if __name__ == "__main__":
    print("::::ruff")
    run("ruff check --no-cache")
    if "--update" in argv:
        if h(html_file_name) != h("old-ebooks/Unsong.html") or h(txt_file_name) != h("old-ebooks/Unsong.epub.txt"):
            print("You have requested a hash update, but the hashes in old-ebooks/ don't match the ones in ebooks/, which is odd, so as a precaution I'm not doing anything, and you can sort that out.")
        else:
            # a very silly way of doing, you know, the thing.
            P(argv[0]).write_text(
                P(argv[0])
                .read_text()
                .replace(html_hardcoded_hash, h(html_file_name))
                .replace(txt_hardcoded_hash, h(txt_file_name))
            )
    else:
        main()
