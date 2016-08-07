#-*- coding: utf-8 -*-
import re
import string
import glob
import os.path


def make_pretty_name(name):
    pretty_name = re.sub(r'-', ' ', name)
    return string.capwords(pretty_name)

header = """
# TIL
> Today I Learned

오늘 배운 내용을 간결하게 정리하여 모아둔다.

---

"""

footer = """
---

## Rules

* 폴더와 파일명은 영문 소문자로 쓴다.
* 문서는 GFM(Github Flavored Markdown) 을 따른다.


## Usage

### Generate `README.md`
```
$ python3 build.py
```

### Run in Local

Use [Docker](https://www.docker.com) and [Gollum](https://github.com/gollum/gollum). Details are [here](https://github.com/AWEEKJ/TIL/blob/master/docker/gollum-via-docker.md).


## Other TIL Collections
Inspired by

* [@thoughtbot](https://github.com/thoughtbot/til)
* [@jbranchaud](https://github.com/jbranchaud/til)
* [@milooy](https://github.com/milooy/TIL)
* [@channprj](https://github.com/channprj/TIL)

## License

© 2016 Hanju Jo

This repository is licensed under the MIT license. See `LICENSE` for details.
"""

"""
readme = open('README.md', 'r+')

readme.write(header)

readme.write("## Categories\n")

readme.write(footer)

readme.close
"""


###################################


readme = open('README.md', 'r+')
readme.write(header)
readme.write("## Categories\n")

files = glob.glob('**', recursive=True)
directories = []

for file in files:
    if os.path.isdir(file):
        directories.append(file)

directories.remove('drafts')

for directory in directories:
    readme.write("* [" + directory.capitalize() + "](#" + directory + ")\n")

for directory in directories:
    readme.write("## " + directory.capitalize() + "\n")
    sub_files = glob.glob(directory + '/*.md')
    for sub_file in sub_files:
        readme.write("* [" + make_pretty_name(os.path.basename(sub_file)) + "](" + sub_file + ")\n")

readme.write(footer)
readme.close
