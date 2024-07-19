from selenium.webdriver.common.by import By


class locators:
    BUTTON_INTER = (By.ID, 'kc-login')  # кнопка вход
    MESSAGE_NUBER = (By.ID, 'username-meta')  # сообщение Введите номер телефона
    BUTTON_PHONE = (By.ID, 't-btn-tab-phone')  # телефон
    BUTTON_MAIL = (By.ID, 't-btn-tab-mail')  # почта
    BUTTON_LOGIN = (By.ID, 't-btn-tab-login')  # логин
    MESSAGE_MAIL = (By.ID, 'username-meta')  # сообщение Введите почту(Введите адрес, указанный при регистрации)
    MESSAGE_PHONE = (By.ID, 'username-meta')  # сообщение Введите логин(Введите логин, указанный при регистрации)
    BOX_INPUT = (By.ID, 'username')  # поле ввода телефона
    INTER_LOGIN = (By.ID, 'username')  # поле ввода логина
    INTER_MAIL = (By.ID, 'username')  # поле ввода почты
    INTER_PASSWORD = (By.ID, 'password')  # поле ввода пароля
    FORGOT_PASSWORD = (By.ID, 'forgot_password')  # забыл пароль
    BUTTON_REGISTER = (By.ID, 'kc-register')  # кнопка зарегистрироваться
    BUTTON_CONTINUE = (By.ID, 'reset')  # кнопка продолжить
    BUTTON_BACK = (By.ID, 'reset-back')  # кнопка вернуться назад
    BUTTON_EXIT = (By.ID, 'logout-btn')  # кнопка выход
    ERROR_MESSAGE = (By.ID, 'form-error-message')  # сообщение об ошибке
    POINT_SMS = (By.XPATH, '//*[@id="sms-reset-type"]/span/span[3]/span[1]')  # точка смс
    POINT_EMAIL = (By.XPATH, '//*[@id="email-reset-type"]/span/span[3]/span[1]')  # точка почта
    BUTTON_CONTINUE_2 = (By.ID, 'reset-form-submit')  # кнопка продолжить после выбора смс или телефон
    NEW_PASS = (By.ID, 'password-new')  # поле новый пароль
    NEW_PASS_CONFIRM = (By.ID, 'password-confirm')  # поле новый пароль
    PASSWORD_FAKE = (By.ID, 'password-new-meta')  #""" # Пароль должен содержать хотя бы одну заглавную букву
                                                        # #Длина пароля должна быть не менее 8 символов
                                                        #Пароль должен содержать только латинские буквы
                                                         #Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"""
    BUTTON_SAVE_PASS = (By.ID, 't-btn-reset-pass')  # кнопка сохранения пароля
    FILD_NAME = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input') # поле имя в форме регистрации
    BUTTON_REGISTER_FIN = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button') #кнопка завершения регистрации
    MESS_NAME = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span') # ошибка ввдете имя
    MESS_SURN = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span') # ошибка ввдете фамилию
    MESS_POST = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span') # ошибка ввдете почту
    MESS_PASS = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span') # ошибка ввдете пароль
    MESS_CONP = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[2]/span')# ошибка ввдете пароль
