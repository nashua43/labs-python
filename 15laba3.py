"""ExamTaskC15. На вход подаются сведения о клиентах фитнес-центра. В первой строке
указывается код K одного из клиентов, во второй строке — целое число N, а каждая из
последующих N строк имеет формат
<Код клиента> <Продолжительность занятий (в часах)> <Год> <Номер месяца>
Все данные целочисленные. Значение года лежит в диапазоне от 2000 до 2010, код клиента —
в диапазоне 10–99, продолжительность занятий — в диапазоне 1−30. Для каждого года, в
котором клиент с кодом K посещал центр, определить месяц, в котором продолжительность
занятий данного клиента была наибольшей для данного года (если таких месяцев несколько,
то выбирать месяц с наименьшим номером). Сведения о каждом годе выводить на новой
строке в следующем порядке: наибольшая продолжительность занятий в году, год, номер
месяца. Упорядочивать сведения по убыванию продолжительности занятий, а при равной
продолжительности — по возрастанию номера года. Если данные о клиенте с кодом K
отсутствуют, то вывести строку «Нет данных»."""



class FitnessRecord: #Класс для хранения записи о посещении фитнес-центра

    def __init__(self, client_code, duration, year, month):
        self.client_code = client_code
        self.duration = duration
        self.year = year
        self.month = month


class YearStats: #Класс для хранения статистики по году для конкретного клиента

    def __init__(self, year):
        self.year = year
        self.max_duration = -1
        self.best_month = None

    def add_record(self, month, duration):
        if self.max_duration == -1 or duration > self.max_duration:
            self.max_duration = duration
            self.best_month = month
        elif duration == self.max_duration and month < self.best_month:
            self.best_month = month

    def __str__(self):
        return f"{self.max_duration} {self.year} {self.best_month}"


class FitnessDataProcessor:

    def __init__(self):
        self.records = []
        self.target_client = None
        self.years_stats = {}

    def read_data(self):
        print("\n" + "=" * 50)
        print("ПОИСК ЛУЧШЕГО МЕСЯЦА ДЛЯ КЛИЕНТА")
        print("=" * 50)

        # Ввод кода клиента
        while True:
            try:
                self.target_client = int(
                    input("\nКод клиента для поиска (10-99): "))
                if 10 <= self.target_client <= 99:
                    break
                print("Ошибка: код должен быть от 10 до 99")
            except ValueError:
                print("Ошибка: введите число")

        # Ввод количества записей
        while True:
            try:
                n = int(input("Сколько записей? "))
                if n > 0:
                    break
                print("Ошибка: введите положительное число")
            except ValueError:
                print("Ошибка: введите число")

        print(f"\nВведите {n} записей: <код> <часы> <год> <месяц>")
        print("Пример: 42 5 2005 3")

        # Чтение записей
        for i in range(n):
            while True:
                try:
                    line = input(f"Запись {i + 1}: ").strip()
                    if not line:
                        print("Строка пустая, повторите")
                        continue

                    parts = line.split()
                    if len(parts) != 4:
                        print("Нужно 4 числа через пробел")
                        continue

                    client_code, duration, year, month = map(int, parts)

                    # Проверка диапазонов
                    if client_code < 10 or client_code > 99:
                        print("Код клиента должен быть 10-99")
                        continue
                    if duration < 1 or duration > 30:
                        print("Часы должны быть 1-30")
                        continue
                    if year < 2000 or year > 2010:
                        print("Год должен быть 2000-2010")
                        continue
                    if month < 1 or month > 12:
                        print("Месяц должен быть 1-12")
                        continue

                    # Создаем запись
                    record = FitnessRecord(client_code, duration, year, month)
                    self.records.append(record)
                    print(" Запись добавлена")
                    break

                except ValueError:
                    print("Ошибка: введите 4 целых числа")
                except Exception as e:
                    print(f"Ошибка: {e}")

        print("\n Ввод данных завершен")

    def process_data(self): #Обработка данных для целевого клиента
        self.years_stats = {}

        for record in self.records:
            if record.client_code == self.target_client:
                if record.year not in self.years_stats:
                    self.years_stats[record.year] = YearStats(record.year)
                self.years_stats[record.year].add_record(record.month, record.duration)

    def print_results(self):
        print("РЕЗУЛЬТАТЫ")

        if not self.years_stats:
            print("\nНет данных")
            return

        # Собираем результаты
        results = []
        for year, stats in self.years_stats.items():
            if stats.best_month is not None:
                results.append((stats.max_duration, year, stats.best_month))

        # Сортировка по убыванию продолжительности, при равенстве - по возрастанию года
        for i in range(len(results)):
            for j in range(i + 1, len(results)):
                if results[i][0] < results[j][0]:  # По убыванию продолжительности
                    results[i], results[j] = results[j], results[i]
                elif results[i][0] == results[j][0] and results[i][1] > results[j][1]:  # По возрастанию года
                    results[i], results[j] = results[j], results[i]

        # Выводим в формате: продолжительность год месяц
        print()
        for duration, year, month in results:
            print(f"{duration} {year} {month}")


def main():
    processor = FitnessDataProcessor()
    processor.read_data()
    processor.process_data()
    processor.print_results()

    print("\nНажмите Enter для выхода...")
    input()

if __name__ == "__main__":
    main()