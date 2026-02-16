"""ExamTaskC3. На вход подаются сведения о клиентах фитнес-центра. В первой строке
указывается целое число N, а каждая из последующих N строк имеет формат
<Продолжительность занятий (в часах)> <Код клиента> <Год> <Номер месяца>
Все данные целочисленные. Значение года лежит в диапазоне от 2000 до 2010, код клиента —
в диапазоне 10–99, продолжительность занятий — в диапазоне 1–30. Найти строку исходных
данных с минимальной продолжительностью занятий. Вывести эту продолжительность, а
также соответствующие ей год и номер месяца (в указанном порядке). Если имеется несколько
строк с минимальной продолжительностью, то вывести данные, соответствующие самой
ранней дате."""
class FitnessRecord:
    def __init__(self, duration, client_code, year, month):
        self.duration = duration
        self.client_code = client_code
        self.year = year
        self.month = month

    def get_date_value(self): #Получить числовое значение даты для сравнения
        return self.year * 12 + self.month


class FitnessDataProcessor: #Класс для обработки данных фитнес-центра

    def __init__(self):
        self.records = []

    def read_data(self):

        # Ввод количества записей с проверкой
        while True:
            try:
                n = int(input("\nСколько записей ввести? "))
                if n > 0:
                    break
                else:
                    print("Ошибка: введите положительное число")
            except ValueError:
                print("Ошибка: введите целое число")

        print(f"\nВведите {n} записей в формате: <часы> <код> <год> <месяц>")
        print("Пример: 15 42 2005 3")


        # Чтение записей
        for i in range(n):
            while True:
                try:
                    line = input(f"Запись {i + 1}: ").strip()
                    parts = line.split()

                    if len(parts) != 4:
                        print("Ошибка: нужно ввести 4 числа через пробел")
                        continue

                    duration = int(parts[0])
                    client_code = int(parts[1])
                    year = int(parts[2])
                    month = int(parts[3])

                    # Проверка диапазонов
                    if not (1 <= duration <= 30):
                        print(
                            "Ошибка: продолжительность должна быть от 1 до 30")
                        continue
                    if not (10 <= client_code <= 99):
                        print("Ошибка: код клиента должен быть от 10 до 99")
                        continue
                    if not (2000 <= year <= 2010):
                        print("Ошибка: год должен быть от 2000 до 2010")
                        continue
                    if not (1 <= month <= 12):
                        print("Ошибка: месяц должен быть от 1 до 12")
                        continue

                    # Если все проверки пройдены
                    record = FitnessRecord(duration, client_code, year, month)
                    self.records.append(record)
                    break

                except ValueError:
                    print("Ошибка: введите целые числа")

    def find_min_duration_record(self): #Находит запись с минимальной продолжительностью
        if not self.records:
            return None

        # Находим минимальную продолжительность
        min_duration = min(record.duration for record in self.records)
        print(f"\nМинимальная продолжительность: {min_duration} часов")

        # Отбираем все записи с минимальной продолжительностью
        min_records = [r for r in self.records if r.duration == min_duration]

        print(
            f"Найдено записей с такой продолжительностью: {len(min_records)}")

        # Если несколько записей, показываем их все
        if len(min_records) > 1:
            print("\nЗаписи с минимальной продолжительностью:")
            for r in min_records:
                date_value = r.get_date_value()
                print(
                    f"  {r.duration} ч, код {r.client_code}, {r.year} год, месяц {r.month} (дата в числах: {date_value})")

        # Если только одна запись, возвращаем её
        if len(min_records) == 1:
            return min_records[0]

        # Если несколько, выбираем самую раннюю по дате
        earliest = min(min_records, key=lambda r: r.get_date_value())
        print(
            f"\nВыбрана самая ранняя дата: {earliest.year} год, месяц {earliest.month}")
        return earliest

    def print_result(self):
        result = self.find_min_duration_record()


        print("РЕЗУЛЬТАТ:")


        if result:
            print(f"\n Найдена запись с минимальной продолжительностью:")
            print(f"   Продолжительность: {result.duration} часов")
            print(f"   Год: {result.year}")
            print(f"   Месяц: {result.month}")
            print(
                f"\nИтоговая строка: {result.duration} {result.year} {result.month}")
        else:
            print("\n Нет данных для обработки")



def main():
    processor = FitnessDataProcessor()
    processor.read_data()
    processor.print_result()

    print("\nНажмите Enter для выхода...")
    input()

if __name__ == "__main__":
    main()