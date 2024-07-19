from pages.new_pas_page import NewPassPage
import time


def test_button_forgot_pas(browser):
    NewPass_Page = NewPassPage(browser)
    NewPass_Page.open()
    NewPass_Page.button_forgot_pass_click()
    NewPass_Page.box_input_send()
    time.sleep(30)  # ввод капчи
    NewPass_Page.button_continue()
    NewPass_Page.point_sms()
    NewPass_Page.button_next()
    time.sleep(30)  # ввод кода
    NewPass_Page.inter_pass_new()
    NewPass_Page.inter_pass_new_confirm()
    NewPass_Page.button_save_pass()







def test_button_forgot_pas_fake(browser): # негативная проверка на пустое (неверное) поле капчи или неправильный  номер
    NewPass_Page = NewPassPage(browser)
    NewPass_Page.open()
    NewPass_Page.button_forgot_pass_click()
    NewPass_Page.box_input_send()
    NewPass_Page.button_continue()
    assert 'Неверный логин или текст с картинки' == NewPass_Page.error_message
