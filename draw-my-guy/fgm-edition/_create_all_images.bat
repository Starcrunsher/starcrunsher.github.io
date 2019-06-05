
goto anfang
:anfang

mkdir out\
for %%f in (*.png) do S:\ffmpeg\bin\ffmpeg.exe -i "%%f" -vf "scale=w=960:h=540:force_original_aspect_ratio=1" -pix_fmt rgba -compression_level 200 -n "out\%%~nf.png"

goto ende
:ende
pause
