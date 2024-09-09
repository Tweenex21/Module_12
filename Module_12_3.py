import unittest
import test_12_1
import test_12_2

TestSuite_RT = unittest.TestSuite()
TestSuite_RT.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
TestSuite_RT.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(TestSuite_RT)