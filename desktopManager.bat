SETLOCAL
REM @ECHO OFF

REM Declare variables
SET DownloadPath="C:\Users\Nikolaj Licht\Desktop"

REM TEXTS
SET CurrentPath=%DownloadPath:"=%\text
IF exist %CurrentPath% ( echo %CurrentPath% exists ) ELSE ( mkdir %CurrentPath% && echo %CurrentPath% created)
move %DownloadPath%\*.pdf %CurrentPath:"=%
move %DownloadPath%\*.txt %CurrentPath%

REM images
SET CurrentPath=%DownloadPath:"=%\images
IF exist %CurrentPath% ( echo %CurrentPath% exists ) ELSE ( mkdir %CurrentPath% && echo %CurrentPath% created)
move %DownloadPath%\*.png %CurrentPath%
move %DownloadPath%\*.gif %CurrentPath%
move %DownloadPath%\*.jpeg %CurrentPath%
move %DownloadPath%\*.jpg %CurrentPath%
move %DownloadPath%\*.tiff %CurrentPath%
move %DownloadPath%\*.svg %CurrentPath%
move %DownloadPath%\*.eps %CurrentPath%

REM music
SET CurrentPath=%DownloadPath:"=%\music
IF exist %CurrentPath% ( echo %CurrentPath% exists ) ELSE ( mkdir %CurrentPath% && echo %CurrentPath% created)
move %DownloadPath%\*.wav %CurrentPath%
move %DownloadPath%\*.mp3 %CurrentPath%
move %DownloadPath%\*.flac %CurrentPath%
move %DownloadPath%\*.mwa %CurrentPath%
move %DownloadPath%\*.m4a %CurrentPath%
move %DownloadPath%\*.m4p %CurrentPath%
move %DownloadPath%\*.webm %CurrentPath%
move %DownloadPath%\*.aup %CurrentPath%


REM executables
SET CurrentPath=%DownloadPath:"=%\executables
IF exist %CurrentPath% ( echo %CurrentPath% exists ) ELSE ( mkdir %CurrentPath% && echo %CurrentPath% created)
move %DownloadPath%\*.exe %CurrentPath%
move %DownloadPath%\*.msi %CurrentPath%
move %DownloadPath%\*.jar %CurrentPath%
move %DownloadPath%\*.apk %CurrentPath%

REM compressed
SET CurrentPath=%DownloadPath:"=%\compressed
IF exist %CurrentPath% ( echo %CurrentPath% exists ) ELSE ( mkdir %CurrentPath% && echo %CurrentPath% created)
move %DownloadPath%\*.zip %CurrentPath%
move %DownloadPath%\*.rar %CurrentPath%
move %DownloadPath%\*.7z %CurrentPath%

REM ebooks
SET CurrentPath=%DownloadPath:"=%\ebooks
IF exist %CurrentPath% ( echo %CurrentPath% exists ) ELSE ( mkdir %CurrentPath% && echo %CurrentPath% created)
move %DownloadPath%\*.epub %CurrentPath%
move %DownloadPath%\*.mobi %CurrentPath%

REM threeD
SET CurrentPath=%DownloadPath:"=%\3D
IF exist %CurrentPath% ( echo %CurrentPath% exists ) ELSE ( mkdir %CurrentPath% && echo %CurrentPath% created)
move %DownloadPath%\*.fbx %CurrentPath%
move %DownloadPath%\*.blend %CurrentPath%
move %DownloadPath%\*.blend1 %CurrentPath%
move %DownloadPath%\*.blend2 %CurrentPath%

REM office
SET CurrentPath=%DownloadPath:"=%\office
IF exist %CurrentPath% ( echo %CurrentPath% exists ) ELSE ( mkdir %CurrentPath% && echo %CurrentPath% created)
move %DownloadPath%\*.xlsx %CurrentPath%
move %DownloadPath%\*.docx %CurrentPath%
move %DownloadPath%\*.doc %CurrentPath%
move %DownloadPath%\*.pptx %CurrentPath%
move %DownloadPath%\*.odf %CurrentPath%
move %DownloadPath%\*.one %CurrentPath%

REM AddBooksToBookFolder
SET LibraryPath="C:\Users\Niko\Books"
SET articlePath=%LibraryPath:"=%\short
ECHO %articlePath%
SET longPath=%LibraryPath:"=%\long
ECHO %longPath%
IF exist %articlePath% ( echo %articlePath% exists ) ELSE ( mkdir %articlePath% && echo %articlePath% created)
IF exist %longPath% ( echo %longPath% exists ) ELSE ( mkdir %longPath% && echo %longPath% created)
SET DownLoadTextPath=%DownloadPath:"=%\text
FOR %%G in (C:\Users\Niko\Downloads\text\*.pdf) DO FOR /F "usebackq delims==" %%i IN (`qpdf --show-npages "%%G"`) DO IF %%i LEQ 100 (move "%%G" %articlePath%) ELSE (move "%%G" %longPath%)

