import json

import requests


class IMEIChecker:
    def __init__(self, sandbox_api, service_id, base_url):
        self.sandbox_api = sandbox_api
        self.service_id = service_id
        self.base_url = base_url

    def request_maker(self, imei_number):
        imei_number = str(imei_number)
        if self.imei_validation(imei_number):
            headers = {
                'Authorization': 'Bearer ' + self.sandbox_api,
                'Content-Type': 'application/json'
            }

            body = json.dumps({
                "deviceId": imei_number,
                "serviceId": self.service_id
            })

            response = requests.post(self.base_url, headers=headers, data=body)
            return response.json()["properties"]
        else:
            return {"error": "некорректный IMEI"}

    def imei_validation(self, imei_number):
        """
        Проверка IMEI на валидность.
        :param imei_number:
        1. Цифры проверяемой последовательности нумеруются справа налево.
        2. Цифры, оказавшиеся на нечётных местах, остаются без изменений.
        3. Цифры, стоящие на чётных местах, умножаются на 2.
        4. Если в результате такого умножения возникает число больше 9, оно заменяется суммой цифр получившегося
        произведения — однозначным числом, т. е. цифрой.
        5. Все полученные в результате преобразования цифры складываются.
        Если сумма кратна 10, то исходные данные верны.
        :return:
        1. True в случае корректного IMEI
        2. False в случае некорректного IMEI
        """
        if len(imei_number) != 15:
            return False

        reversed_imei_number = imei_number[::-1]
        only_odd = reversed_imei_number[0::2]
        only_even = reversed_imei_number[1::2]
        new_even_number = ""

        for i in only_even:
            if (i_mult := (int(i) * 2)) > 9:
                i_sum = int(str(i_mult)[0]) + int(str(i_mult)[1])
                i = str(i_sum)
            else:
                i_mult = int(i) * 2
                i = str(i_mult)
            new_even_number += i
        processed_number = new_even_number + only_odd
        total_sum = 0
        for i in processed_number:
            total_sum += int(i)
        if total_sum % 10:
            return False
        else:
            return True
