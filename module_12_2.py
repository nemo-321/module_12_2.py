# Здесь мы импортируем необходимые модули. `runner_and_tournament` содержит классы и функции, которые мы собираемся
# тестировать, а `unittest` — это стандартная библиотека для написания тестов в Python.

import runner_and_tournament
import unittest

# Мы создаем класс `TournamentTest`, который наследует от `unittest.TestCase`.
# Это позволяет нам использовать методы для тестирования.

class TournamentTest(unittest.TestCase):

    # Класс-метод для настройки тестов:
    # Метод `setUpClass` вызывается один раз перед запуском всех тестов.
    # Здесь мы создаем словарь `all_results`, который будет хранить результаты всех тестов.
    
    all_results = None
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    # Метод настройки для каждого теста:
    # Метод `setUp` вызывается перед каждым тестом. Здесь мы создаем три экземпляра класса `Runner`
    # с разными именами и скоростями.

    def setUp(self):
        self.usain = runner_and_tournament.Runner('Усэйн', 10)
        self.andrey = runner_and_tournament.Runner('Андрей', 9)
        self.nik = runner_and_tournament.Runner('Ник', 3)

    #  Метод для очистки после всех тестов:
    #  Метод `tearDownClass` вызывается один раз после выполнения всех тестов.
    #  Здесь мы собираем и выводим результаты всех тестов, преобразуя их в строковый формат.

    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for key, value in value.items():
                res[key] = str(value)
            print(res)

    # Тестовые методы:  Каждый метод, начинающийся с `test_`, представляет собой отдельный тест:
    # Здесь создается турнир между Усэйном и Ником. После запуска турнира мы проверяем, что последний
    # финишировавший бегун — Ник. Результат сохраняется в `all_results`.

    def test_1(self):
        first_run = runner_and_tournament.Tournament(90, self.usain, self.nik)
        result = first_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    # test_2: Аналогично, но с Андреем и Ником.

    def test_2(self):
        second_run = runner_and_tournament.Tournament(90, self.andrey, self.nik)
        result = second_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    #  test_3: Здесь запускается турнир между Андреем, Усэйном и Ником. Проверяем, что Ник снова финиширует последним.
    #
    def test_3(self):
        third_run = runner_and_tournament.Tournament(90, self.andrey, self.usain, self.nik)
        result = third_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

# Запуск тестов:

if __name__ == '__main__':
    unittest.main()