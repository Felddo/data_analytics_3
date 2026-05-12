# Описание задачи
Интеллектуальный Telegram‑бот, который анализирует загруженные пользователем датасеты в форматах CSV и XLSX с помощью языковой модели и автоматически формирует структурированный аналитический отчёт.

### Возможности
* Приём файлов форматов .csv и .xlsx
* Автоматическая проверка корректности формата
* Анализ структуры и содержимого датасета с помощью AI‑агента
* Выполнение Python-кода для углублённого анализа данных
* Формирование структурированного аналитического отчёта
* Генерация отчёта на русском языке

### Установка
1. git clone https://github.com/Felddo/data_analytics_3
2. cd data_analytics_3
3. pip install -r requirements.txt
4. Делаем ключ на сайте https://console.groq.com/keys
5. Вставляем в файл .env свой ключ "GROQ_API_KEY==ключ"
6. Делаем токен в @BotFather
7. Вставляем его в файл bot.py в переменную TOKEN 
8. python bot.py

### Пример входных данных
```csv
model,year,price,transmission,mileage,fuelType,tax,mpg,engineSize
 5 Series,2014,11200,Automatic,67068,Diesel,125,57.6,2.0
 6 Series,2018,27000,Automatic,14827,Petrol,145,42.8,2.0
 5 Series,2016,16000,Automatic,62794,Diesel,160,51.4,3.0
 1 Series,2017,12750,Automatic,26676,Diesel,145,72.4,1.5
 7 Series,2014,14500,Automatic,39554,Diesel,160,50.4,3.0
 5 Series,2016,14900,Automatic,35309,Diesel,125,60.1,2.0
 5 Series,2017,16000,Automatic,38538,Diesel,125,60.1,2.0
 2 Series,2018,16250,Manual,10401,Petrol,145,52.3,1.5
 4 Series,2017,14250,Manual,42668,Diesel,30,62.8,2.0
 5 Series,2016,14250,Automatic,36099,Diesel,20,68.9,2.0
 X3,2017,15500,Manual,74907,Diesel,145,52.3,2.0
 1 Series,2017,11800,Manual,29840,Diesel,20,68.9,2.0
 X3,2016,15500,Automatic,77823,Diesel,125,54.3,2.0
 2 Series,2015,10500,Manual,31469,Diesel,20,68.9,2.0
```

### Пример выходных данных
1. Общая структура данных
- Размер датасета: 14 строк, 9 столбцов
- Колонки: model, year, price, transmission, mileage, fuelType, tax, mpg, engineSize
- Типы данных:
  - model: str
  - year: int64
  - price: int64
  - transmission: str
  - mileage: int64
  - fuelType: str
  - tax: int64
  - mpg: float64
  - engineSize: float64
- Дубликаты: 0

2. Ключевые статистики
- Средние значения:
  - year: 2016.29
  - price: 15028.57
  - mileage: 41998.07
  - tax: 106.43
  - mpg: 58.80
  - engineSize: 2.07
- Максимумы:
  - year: 2018
  - price: 27000
  - mileage: 77823
  - tax: 160
  - mpg: 72.40
  - engineSize: 3.00
- Минимумы:
  - year: 2014
  - price: 10500
  - mileage: 10401
  - tax: 20
  - mpg: 42.80
  - engineSize: 1.50

3. Закономерности и инсайты
- Корреляция между ценой и годом выпуска составляет 0.54, что указывает на умеренную положительную связь.
- Корреляция между ценой и пробегом составляет -0.26, что указывает на слабую отрицательную связь.
- По типам трансмиссии:
  - Automatic: средняя цена 15788.89, минимум 11200, максимум 27000
  - Manual: средняя цена 13660.00, минимум 10500, максимум 16250
