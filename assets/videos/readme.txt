One of the author notes links to these youtube videos, which we also include here in this github repo for posterity — although we don't include them in the ebook directly as this would multiply the file size of the ebook by 100.

One of the videos is 107MiB — too big for GitHub to want to host it! We also could not include it via git lfs because of https://github.com/wyattscarpenter/unsong-book-fetcher/issues/19#issuecomment-2482879452 ; so, "Mayor Ed Koch Tells About his Late-Night Meeting with the Rebbe [WZaSVyDVHe0].mp4" is stored in here as a multi-part zip file. Hopefully this is easier to most users than the obvious alternative of just breaking the file up on byte boundaries and requiring you to cat it back together. You may need to install 7zip to unzip this file? In fact, I think you do.

(In retrospect, it would have been better to simply partition the files, and rely on the following simple command line commands to reconstruct them:
• (posix) cat file1.bin file2.bin file3.bin > file4.mp4
• (windows cmd) copy /b File1.bin + File2.bin + File3.bin File4.mp4
(concatenating files is also a trivial thing to do in almost any programming language, unlike implementing the standard method of unzipping multiple files)
But at this point it's not worth the bother of redoing.)
