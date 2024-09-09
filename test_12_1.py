import Lesson_12_1
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Lesson_12_1.Runner("Test Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Lesson_12_1.Runner("Test Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Lesson_12_1.Runner("Runner One")
        runner2 = Lesson_12_1.Runner("Runner Two")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()