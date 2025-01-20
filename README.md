# Repository of Telegram Bots

## Installation

Create the virtual environment:

```bash
python -m venv bots_env
```

Active the environment on Linux/Mac:

```bash
source bots_env/bin/activate
```

Activate the environment on Windows:

```txt
bots_env\Scripts\activate
```

Install the dependencies with `pip`:

```bash
pip install -r requirements.txt
```

## Repository Structure

`schemas`: JSON schemas of requests and responses for easy reference.

`echo`: A very basic echo server to test the bot API

`echofriend`: A basic echo server that handles three global commands: `start`
, `help` and `echo`.

`fixture_scout`: A simple bot that reads a football calendar from csv files
responds to queries made by the command `/fixture`. It is in development right now.

## Future improvements

- `fixture_scout`: Create a simple module import the data from csv files
using `csv` module
