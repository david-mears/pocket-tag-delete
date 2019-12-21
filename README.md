# Deleting by tag for Pocket

A script that deletes things tagged with whatever you like, on Pocket.

## Installation

Using the terminal on MacOS, given you have Python and Git (should come with MacOS).

Clone this project:
```bash
git clone https://github.com/david-mears/pocket-tag-delete.git
```

Change into the newly created directory:
```bash
cd pocket-tag-delete
```

Make sure geckodriver is intalled. (Might be fiddly for MacOS Catalina, the geckodriver devs are working on it. The below works on 21st December 2019.) 

```bash
curl -OL https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-macos.tar.gz
tar -xvf geckodriver-v0.26.0-macos.tar.gz
```

Put geckodriver on PATH. That means: take the filepath to the directory containing geckodriver, and add it to the environment variable called PATH. If the filepath to the directory containing geckodriver is /Users/david/random_directory, then:

```bash
export PATH=$PATH:/Users/david/random_directory
```

Also make sure Firefox is installed.

Still/back in the directory pocket-tag-delete, create and activate the virtual environment:
```bash
python3 -m venv env
```
(That's assuming you have Python 3.)
```bash
source env/bin/activate
```

Then:
```bash
pip install -r requirements.txt
```

Create a file called '.env' in the root directory:
```bash
touch .env
```

and open it:
```
open .env
```

Put in your pocket username and password, e.g., and save the file:

POCKET_USERNAME=my@username.com
POCKET_PASSWORD=secret_password

## Use

By default, this script deletes everything tagged 'hacker news'. To change this, just change the variable called `url` in script.py before running it. Pocket turns whitespaces in the tags into hyphens for the purposes of this url.

To run, you'll have installed, and activated the virtual environment:
```bash
python script.py
```

If it errors, try it again.
