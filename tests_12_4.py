import unittest
import logging

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

logging.basicConfig(
    level=logging.INFO,
    filemode='w',
    filename='runner_tests.log',
    encoding='UTF-8',
    format='%(levelname)s | %(message)s'
)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner_obj_1 = Runner('John', -5)
            for i in range(10):
                runner_obj_1.walk()
            self.assertEqual(runner_obj_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as VE:
            logging.warning(f'Неверная скорость для Runner. ValueError: {VE}')



    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner_obj_2 = Runner(123)
            for i in range(10):
                runner_obj_2.run()
            self.assertEqual(runner_obj_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as TE:
            logging.warning(f'Неверный тип данных для объекта Runner. TypeError: {TE}')



    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_obj_3 = Runner('Katie')
        runner_obj_4 = Runner('Maggie')
        for i in range(10):
            runner_obj_3.run()
            runner_obj_4.walk()
        self.assertNotEqual(runner_obj_3.distance, runner_obj_4.distance)


if __name__ == '__main__':
    unittest.main()