# Mastermind

A classic implementation of Mastermind with Python (working with python 2.7 and python 3).

## Quick start

### Step 0 : Installation python and virtualenv

```
# Ubuntu
sudo apt-get install python3 python3-pip virtualenv
```

### Step 1 : Create virtualenv and download dependencies

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 2 : Launch

```
# For graphical UI
python main.py

# For autorun 5000 time without graphical UI
python main.py 5000
```

## Files

* main.py : The entry point
* model.py : Contain the **Board** object
* basic_ai.py : Classic algorithm that generate all possible moves and reduce the list from the previous play
* ui.py : Classes and function to draw the game by using *pygame*
* stats.py : Class that generate XLXS file with games stats
