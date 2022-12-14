#
#    setup.py
#
# MIT License
# 
# Copyright (c) 2022 Alicia González Martínez and Thomas Milo
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#################################################################################

from distutils.core import setup

def readme():
    with open('README.md') as fp:
        return fp.read()

setup(
    name = "rasm",
    packages = ["rasm", "resources"],
    package_data = {'resources' : ['mushaf_simple.json', 'mushaf_uthmani.json', 'mushaf_dt.json']},
    version = "1.0",
    description = "text utility for converting Arabic-scripted text to a completely dediacritised skeleton",
    long_description = readme(),
    author = "Alicia González Martínez and Thomas Milo",
    author_email = "aliciagm85+kabikaj@gmail.com",
    url = "https://gitlab.com/abjad/yakabikaj.git",
    download_url = "git@gitlab.com:abjad/yakabikaj.git",
    scripts=['bin/rasm'],
    keywords = ["arabic", "persian", "urdu", "quran", "manuscript", "rasm", "unicode", "NLP", "digital humanities"],
    license = 'MIT',
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Arabic",
        "Natural Language :: Persian",
        "Natural Language :: Urdu"
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Religion",
        "Topic :: Scientific/Engineering :: Information Analysis"
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        ]
)