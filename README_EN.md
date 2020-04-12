# botank
It is a tool for automated testing of Alice skills 
(and maybe other chat bots in the future).

We shoot random requests into your bot and look how it copes with them.

The tool is written in Python, but it calls the bots through a web hook, 
therefore the bots can be written in any language or without language at all.

Links: [GitHub](https://github.com/avidale/botank), 
[PyPI](https://pypi.org/project/botank/).

Read this in other languages: 
[English](https://github.com/avidale/botank/blob/master/README_EN.md), 
[Русский](https://github.com/avidale/botank).

## The essentials
To install the tool you need Python>=3.6 and the `pip` package manager 
(or analogs). 

Installation:
```commandline
pip install botank
```

Usage:
```commandline
python -m botank http://localhost:5000/alice/ -n 100 -o results.txt
```
When you run it like this, 
*botank* sends to `http://localhost:5000/alice/` 
100 Alice-like random requests into your skill, 
and saves the results to the file `results.txt`.
