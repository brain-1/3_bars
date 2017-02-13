# Ближайшие бары

Скрипт предназначен для определения бара с максимальным и минимальным числом посадочных
мест среди баров Москвы.
А также, если ввести текущие координаты GPS (широта и долгота в градусах и долях градуса), скрипт рассчитает 
ближайший к вам бар и выведет дистанцию до него в метрах.
Для точности расчетов используется модификация [формулы гаверсинусов для антиподов](http://gis-lab.info/qa/great-circles.html) 

Для расчетов используются [актуальный список московских баров.](http://data.mos.ru/opendata/7710881420-bary)

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python bars.py # possibly requires call of python3 executive instead of just python


Download latest data file...                                                                                                                            
Done                                                                                                                                                    
Load data from data-2897-2016-11-23.json                                                                                                                
Enter your Latitude:55.95112213                                                                                                                         
Enter your Longitude:37.61650085                                                                                                                        
Biggest bar is Спорт бар «Красная машина»  Seats number  450                                                                                           
Smallest bar is БАР. СОКИ  Seats number  0                                                                                                             
Closest bar is Капитан Конрад Distance to bar- 4297  [meters]   
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
