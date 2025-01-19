# Fixture Scout Bot

## Workflow Design

- The bot is registered in the telegram client
- The telegram client calls back the bot
- Handles one of the following commands: `start`, `help`, `fixtures`.
- `start` and `help` both return help texts.
- `fixtures` will query the fixtures of a given team for the upcoming month.
- The bot calls the message client to answer the user.

## Data access

- The module fixture maps relational records to objects.
- It publishes the definition of a fixture that the core will consume.
