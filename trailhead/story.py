"""Story data for Trailhead, kept separate from the game engine."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Choice:
    text: str
    next_scene: str
    energy: int = 0
    water: int = 0


@dataclass(frozen=True)
class Scene:
    text: str
    choices: tuple[Choice, ...] = ()
    ending: str | None = None


SCENES: dict[str, Scene] = {
    "trailhead": Scene(
        "At the trailhead, the cedar-scented valley opens toward a high Himalayan lake. "
        "Your guide suggests a gentle first day; clouds are gathering beyond the ridge.",
        (
            Choice("Spend a day acclimatising in the village.", "acclimatise", energy=1, water=1),
            Choice("Set off at once to gain ground.", "rush", energy=-1, water=-1),
        ),
    ),
    "acclimatise": Scene(
        "You take an easy walk, sip water, and sleep low. By morning, the climb feels less hurried.",
        (
            Choice("Check in with the village team before leaving.", "village_check", energy=1),
            Choice("Start early while the air is cool.", "early_start", water=-1),
        ),
    ),
    "rush": Scene(
        "The steep start leaves your breathing ragged. A shepherd points out a nearby resting stop.",
        (
            Choice("Pause, drink, and settle your pace.", "village_check", energy=1, water=-1),
            Choice("Press on up the steep path.", "steep_ascent", energy=-2, water=-1),
        ),
    ),
    "village_check": Scene(
        "At the last homes, you hear the afternoon forecast and mark the team's turnaround time.",
        (
            Choice("Follow the forest trail toward the meadow.", "meadow", water=-1),
            Choice("Wait and watch the weather before committing.", "storm_watch", energy=1),
        ),
    ),
    "early_start": Scene(
        "The dawn is clear. You keep a steady pace and leave the first flowers undisturbed.",
        (
            Choice("Take the lower meadow path.", "meadow", water=-1),
            Choice("Climb toward the ridge while skies are clear.", "ridge", energy=-1, water=-1),
        ),
    ),
    "steep_ascent": Scene(
        "Loose stones slow your climb. A cold breeze carries the smell of rain from the pass.",
        (
            Choice("Continue carefully to the ridge.", "ridge", energy=-1, water=-1),
            Choice("Stop at the sheltered bend and reassess.", "storm_watch", energy=1),
        ),
    ),
    "meadow": Scene(
        "A broad alpine meadow lies below the snowline. You refill from your treated water and pack out a snack wrapper.",
        (
            Choice("Cross the stream where it runs shallow.", "stream", energy=-1, water=1),
            Choice("Take the longer, sheltered track to camp.", "forest_camp", energy=1, water=-1),
        ),
    ),
    "ridge": Scene(
        "From the ridge, the lake basin is visible, but a veil of cloud is closing over the high ground.",
        (
            Choice("Descend toward the lake approach, keeping to the marked trail.", "lake_approach", energy=-1, water=-1),
            Choice("Drop back to shelter and check the clouds.", "storm_watch", energy=1),
        ),
    ),
    "storm_watch": Scene(
        "Rain begins to drum on your hood. The guide checks the time: the safe turnaround window is narrowing.",
        (
            Choice("Turn back together while the trail is still clear.", "safe_return"),
            Choice("Take the exposed pass despite the weather and the agreed time.", "exposed_pass", energy=-2, water=-1),
        ),
    ),
    "stream": Scene(
        "The stream is stronger than it looked. You cross one at a time, then pause to steady your breath.",
        (
            Choice("Rest at the forest camp before climbing higher.", "forest_camp", energy=1),
            Choice("Continue toward the lake while you have daylight.", "lake_approach", energy=-1, water=-1),
        ),
    ),
    "forest_camp": Scene(
        "At camp, you add a warm layer, top up your bottle, and leave the small clearing as you found it.",
        (
            Choice("Head up to the lake approach before the turnaround time.", "lake_approach", energy=-1, water=-1),
            Choice("Listen to the wind and check in with the guide.", "storm_watch", energy=1),
        ),
    ),
    "exposed_pass": Scene(
        "Wind drives sleet across the pass. Your hands are cold, and the safe hour to turn around has passed.",
        (
            Choice("Keep pushing for the lake in worsening visibility.", "late_push", energy=-2, water=-1),
            Choice("Admit the conditions have changed and descend carefully.", "safe_return", energy=-1),
        ),
    ),
    "lake_approach": Scene(
        "The last climb is steep and the air thin. You check the time: there is just enough margin to reach the basin and return.",
        (
            Choice("Continue at a measured pace toward the lake.", "lake_ending", energy=-1, water=-1),
            Choice("Push beyond the turnaround time for a better view.", "late_push", energy=-2, water=-1),
            Choice("Turn back now with daylight and a clear route.", "safe_return"),
        ),
    ),
    "late_push": Scene(
        "The light fades behind the ridge. Cold fingers and low water make the descent harder to judge.",
        (
            Choice("Press on in the dark, away from the agreed plan.", "caught_out", energy=-2, water=-1),
            Choice("Stop the climb and descend cautiously with your group.", "safe_return", energy=-1),
        ),
    ),
    "lake_ending": Scene(
        "In the afternoon light, the lake catches a stripe of gold beneath the peaks. "
        "You take it in quietly, carry every scrap back, and start down on time.",
        ending="Sunlight at the lake",
    ),
    "safe_return": Scene(
        "You return safely before the weather closes in. The lake will wait; your team has made the mountain a good day by turning back together.",
        ending="A safe return",
    ),
    "caught_out": Scene(
        "Darkness and sleet catch your group above the tree line. You huddle for a difficult night, a stark reminder that the turnaround time was there for a reason.",
        ending="Caught out",
    ),
    "spent": Scene(
        "Your group is too tired or too short on water to continue safely. You turn back early together, carrying the lesson that a good trek depends on respecting your limits.",
        ending="Too tired or too dry",
    ),
}

START_SCENE = "trailhead"
SPENT_SCENE = "spent"
