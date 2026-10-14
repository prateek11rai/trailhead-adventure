import unittest

from trailhead.story import SCENES, SPENT_SCENE, START_SCENE


class StoryTests(unittest.TestCase):
    def test_every_choice_targets_an_existing_scene(self):
        for scene_id, scene in SCENES.items():
            for choice in scene.choices:
                with self.subTest(scene=scene_id, destination=choice.next_scene):
                    self.assertIn(choice.next_scene, SCENES)

    def test_every_scene_is_reachable_from_the_start(self):
        reached = set()
        pending = [(START_SCENE, 5, 4)]
        visited_states = set()
        while pending:
            state = pending.pop()
            if state in visited_states:
                continue
            visited_states.add(state)
            scene_id, energy, water = state
            reached.add(scene_id)
            for choice in SCENES[scene_id].choices:
                next_energy = energy + choice.energy
                next_water = water + choice.water
                if next_energy <= 0 or next_water <= 0:
                    reached.add(SPENT_SCENE)
                else:
                    pending.append((choice.next_scene, next_energy, next_water))
        self.assertEqual(reached, set(SCENES))

    def test_endings_have_no_choices_and_labels(self):
        endings = [scene for scene in SCENES.values() if not scene.choices]
        self.assertTrue(all(not ending.choices for ending in endings))
        self.assertTrue(all(ending.ending for ending in endings))

    def test_non_endings_have_two_or_three_choices(self):
        for scene_id, scene in SCENES.items():
            if scene.choices:
                with self.subTest(scene=scene_id):
                    self.assertIn(len(scene.choices), (2, 3))


if __name__ == "__main__":
    unittest.main()
