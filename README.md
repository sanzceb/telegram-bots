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

`echofriend`: A basic echo server that handles two global commands: `start` and
`help`.

## Future improvements

- Implement a new module to deal with the Telegram API
- Implement a parsing module of Telegram API responses.
