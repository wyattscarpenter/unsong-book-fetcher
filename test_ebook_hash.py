#!/usr/bin/env python3

from hashlib import sha256 as s
from pathlib import Path as P
from typing import NoReturn
from subprocess import run, DEVNULL as nul
from shutil import rmtree, move

def h(file_name: str) -> str:
  return s(P(file_name).read_bytes()).hexdigest()

def a(x, y) -> None|NoReturn:
  print(x, '(actual)', '≟', y, '(expected)', x==y)
  if not x==y:
    print("Hash check failed! Do a diff of old-ebooks/ and ebooks/ , I guess...")
    exit(17)

def f(file_name_of_actual_file: str, expected_hash_hexdigest: str) -> None|NoReturn:
  print(file_name_of_actual_file)
  a( h(file_name_of_actual_file), expected_hash_hexdigest)

def compare() -> None|NoReturn:
  f('ebooks/Unsong.html', 'e716d3a24eaa5d215bb5f290d9f972e911251456a7b00865de97763aa30de580')
  #We can't use the hash method for epub; I guess calibre's ebook-convert is probably not bit-exact/deterministic/reproducible https://bugs.launchpad.net/calibre/+bug/1998328 #given infinite time on this finite earth, this would be a thing to go fix. #But given that we don't have infinite time, and there's no other reason to care about this, particularly, we use a different method: converting to txt and comparing those, since text output actually is bit-exact.  #converting to a .html is not actually supported by ebook-convert, either
  run("ebook-convert ebooks/Unsong.epub ebooks/Unsong.epub.txt", stdout=nul)
  f('ebooks/Unsong.epub.txt', "d8cb808328f81680020760620f6d432e190d88327fd5698a69150b2074be6cbd")

def main() -> None|NoReturn:
  run("ruff check --no-cache")
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
  main()
