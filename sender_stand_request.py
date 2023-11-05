import configuration
import requests
import data

# создание нового пользователя
def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, # подставляем полный url
                         json=data.user_body,  # тело
                         headers=data.headers) # заголовки

# создание нового набора
def post_new_client_kit(kit_name, auth_token):
    kit_body = data.kit_body.copy()
    kit_body["name"] = kit_name
    headers_kit = data.headers_kit.copy()
    headers_kit["Authorization"] = "Bearer "+auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH, # подставляем полный url
                         json=kit_body,
                         headers=headers_kit)

# создание набора с путсым телом
def post_new_client_kit_empty_body(auth_token):
    kit_body = data.empty_body.copy()
    headers_kit = data.headers_kit.copy()
    headers_kit["Authorization"] = "Bearer "+auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH, # подставляем полный url
                         json=kit_body,
                         headers=headers_kit)
