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
Student_ID,Age,Gender,Academic_Level,Country,Avg_Daily_Usage_Hours,Most_Used_Platform,Affects_Academic_Performance,Sleep_Hours_Per_Night,Mental_Health_Score,Overall_Impact
232,21,Male,Undergraduate,Other,4.0,Facebook,No,6.7,6.8,Neutral
564,23,Female,Undergraduate,Other,1.6,LinkedIn,No,8.6,7.6,Positive
788,22,Male,Graduate,Canada,4.6,Instagram,No,6.7,7.0,Neutral
686,18,Male,Undergraduate,Other,7.0,Snapchat,Yes,5.4,5.3,Negative
608,24,Female,High School,Other,7.5,Facebook,Yes,5.0,4.4,Negative
370,19,Female,High School,Other,4.1,Twitter,Yes,6.8,6.8,Neutral
862,22,Female,Graduate,Other,8.0,Instagram,Yes,5.2,5.3,Negative
520,21,Female,Graduate,Other,6.0,Facebook,Yes,5.7,4.7,Negative
703,24,Male,Undergraduate,USA,4.7,YouTube,No,7.0,6.2,Neutral
33,19,Male,High School,Other,3.6,TikTok,No,8.1,8.6,Positive
519,18,Male,Graduate,Other,4.1,LinkedIn,No,7.3,6.8,Neutral
```

### Пример выходных данных
1. Общая структура данных
- Размер датасета: 11 строк, 11 столбцов
- Колонки: Student_ID, Age, Gender, Academic_Level, Country, Avg_Daily_Usage_Hours, Most_Used_Platform, Affects_Academic_Performance, Sleep_Hours_Per_Night, Mental_Health_Score, Overall_Impact
- Типы данных:
  - Student_ID: int64
  - Age: int64
  - Gender: object
  - Academic_Level: object
  - Country: object
  - Avg_Daily_Usage_Hours: float64
  - Most_Used_Platform: object
  - Affects_Academic_Performance: object
  - Sleep_Hours_Per_Night: float64
  - Mental_Health_Score: float64
  - Overall_Impact: object
- Дубликаты: 0
2. Ключевые статистики
- Средние значения:
  - Student_ID: 535.000000
  - Age: 21.000000
  - Avg_Daily_Usage_Hours: 5.018182
  - Sleep_Hours_Per_Night: 6.590909
  - Mental_Health_Score: 6.318182
- Максимумы:
  - Student_ID: 862.0
  - Age: 24.0
  - Avg_Daily_Usage_Hours: 8.0
  - Sleep_Hours_Per_Night: 8.6
  - Mental_Health_Score: 8.6
- Минимумы:
  - Student_ID: 33.0
  - Age: 18.0
  - Avg_Daily_Usage_Hours: 1.6
  - Sleep_Hours_Per_Night: 5.0
  - Mental_Health_Score: 4.4
3. Закономерности и инсайты
- Корреляционная матрица показывает сильную отрицательную корреляцию между Mental_Health_Score и Avg_Daily_Usage_Hours ( -0.842280 ), что может указывать на то, что увеличение времени, проведенного в социальных сетях, негативно влияет на психическое здоровье.
- Также наблюдается сильная положительная корреляция между Sleep_Hours_Per_Night и Mental_Health_Score ( 0.910571 ), что подтверждает важность достаточного сна для психического благополучия.
- Возраст и использование социальных сетей имеют умеренную корреляцию, что может указывать на изменение поведения с возрастом.
