# Инструкция по запуску

## 1. Установить зависимости

Скрипт использует библиотеку **dnspython**.

Через `pip`:
```python
pip install dnspython
```
---
## 2. Изменить список email-адресов

Внутри файла есть список:

```python
emails = [
    "user1@gmail.com",
    "test@yahoo.com",
    ...,
    ...
    ]
```

Можно заменить его на свой.

---
## 3. Запустить скрипт

Если файл называется, например, **check_mail.py**, то запуск:
```python
python check_mail.py
```

Пример вывода результата в терминале:
```python
admin@example.com: домен валиден
nobody@github.io: MX-записи отсутствуют или некорректны
test@wikipedia.org: домен валиден
```