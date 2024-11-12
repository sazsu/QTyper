<div align=center>
  <h1 >QTyper</h1>
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/>
  <img src="https://img.shields.io/badge/PyQt-2cde85?style=for-the-badge&&logo=qt&logoColor=white"/>
  <img src="https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/license-GPLv3-blue?style=for-the-badge"/>
</div>

## О проекте

QTyper - это приложение с графическим интерфейсом для тестирования скорости и точности печати, разработанное с использованием библиотеки [PyQt](https://doc.qt.io/qtforpython-6/). Идея проекта вдохновлена веб-сайтом [monkeytype.com](https://monkeytype.com/).

Данное приложение создано в качестве проекта QT на курсе основ промышленного программирования в Яндекс Лицее.

## Функциональность

- Измерение скорости печати ([WPM](## "Words Per Minute - Слова В Минуту"))
- Измерение точности печати
- Выбор различных режимов тестирования
- Сохранение статистики в базу данных
- Отображение статистики на основе пройденных тестов
- Смена цвета интерфейса
- Экспорт данных из базы данных в формате CSV

## Пререквизиты

- [git](https://git-scm.com/downloads)
- [python](https://www.python.org/downloads/) версии 3.8 и выше

## Быстрый старт

1. Клонируйте репозиторий:
```sh
git clone https://github.com/sazsu/QTyper.git
```
2. Перейдите в директорию проекта:
```sh
cd QTyper
```
3. Создайте виртуальное окружение:
```sh
python -m venv your_venv_name
```
4. Установите зависимости:
```sh
python -m pip install -r requirements.txt
```
5. Запустите проект:
```sh
python -m app
```

## Технологии
- Python
- PyQt6
- СУБД SQLite
- Matplotlib

## Признания
[Английские](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Contemporary_fiction) и [русские](https://en.wiktionary.org/wiki/Appendix:Russian_Frequency_lists/1-1000) слова для генерации тестов были выбраны из списка наиболее часто употребляемых слов по мнению [Wiktionary](https://www.wiktionary.org/).

## Лицензия
Данный проект лицензирован в соответствии с условиями лицензии GNU General Public License v3.0, ознакомиться с ней можно [здесь](https://www.gnu.org/licenses/gpl-3.0.en.html) или в файле LICENSE.
