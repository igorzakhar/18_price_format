# Форматирование цены

Небольшой скрипт для форматирования цен на товары. 

# Установка

Для запуска программы требуется установленный Python 3.5. 

# Как использовать

В программе используется встроенный модуль ```decimal``` с помощью которого можно записывать числа с желаемым уровнем точности. Это особенно важно  для расчетов денежных сумм.  

Модуль ```format_price``` включает в себя 2 функции:  
- ```convert_to_decimal(price)``` - функция для преобразования входящего строкового значения в экземпляр класса ```decimal.Decimal```.
- ```format_price(price)``` - функция для форматирования значения экземпляра класса ```decimal.Decimal```

#### 1. Запуск скрипта через командную строку:
```
$ python3 format_price.py <value>
```
Пример вывода при запуске через командную строку в ОС Linux(Debian):
```
$ python format_price.py 1241515.4265778
1 241 515.43
```
При запуске с невалидными данными программа выдаст сообщение об ошибке.  
Пример запуска скрипта с невалидными данными:  
```
$ python format_price.py 1241ABC.12def
Incorrect value
```
#### 2. Импортирование модуля
Пример использования:

```python
>>> from format_price import convert_to_decimal, format_price
>>> price = convert_to_decimal('123456.93333')
>>> formatted_price = format_price(price)
>>> formatted_price
'123 456.93'
```

# Запуск тестов
В репозитории находится скрипт для запуска тестов unittest ```test.py```. 
Набор тестов включает в себя следующие тесты:  
- ввод строкового представления целого числа int;
- ввод строкового представления числа с плавающей запятой float;
- конвертирование некорректного значения;
- форматирование некорректного значения;
- проверка округления  ROUND_HALF_UP (округление вверх, если цифра пять и больше);
- ввод строкового представления числа типа float с нулями после запятой.  

Пример запуска тесов в OC Linux(Debian):

```
$ python test.py -v
test_convert_invalid_value (__main__.FormatPriceTestCase) ... ok
test_format_invalid_value (__main__.FormatPriceTestCase) ... ok
test_input_float_string (__main__.FormatPriceTestCase) ... ok
test_input_integer_string (__main__.FormatPriceTestCase) ... ok
test_round_half_up (__main__.FormatPriceTestCase) ... ok
test_trailing_zeros_value (__main__.FormatPriceTestCase) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

# Цели проекта

Код написан для образовательных целей. Учебный курс для веб-разработчиков - [DEVMAN.org](https://devman.org)
