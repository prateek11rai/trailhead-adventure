import unittest

from trailhead.engine import play


class EngineTests(unittest.TestCase):
    def test_invalid_input_reprompts_without_leaving_scene(self):
        answers = iter(("invalid", "0", "1", "q"))
        prompts = []
        output = []

        def answer(prompt):
            prompts.append(prompt)
            return next(answers)

        play(answer, output.append)

        rendered = "\n".join(output)
        self.assertEqual(rendered.count("At the trailhead"), 1)
        self.assertEqual(len(prompts), 4)
        self.assertEqual(rendered.count("Please enter one of the listed numbers, or q to quit."), 2)
        self.assertIn("You leave the trail safely. Goodbye.", rendered)

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
