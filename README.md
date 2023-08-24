# **TO RUN APP**

`uvicorn main:app --reload` for no env var

`python main.py` 

# **For messages translate**

First extract the messages to be translated into a pot file:

`pybabel extract -F babel.cfg -o messages.pot --ignore-dirs="venv" .`

Then initialize the translations:

`pybabel init -i messages.pot -d translations -l fr`

`pybabel init -i messages.pot -d translations -l de`

`pybabel init -i messages.pot -d translations -l en`

And finally compile the translations:

`pybabel compile -d translations`

For update messages:

`pybabel update -i messages.pot -d translations`