
Set-Location "C:\pico\imageProcessing"

python C:\pico\imageProcessing\web2pdf.py

cmd.exe /c "magick convert screenshot.png -crop 480x800+0+0 screenshot800480.png"

Set-Location "C:\pico\imageProcessing\ImageToEpaperConverter-master"

node standalone

Set-Location "C:\pico\imageProcessing"



