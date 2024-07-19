from pages.base_page import BasePage
from pages.Locators_page import locators


class NewPassPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://b2c.passport.rt.ru')  # открытие страницы

    def button_forgot_pass_click(self):
        self.find(locators.FORGOT_PASSWORD).click()

    def button_continue(self):
        self.find(locators.BUTTON_CONTINUE).click()

    def box_input(self):  # поиск поля ввода телефона
        return self.find(locators.BOX_INPUT)

    def box_input_send(self):  # ввод номера телефона
        self.box_input().send_keys('номер телефона') # !!!!!!!!!!! введите свои данные

    def point_sms(self): # выбор способа востановления по смс
        self.find(locators.POINT_SMS).click()

    def point_email(self): # выбор способа востановления по почте
        self.find(locators.POINT_EMAIL).click()

    def button_next(self): # кнопка дальше
        self.find(locators.BUTTON_CONTINUE_2).click()

    @property # сообщение об ошибке вврода капчи
    def error_message(self):
        return self.find(locators.ERROR_MESSAGE).text

    def fild_password(self): # поле ввода нового пароля
        self.find(locators.NEW_PASS)

    def fild_password_confirm(self):  # поле ввода подтврждения
        self.find(locators.NEW_PASS_CONFIRM)

    def inter_pass_new(self):  # ввод нового пароля
        self.fild_password().send_keys('пароль')  # !!!!!!!!!!! введите свои данные

    def inter_pass_new_confirm(self):  # ввод нового пароля
        self.fild_password_confirm().send_keys('пароль')  # !!!!!!!!!!! введите свои данные

    def button_save_pass(self):
        self.find(locators.BUTTON_SAVE_PASS).click()