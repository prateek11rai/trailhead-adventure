import unittest

from trailhead.story import SCENES, START_SCENE


class StoryTests(unittest.TestCase):
    def test_every_choice_targets_an_existing_scene(self):
        for scene_id, scene in SCENES.items():
            for choice in scene.choices:
                with self.subTest(scene=scene_id, destination=choice.next_scene):
                    self.assertIn(choice.next_scene, SCENES)

    def test_every_scene_is_reachable_from_the_start(self):
        reached = set()
        pending = [START_SCENE]
        while pending:
            scene_id = pending.pop()
            if scene_id in reached:
                continue
            reached.add(scene_id)
            pending.extend(
                choice.next_scene for choice in SCENES[scene_id].choices
            )
        self.assertEqual(reached, set(SCENES))

    def test_endings_have_no_choices_and_there_are_at_least_three(self):
        endings = [scene for scene in SCENES.values() if not scene.choices]
        self.assertGreaterEqual(len(endings), 3)
        self.assertTrue(all(not ending.choices for ending in endings))

    def test_non_endings_have_two_or_three_choices(self):
        for scene_id, scene in SCENES.items():
            if scene.choices:
                with self.subTest(scene=scene_id):
                    self.assertIn(len(scene.choices), (2, 3))


if __name__ == "__main__":
    unittest.main()
