import unittest

from trailhead.engine import play


class EngineTests(unittest.TestCase):
    def test_invalid_input_reprompts_without_leaving_scene(self):
        answers = iter(("invalid", "q"))
        prompts = []
        output = []

        def answer(prompt):
            prompts.append(prompt)
            return next(answers)

        play(answer, output.append)

        self.assertEqual(len(prompts), 2)
        self.assertEqual(output[:4], output[5:9])
        self.assertEqual(
            output.count("Please enter one of the listed numbers, or q to quit."),
            1,
        )
        self.assertIn("You leave the trail safely. Goodbye.", output)

    def test_scripted_paths_reach_each_ending_and_stop(self):
        endings = {
            "Sunlight at the lake": ("1", "1", "1", "1", "2", "1"),
            "A safe return": ("1", "1", "2", "1"),
            "Caught out": ("1", "1", "2", "2", "1", "1"),
            "Too tired or too dry": ("2", "2", "1", "1"),
        }
        for ending, scripted_answers in endings.items():
            with self.subTest(ending=ending):
                answers = iter(scripted_answers)
                output = []
                play(lambda _prompt: next(answers), output.append)
                self.assertIn(f"\nEnding: {ending}", output)
                self.assertEqual(output[-1], "\nThe trek is over.")
                with self.assertRaises(StopIteration):
                    next(answers)

    def test_depleted_resources_are_never_displayed_as_negative(self):
        answers = iter(("2", "2", "1", "1"))
        output = []
        play(lambda _prompt: next(answers), output.append)
        resource_displays = [
            line for line in output if line.startswith("\nEnergy: ")
        ]
        self.assertTrue(resource_displays)
        self.assertTrue(
            all("-" not in display.split("|")[0] for display in resource_displays)
        )
        self.assertTrue(
            all("-" not in display.split("|")[1] for display in resource_displays)
        )

    def test_q_quits_cleanly(self):
        output = []
        play(lambda _prompt: "q", output.append)
        self.assertIn("You leave the trail safely. Goodbye.", output)

    def test_eof_quits_cleanly(self):
        output = []

        def eof(_prompt):
            raise EOFError

        play(eof, output.append)
        self.assertIn("\nYou leave the trail safely. Goodbye.", output)

    def test_keyboard_interrupt_quits_cleanly(self):
        output = []

        def interrupt(_prompt):
            raise KeyboardInterrupt

        play(interrupt, output.append)
        self.assertIn("\nYou leave the trail safely. Goodbye.", output)


if __name__ == "__main__":
    unittest.main()
