# open_notify_cli

This Python script allows the user to get information from <http://api.open-notify.org/> through a command-line interface.

## Installation Instructions

1. `python3 -m venv ./venv`
2. `source ./venv/bin/activate`
3. `pip install -r requirements.txt`

## Usage Examples

### Get the current location of the ISS

```python
>>> ./app.py loc
The ISS current location at 2019-10-31 17:49:58.204460 is (-49.6510, -75.2648)
```

### For each craft, get the details of everyone currently in space

```python
>>> ./app.py people
There are 6 people aboard the ISS. They are Christina Koch, Alexander Skvortsov, Luca Parmitano, Andrew Morgan, Oleg Skripochka, Jessica Meir
```

### Get the passing details of the ISS for a given location

#### Format for getting ISS passing details

`./app.py pass {latitude} {longitude}`

```python
>>> ./app.py pass 34 -130
The ISS will be overhead ('34', '-130') at 1572599467 for 450
The ISS will be overhead ('34', '-130') at 1572605137 for 654
The ISS will be overhead ('34', '-130') at 1572611021 for 546
The ISS will be overhead ('34', '-130') at 1572617008 for 350
The ISS will be overhead ('34', '-130') at 1572622885 for 413
```
