# Trailhead

Trailhead is a small terminal choose-your-own-adventure game about leading a trek to a high-altitude Himalayan lake. Your choices shape the journey: acclimatise or hurry, manage your energy and water, and decide whether the conditions leave enough time to continue.

## Play

Run the game with Python 3.10 or newer:

```sh
python -m trailhead
```

Choose a numbered option at each scene. Enter `q` to quit; end-of-file and Ctrl+C also exit cleanly. The game uses only the Python standard library.

## Tests

Run the unit tests with:

```sh
python -m unittest
```

## Endings

There are several possible endings, shaped by your decisions and by whether your group has enough energy and water to continue safely. Reach an ending to see its label; the routes are yours to discover.

## Project layout

```text
trailhead/
  engine.py   # Terminal interaction and game loop
  story.py    # Scenes, choices, and ending text
  __main__.py # Entry point for python -m trailhead
tests/
  test_engine.py
  test_story.py
```

## Built with GitHub Copilot

Trailhead was built in a GitHub Codespace with GitHub Copilot CLI. GitHub Copilot is credited as a co-author on the commits.
