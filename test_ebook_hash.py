from hashlib import sha256 as s
from pathlib import Path as P
from typing import NoReturn

def h(file_name: str) -> str:
  return s(P(file_name).read_bytes()).hexdigest()

def a(x, y) -> None|NoReturn:
  print(x, '(actual)', '≟', y, '(expected)', x==y)
  if not x==y:
    print("Hash check failed! Do a diff, I guess...")
    exit(17)

def f(file_name_of_actual_file: str, expected_hash_hexdigest: str) -> None|NoReturn:
  print(file_name_of_actual_file)
  a( h(file_name_of_actual_file), expected_hash_hexdigest)
  
x = h('Unsong.html')
y = 'e716d3a24eaa5d215bb5f290d9f972e911251456a7b00865de97763aa30de580'
a(x,y)
x = h('Unsong.epub')
y = '7fb5309633a68a1440fe4c95bff5095dd55265d4db07186684aadd88211a7b9f'
#a(x, y) #I guess calibre's ebook-convert is probably not bit-exact/deterministic/reproducible https://bugs.launchpad.net/calibre/+bug/1998328 #given infinite time on this finite earth, this would be a thing to go fix. #But given that we don't have infinite time, and there's no other reason to care about this, particularly, we use a different method: converting to txt and comparing those, since text output actually is bit-exact.
f('Unsong.epub.txt', "d8cb808328f81680020760620f6d432e190d88327fd5698a69150b2074be6cbd")
