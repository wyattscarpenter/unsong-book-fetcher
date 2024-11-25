: << '____CMD____'


@echo off

call pip3 install -r ".\requirements.txt" -qq
call python3 ".\get_unsong.py" || call python ".\get_unsong.py"

call ebook-convert ".\ebooks\Unsong.html" ".\ebooks\Unsong.epub" ^
 --level1-toc="//h:h1" ^
 --level2-toc="//h:h2" ^
 --no-default-epub-cover ^
 --authors "Scott Alexander" ^
 --language en

goto :EOF


____CMD____



pip3 install -r "./requirements.txt" -qq
python3 "./get_unsong.py" || python "./get_unsong.py"

ebook-convert "./ebooks/Unsong.html" "./ebooks/Unsong.epub" \
  --level1-toc="//h:h1" \
  --level2-toc="//h:h2" \
  --no-default-epub-cover \
  --authors "Scott Alexander" \
  --language en

exit 0
