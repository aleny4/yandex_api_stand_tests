import configuration
import requests
import data

# создание нового пользователя
def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, # подставляем полный url
                         json=data.user_body,  # тело
                         headers=data.headers) # заголовки

# создание нового набора
def post_new_kit(kit_body, auth_token):
    headers_kit = data.headers_kit.copy()
    headers_kit["Authorization"] = "Bearer "+auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH, # подставляем полный url
                         json=kit_body,
                         headers=headers_kit)
