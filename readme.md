# To install the exact package versions specified in a requirements.txt

`pip install -r requirements.txt`
or
`pip3 install -r requirements.txt`

# To generate/re-generate requirements file use

`pip freeze > requirements.txt`
or
`pip3 freeze > requirements.txt`

# To add a single line to requirements

`pip install <package> && pip freeze | grep <package> >> requirements.txt`
or
`pip3 install <package> && pip3 freeze | grep <package> >> requirements.txt`

Try it our because most likely >> will add a new line in the end and by doing "pip freeze" next time you will get unexpected git changes.
Also >> doesn't check if this package already is in the text file, so you can end up with duplicates.

# Run

`python youtube.py`
or
`python3 youtube.py`
