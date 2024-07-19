from pages.base_page import BasePage
from pages.Locators_page import locators


class RegPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://b2c.passport.rt.ru')  # открытие страницы

    def open_reg(self):
        self.find(locators.BUTTON_REGISTER).click()

    def click_button_register(self):
        self.find(locators.BUTTON_REGISTER_FIN).click()

    @property
    def message_name(self):
        return self.find(locators.MESS_NAME).text

    @property
    def message_surname(self):
        return self.find(locators.MESS_SURN).text

    @property
    def message_post(self):
        return self.find(locators.MESS_POST).text

    @property
    def message_pass(self):
        return self.find(locators.MESS_PASS).text

    @property
    def message_conpas(self):
        return self.find(locators.MESS_CONP).text
