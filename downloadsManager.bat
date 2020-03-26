SETLOCAL
REM @ECHO OFF

REM Declare variables
SET DownloadPath="C:\Users\Niko\Downloads"

REM Remove files older than 7 days
forfiles /p %DownloadPath% /m *.* /c "cmd /c Del @path" /d -7

REM TEXTS
SET CurrentPath=%DownloadPath:"=%\text
forfiles /p %CurrentPath% /m *.* /c "cmd /c Del @path" /d -45
IF exist %CurrentPath% ( echo %CurrentPath% exists ) ELSE ( mkdir %CurrentPath% && echo %CurrentPath% created)
move %DownloadPath%\*.pdf %CurrentPath%
move %DownloadPath%\*.docx %CurrentPath%
move %DownloadPath%\*.txt %CurrentPath%

REM images
SET CurrentPath=%DownloadPath:"=%\images
forfiles /p %CurrentPath% /m *.* /c "cmd /c Del @path" /d -7
IF exist %CurrentPath% ( echo %CurrentPath% exists ) ELSE ( mkdir %CurrentPath% && echo %CurrentPath% created)
move %DownloadPath%\*.png %CurrentPath%
move %DownloadPath%\*.gif %CurrentPath%
move %DownloadPath%\*.jpeg %CurrentPath%
move %DownloadPath%\*.jpg %CurrentPath%
move %DownloadPath%\*.tiff %CurrentPath%
move %DownloadPath%\*.svg %CurrentPath%
move %DownloadPath%\*.eps %CurrentPath%

REM sounds
SET CurrentPath=%DownloadPath:"=%\sounds
forfiles /p %CurrentPath% /m *.* /c "cmd /c Del @path" /d -7
IF exist %CurrentPath% ( echo %CurrentPath% exists ) ELSE ( mkdir %CurrentPath% && echo %CurrentPath% created)
move %DownloadPath%\*.wav %CurrentPath%
move %DownloadPath%\*.mp3 %CurrentPath%
move %DownloadPath%\*.flac %CurrentPath%
move %DownloadPath%\*.mwa %CurrentPath%
move %DownloadPath%\*.m4a %CurrentPath%
move %DownloadPath%\*.m4p %CurrentPath%
move %DownloadPath%\*.webm %CurrentPath%

REM executables
SET CurrentPath=%DownloadPath:"=%\executables
forfiles /p %CurrentPath% /m *.* /c "cmd /c Del @path" /d -7
IF exist %CurrentPath% ( echo %CurrentPath% exists ) ELSE ( mkdir %CurrentPath% && echo %CurrentPath% created)
move %DownloadPath%\*.exe %CurrentPath%
move %DownloadPath%\*.msi %CurrentPath%
move %DownloadPath%\*.jar %CurrentPath%
move %DownloadPath%\*.apk %CurrentPath%

REM compressed
SET CurrentPath=%DownloadPath:"=%\compressed
forfiles /p %CurrentPath% /m *.* /c "cmd /c Del @path" /d -7
IF exist %CurrentPath% ( echo %CurrentPath% exists ) ELSE ( mkdir %CurrentPath% && echo %CurrentPath% created)
move %DownloadPath%\*.zip %CurrentPath%
move %DownloadPath%\*.rar %CurrentPath%
move %DownloadPath%\*.7z %CurrentPath%

REM ebooks
SET CurrentPath=%DownloadPath:"=%\ebooks
REM forfiles /p %CurrentPath% /m *.* /c "cmd /c Del @path" /d -7
IF exist %CurrentPath% ( echo %CurrentPath% exists ) ELSE ( mkdir %CurrentPath% && echo %CurrentPath% created)
move %DownloadPath%\*.epub %CurrentPath%
move %DownloadPath%\*.mobi %CurrentPath%

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

