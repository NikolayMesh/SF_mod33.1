from pages.login_page import LoginPage


def test_button_exist(browser):  # проверка наличия кнопки на странице
    login_page = LoginPage(browser)
    login_page.open()
    assert login_page.buttonIsDisplayed()


def test_button_clicked(browser):  # вкладка телефон пустое поле нажатие кнопки вход
    login_page = LoginPage(browser)
    login_page.open()
    login_page.click_Button()
    assert 'Введите номер телефона' == login_page.result_text


def test_button_mail_clicked(browser):  # вкладка почта пустое поле нажатие кнопки вход
    login_page = LoginPage(browser)
    login_page.open()
    login_page.button_mail_click()
    login_page.click_Button()
    assert 'Введите адрес, указанный при регистрации' == login_page.result_text


def test_button_login_clicked(browser):  # вкладка логин пустое поле нажатие кнопки вход
    login_page = LoginPage(browser)
    login_page.open()
    login_page.button_login_click()
    login_page.click_Button()
    assert 'Введите логин, указанный при регистрации' == login_page.result_text


def test_button_clicked_enter(browser):  # вкладка телефон вход по телефону
    login_page = LoginPage(browser)
    login_page.open()
    login_page.box_input_send()
    login_page.pass_input()
    login_page.click_Button()
    login_page.button_exit()


def test_button_clicked_enter_mail(browser):  # вкладка телефон вход по почте
    login_page = LoginPage(browser)
    login_page.open()
    login_page.button_mail_click()
    login_page.box_input_send_mail()
    login_page.pass_input()
    login_page.click_Button()
    login_page.button_exit()


def test_button_clicked_enter_login(browser):  # вкладка телефон вход по логину
    login_page = LoginPage(browser)
    login_page.open()
    login_page.button_login_click()
    login_page.box_input_send_login()
    login_page.pass_input()
    login_page.click_Button()
    login_page.button_exit()


def test_button_login_color(browser):  # проверка активности кнопки логин
    login_page = LoginPage(browser)
    login_page.open()
    login_page.button_login_click()
    assert login_page.check_color(login_page.button_login()) == '#ff4f12'


def test_button_clicked_enter_fake_nom(browser):  # вкладка телефон вход по телефону Неверный логин или пароль
    login_page = LoginPage(browser)
    login_page.open()
    login_page.box_input_send_fake()
    login_page.pass_input()
    login_page.click_Button()
    assert 'Неверный логин или пароль' == login_page.message_error_text
