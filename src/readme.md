# 🍽️ Recipes API

## 📌 Описание

REST API сервис для хранения и управления рецептами.

Позволяет:

* создавать рецепты
* получать список рецептов
* просматривать детальную информацию

---

## ⚙️ Технологии

* FastAPI
* Async SQLAlchemy
* SQLite
* Pydantic
* Pytest

---

## 🚀 Запуск проекта

### Установка зависимостей

```bash
pip install fastapi uvicorn sqlalchemy aiosqlite pytest httpx
```

---

### Запуск сервера

```bash
uvicorn main:app --reload
```

---

### Документация API

После запуска доступна по адресу:

```
http://127.0.0.1:8000/docs
```

---

## 🔌 Эндпоинты

### GET /recipes

Получить список рецептов

#### Сортировка:

* по `views` (убывание)
* затем по `cooking_time` (возрастание)

#### Пример ответа:

```json
[
  {
    "id": 1,
    "title": "Pasta",
    "cooking_time": 15,
    "views": 10
  }
]
```

---

### GET /recipes/{id}

Получить рецепт по ID

#### Особенность:

* при каждом запросе `views += 1`

#### Ответ:

```json
{
  "id": 1,
  "title": "Pasta",
  "cooking_time": 15,
  "views": 11,
  "ingredients": "pasta",
  "description": "cook it"
}
```

---

### POST /recipes

Создать рецепт

#### Запрос:

```json
{
  "title": "Soup",
  "cooking_time": 30,
  "ingredients": "water",
  "description": "boil"
}
```

---

## 🗄️ Структура проекта

```
app/
 ├── main.py
 ├── database.py
 ├── models.py
 ├── schemas.py
 └── crud.py
```

---

## 🧪 Запуск тестов

```bash
pytest -v
```

---

## 📈 Бизнес-логика

* Новые рецепты имеют `views = 0`
* При просмотре рецепта:

  ```
  views += 1
  ```
* Сортировка:

  ```
  ORDER BY views DESC, cooking_time ASC
  ```

---
