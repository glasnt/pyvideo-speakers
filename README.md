# PyVideo Speakers

A CLI that visualises repeat speakers from events listed in https://github.com/pyvideo/data

Not terribly efficient, but you know. 

## Install

```
# if you don't already have the data
git clone https://github.com/pyvideo/data 


git clone https://github.com/glasnt/pyvideo_speakers
cd pyvideo_speakers
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```
$ ./speakers.py  --help
Usage: speakers.py [OPTIONS] EVENT_SEARCH

  Visualise event speakers from PyVideo data

Options:
  -d, --pyvideo-data PATH  Location of the PyVideo data cloned repo
  -s, --style [table|csv]  Visualisation style
  --help                   Show this message and exit.
```