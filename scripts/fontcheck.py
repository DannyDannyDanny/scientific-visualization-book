from pathlib import Path

fontsstr = '''Roboto Condensed
Roboto Mono
Roboto Slab
Roboto
Source Code Pro
Source Sans Pro
Source Serif Pro
Times New Roman
Yanone Kaffeesatz
cursive
sans-serif
serif
xkcd
xkcd Script
Humor Sans
Comic Neue
Comic Sans MS'''

logstr = Path('out3.log').read_text()
# print(logstr)

for font in fontsstr.split('\n'):
    if font in logstr:
        print(font)
