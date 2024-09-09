import unittest
import Module_12_2

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Module_12_2.Runner("Усэйн", speed=10)
        self.andrey = Module_12_2.Runner("Андрей", speed=9)
        self.nick = Module_12_2.Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for place, runner in sorted(cls.all_results.items()):
            print(f"{place}: {runner}")

    def test_usain_and_nick(self):
        tournament = Module_12_2.Tournament(90, self.usain, self.nick)
        self.all_results.update(tournament.start())
        self.assertTrue(self.all_results[max(self.all_results)] is self.nick)

    def test_andrey_and_nick(self):
        tournament = Module_12_2.Tournament(90, self.andrey, self.nick)
        self.all_results.update(tournament.start())
        self.assertTrue(self.all_results[max(self.all_results)] is self.nick)

    def test_usain_andrey_and_nick(self):
        tournament = Module_12_2.Tournament(90, self.usain, self.andrey, self.nick)
        self.all_results.update(tournament.start())
        self.assertTrue(self.all_results[max(self.all_results)] is self.nick)


if __name__ == '__main__':
    unittest.main()