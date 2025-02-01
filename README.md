<h3>Бэкенд-система для проверки IMEI устройств, которая интегрирована с Telegram-ботом и предоставляяет API для внешних запросов</h3>

<h4>Функционал.</h4>
<h4>Доступ.</h4>
<ul>
  <li>Белый список пользователей для Telegram</li>
  
  ![Снимок экрана 2025-02-01 074627](https://github.com/user-attachments/assets/9853e5d2-297c-48b9-8b39-e7e5f1de1213)

  <li>Авторизацию по токену для доступа к API.</li>
  
  ![Снимок экрана 2025-02-01 074706](https://github.com/user-attachments/assets/1a337d99-2048-4768-804e-ccc008bfc50e)
  
</ul>
<h4>Telegram-бот.</h4>
<ul>
  <li>Пользователь отправляет боту IMEI</li>
  
  ![Снимок экрана 2025-02-01 074758](https://github.com/user-attachments/assets/28df971f-c170-4477-8ee1-27c738e913e2)<br> --
  ![Снимок экрана 2025-02-01 074807](https://github.com/user-attachments/assets/cd00d6d9-0bb5-4ccc-84cc-3038dced1366)<br> --
  ![Снимок экрана 2025-02-01 074818](https://github.com/user-attachments/assets/9cd1164e-4b14-4dc9-acc2-1d7595f2ed55)

  <li>Бот проверяет IMEI на валидность и отправляет в ответ информацию о IMEI</li>
  
  ![Снимок экрана 2025-02-01 074828](https://github.com/user-attachments/assets/fe962fc7-f183-40bb-8473-2aa849f7b2ff)

  
</ul>
<h4>Запросы API</h4>
<h4>Параметры запроса:</h4>
<ul>
  <li>imei (строка, обязательный) — IMEI устройства.</li>
  <li>token (строка, обязательный) — токен авторизации.</li>
  
  ![Снимок экрана 2025-02-01 075240](https://github.com/user-attachments/assets/b401c47e-b382-49cf-9cb0-94a8ea831e78)

</ul>
<h4>Ответ:JSON с информацией о IMEI.</h4>

![Снимок экрана 2025-02-01 075206](https://github.com/user-attachments/assets/9eb18d74-d416-4e15-9f17-81dfb3547781)

