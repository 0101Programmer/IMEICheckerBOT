import requests
import json
from requests.auth import HTTPBasicAuth

# Белый лист пользователей (должен содержать id пользователей телеграм, которые могут пользоваться ботом)
WHITE_USES_LIST = [""]
# Токен API Sandbox
API_SANDBOX = ""
# Токен API бота
API_BOT = ""
# Service_id для получения только успешных результатов по IMEI
SERVICE_ID = 12
# Ссылка для получения результатов по IMEI
BASE_URL = 'https://api.imeicheck.net/v1/checks'
