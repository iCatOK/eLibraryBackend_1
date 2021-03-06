# eLibraryBackend_1
Первый этап работы над бэкендом электронной библиотеки хакатона BreakPoint.

## API Reference

+ /auth/registration/ (POST) - регистрация нового пользователя (доступно только библиотекарям). Body:
```
{
  "username": "username",
  "full_name": "Иван Иванов",
  "password1": "password123",
  "password2": "password123"
}
```
+ /auth/user/ (GET, PUT) - профиль пользователя. Изменяемые:  full_name, branch. Body:
```
{
    "id": 2,
    "username": "test1",
    "is_librarian": false,
    "full_name": "test1",
    "status": "NB",
    "branch": 1
}
```
+ /api/users/ (GET) - возвращает всех пользователей (доступно только библиотекарям)
+ /api/users/{id} (GET) - возвращает пользователя по id (доступно только библиотекарям)
+ /api/books/ (GET, POST) - возвращает все книги, создает новую книгу (доступ создания книги только для библиотекарей). Body:
```
{
    "author": "",
    "name": "",
    "genre": 1,
    "owner": 1
}
```
+ /api/books/{id} (GET, PUT) - возвращает книгу по id, обновляет книгу (доступ обновления книги только для библиотекарей). Body:
```
{
    "id": 1,
    "author": "Kepef",
    "name": "Kepef",
    "genre": 1,
    "owner": null
}
```
+ /api/branches/ (GET, POST) - возвращает все филиалы, создает новый филиал (доступ только для библиотекарей). Body:
```
{
    "name": "",
    "address": ""
}
```
+ /api/branches/{id} (GET, PUT) - возвращает филиал по id, обновляет филиал (доступ только для библиотекарей). Body:
```
{
    "name": "",
    "address": ""
}
```
+ /api/genres/ (GET, POST) - возвращает все жанры, создает новый жанр (доступ только для библиотекарей). Body:
```
{
    "name": ""
}
```
+ /api/genres/{id} (GET, PUT) - возвращает жанр по id, обновляет жанр (доступ только для библиотекарей). Body:
```
{
    "name": ""
}
```

