class IncorrectVinNumber(Exception):       # IncorrectVinNumber наследует от базового класса Exception
    def __init__(self, message):
        self.message = message             # Сообщение, которое будет выводиться в консоль при выбрасывании исключения

class IncorrectCarNumbers(Exception):      # IncorrectCarNumbers наследует от базового класса Exception
    def __init__(self, message):
        self.message = message             # Сообщение, которое будет выводиться в консоль при выбрасывании исключения

class Car:                                      # Создаем класс Car
    def __init__(self, model, vin, numbers):    # Конструктор класса Car  по заданию
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(self.__vin)          # Вызов функции проверки vin
        self.__is_valid_numbers(self.__numbers)  # Вызов функции проверки numbers

    def __is_valid_vin(self, vin_number):                                 # Проверяем корректность vin_number
        if not isinstance(vin_number, int):                               # Если vin_number не является целым числом, то
            raise IncorrectVinNumber("Некорректный тип vin номер")        # вызываем обработку ошибки с сообщением
        if (vin_number < 1000000) or (vin_number > 9999999):              # Если vin_number не входит в диапозон, то
            raise IncorrectVinNumber("Неверный диапазон для vin номера")  # вызываем обработку ошибки с сообщением
        return True                                                       # Если нет ошибок, то возвращаем True

    def __is_valid_numbers(self, numbers):                                    # Проверяем корректность numbers
        if not isinstance(numbers, str):                                      # Если numbers не является строкой, то
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")  # вызываем обработку ошибки с сообщением
        if len(numbers) != 6:                                                 # Если в numbers количество чисел не 6, то
            raise IncorrectCarNumbers("Неверная длина номера")                # вызываем обработку ошибки с сообщением
        return True                                                           # Если нет ошибок, то возвращаем True



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')