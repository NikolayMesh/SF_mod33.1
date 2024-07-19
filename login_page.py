import ast
from pages.base_page import BasePage
from pages.Locators_page import locators


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://b2c.passport.rt.ru')  # открытие страницы

    def button_log(self):  # поиск кнопки войти
        return self.find(locators.BUTTON_INTER)

    def button_login(self):
        return self.find(locators.BUTTON_LOGIN)

    def box_input(self):  # поиск поля ввода телефона
        return self.find(locators.BOX_INPUT)

    def box_input_send(self):  # ввод номера телефона
        self.box_input().send_keys('номер телефона ') # !!!!!!!!!!! введите свои данные

    def box_input_send_fake(self):  # ввод номера телефона не правильный
        self.box_input().send_keys('номер ') # !!!!!!!!!!! введите свои данные

    def box_input_send_mail(self):  # ввод номера телефона
        self.box_input().send_keys('почта') # !!!!!!!!!!! введите свои данные

    def box_input_send_login(self):  # ввод номера логину
        self.box_input().send_keys('логин') # !!!!!!!!!!! введите свои данные

    def box_input_pass(self):  # поиск поля ввода пароля
        return self.find(locators.INTER_PASSWORD)

    def pass_input(self):  # ввели пароль
        self.box_input_pass().send_keys('пароль') # !!!!!!!!!!! введите свои данные

    def button_mail_click(self):  # нажатие меню выбора вход по почте
        self.find(locators.BUTTON_MAIL).click()

    def button_login_click(self):  # нажатие меню выбора вход по логину
        self.find(locators.BUTTON_LOGIN).click()

    def click_Button(self):  # нажатие кнопки войти
        self.button_log().click()

    def buttonIsDisplayed(self):  # отображение кнопки на странице
        return self.button_log().is_displayed()

    def result_click(self):  # поиск подсказки на экране
        return self.find(locators.MESSAGE_NUBER)

    def message_error(self):  # неправильно введен логин или пароль
        return self.find(locators.ERROR_MESSAGE)

    @property
    def message_error_text(self):  # вывод теста ошибки
        return self.message_error().text

    def button_exit(self):  # кнопка выход в личном кабинете
        self.find(locators.BUTTON_EXIT).click()

    @property
    def result_text(self):  # вывод теста подсказки
        return self.result_click().text

    def check_color(self, elem):  # проверка цвета
        rgba = elem.value_of_css_property('color')
        r, g, b, alpha = ast.literal_eval(rgba.strip('rgba'))
        hex_value = '#%02x%02x%02x' % (r, g, b)
        return hex_value
