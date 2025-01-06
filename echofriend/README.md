# Echo Friend

A simple Telegram bot that handles three commands: `start`, `help`, and `echo`.
`echo` will make the bot send back the text attached to it

## Setup and Configuration

1. Run the [basic setup][setup]

2. Run the bot (within the virtual enviroment):

```bash
python -m echofriend
```

## Key concepts

In addition to what was implemented for [echo][echob]:

- *Bot Command*: it is a message whose text starts with `/`.
- A simple implementation of `Command` pattern makes the bot only respond
to bot commands.

## Future improvements

- Improve the env variables management
- Implement a facade to interact with Telegram.

<!-- Refs -->
[setup]:(https://github.com/sanzceb/telegram-bots?tab=readme-ov-file#installation)
[echob]:(https://github.com/sanzceb/telegram-bots/tree/main/echo)
