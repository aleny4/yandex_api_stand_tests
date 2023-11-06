# импорт необходимых пакетов
import sender_stand_request
import data


# создание пользователя с получением токена
def get_token():
    user_response = sender_stand_request.post_new_user(user_body)
    return user_response.json()["authToken"]

# получение тела запроса в создании набора
def get_kit_body(name): 
    kit_body = data.kit_body.copy()
    kit_body['name'] = name
    return kit_body

# пустое тело запроса в создании набора
def get_empty_kit_body():  
    kit_body = data.kit_body.copy()
    # удаление параметра "name" из запроса
    kit_body.pop('name')
    return kit_body


# позитивные проверки
def positive_assert(name):
    token = get_token()
    kit_body = get_kit_body(name)
    #вызов функции создания набора
    response = sender_stand_request.post_new_kit(kit_body, token)
    # проверяем, что код ответа 201
    assert response.status_code == 201
    assert response.json()['name'] == name

# негативные проверки
def negative_assert_code_400(name):
    token = get_token()
    kit_body = get_kit_body(name)
    #вызов функции создания набора
    response = sender_stand_request.post_new_kit(kit_body, token)
    # проверяем, что код ответа 400
    assert response.status_code == 400
    assert response.json()["name"] == name


# Тест 1. Допустимое количество символов (1)
def test_create_kit_1_letter_in_name_get_positive_response():
    positive_assert("a")

# Тест 2. Допустимое количество символов (511)
def test_create_kit_511_letter_in_name_get_positive_response():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Количество символов меньше допустимого (0)
def test_create_kit_0_letter_in_name_get_negative_response():
    negative_assert_code_400("")

# Тест 4. Количество символов больше допустимого (512)
def test_create_kit_512_letter_in_name_get_negative_response():
    negative_assert_code_400(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Разрешены английские буквы
def test_create_kit_english_letter_in_name_get_positive_response():
    positive_assert("QWErty")

# Тест 6. Разрешены русские буквы
def test_create_kit_russian_letter_in_name_get_positive_response():
    positive_assert("Мария")

# Тест 7. Разрешены спецсимволы
def test_create_kit_special_symbol_in_name_get_positive_response():
    positive_assert("\"№%@\",")

# Тест 8. Разрешены пробелы
def test_create_kit_whitespace_in_name_get_positive_response():
    positive_assert(" Человек и КО ")

# Тест 9. Разрешены цифры
def test_create_kit_numbers_in_name_get_positive_response():
    positive_assert("123")

# Тест 10. Параметр не передан в запросе
def test_create_kit_no_name_get_negative_assert():
    token = get_token()
    kit_body = get_empty_kit_body()
    response = sender_stand_request.post_new_kit(kit_body, token)
    # проверяем, что код ответа 400
    assert response.status_code == 400

# Тест 11. Передан другой тип параметра (число)
def test_create_kit_number_type_name_get_negative_response():
    negative_assert_code_400(123)
