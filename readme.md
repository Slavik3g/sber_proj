## Серивс для извлечения юридической информации из дерева в форматах XML и JSON.
***

### Требования к сервису:
- [X] Принятие дерева извлечений в форматах JSON и XML.
- [X] Реализация функции конвертирования деревьев в словарь.
- [X] Реализация функций нормализации деревьев. А именно: 
  1. Необходимо реализовать функцию приведения любых дат к формату ДД.ММ.ГГГГ.
  2. Необходимо написать функцию приведения любых временных сроков в следующий формат: Г_М_Н_Д, где Г - год, М - это месяц, Н - неделя, Д - день. 

### Запуск приложения
```
docker-compose up --build
```

### Endpoints

| Method | Url                                          | Description      | Headers                                         |
|:-------|:---------------------------------------------|:-----------------|:------------------------------------------------|
| POST   | http://127.0.0.1:8000/api/v1/parse_document/ | Process json/xml | Content-Type: application/json, application/xml |

### Тестовые xml и json данные находятся в папке: 
`examples/`
### Postman коллекция находится в:
`examples/sber_test.postman_collection.json`
***