"""Terminal interaction and game loop for Trailhead."""

import argparse
from dataclasses import dataclass
from typing import Callable

from .story import SCENES, START_SCENE


@dataclass
class GameState:
    energy: int = 5
    water: int = 4


def play(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> None:
    """Run a game, allowing input and output to be substituted in tests."""
    state = GameState()
    current_scene = START_SCENE

    try:
        while True:
            scene = SCENES[current_scene]
            output_fn(f"\nEnergy: {state.energy} | Water: {state.water}")
            output_fn(f"\n{scene.text}")

            if not scene.choices:
                output_fn("\nThe trek is over.")
                return

            for number, choice in enumerate(scene.choices, start=1):
                output_fn(f"{number}. {choice.text}")

            while True:
                answer = input_fn("\nChoose a number (or q to quit): ").strip().lower()
                if answer == "q":
                    output_fn("You leave the trail safely. Goodbye.")
                    return
                if answer.isdigit() and 1 <= int(answer) <= len(scene.choices):
                    choice = scene.choices[int(answer) - 1]
                    state.energy += choice.energy
                    state.water += choice.water
                    current_scene = choice.next_scene
                    break
                output_fn("Please enter one of the listed numbers, or q to quit.")
    except (EOFError, KeyboardInterrupt):
        output_fn("\nYou leave the trail safely. Goodbye.")


def main() -> None:
    parser = argparse.ArgumentParser(description="A choose-your-own-adventure Himalayan trek.")
    parser.parse_args()
    play()


if __name__ == "__main__":
    main()
