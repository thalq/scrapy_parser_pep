# Парсер PEP документации на Python (Scrapy).

[![Scrapy](https://camo.githubusercontent.com/40d00cefb120a829517e503658aaf6c987d5f9cc6be5e2e35fb20bd63bdbceb5/68747470733a2f2f7363726170792e6f72672f696d672f7363726170796c6f676f2e706e67)](https://scrapy.org/)


## Технологии:
- Python
- Parser
- Scrapy

___
## Описание проекта:
#### Парсер [документов PEP](https://www.python.org/dev/peps/) на базе фреймворка Scrapy, c возможностью сохранения работы парсера в формат .csv - парсер cобирает все данные в файл (Номер PEP, Название, Статус PEP), также при работе автоматически формируется таблица с количеством PEP в каждом статусе, и общим количеством PEP.
___

## Запуск проекта:

#### Склонировать репозиторий:
```
git clone git@github.com:thalq/scrapy_parser_pep.git
```


#### Установить и активировать виртуальное окружение
```
python -m venv venv
source env/bin/activate
```

#### Обновить менеджер пакетов PIP
```
python -m pip install --upgrade pip
```

#### Requirements.txt
```
pip install -r requirements.txt
```

## Запустить парсер:
```
scrapy crawl pep
```

## Автор
[Tanya Khalkvist](https://github.com/thalq) 
