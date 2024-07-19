from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.reg_page import RegPage
import time
import pytest


@pytest.mark.parametrize(
    'params',
    [
        ('123', 'Иванов'),
        ('Ю', 'Иванов'),
        ('Ю-Хунь', 'Иванов'),
        ('Name', 'Иванов'),
        ('Итвчнмыстклчнасдкшбдыоьтнмякудв', 'Иванов'),
        ('Ая в', 'Иванов')
    ]
)
def test_new_reg(params):
    name, surname = params
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru')
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input').send_keys(name)
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input').send_keys(surname)
    time.sleep(2)
    error_text = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span').text
    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' == error_text


@pytest.mark.parametrize(
    'params',
    [
        pytest.param(('Иван', '123'), id='Иван, 123'),
        pytest.param(('Иван', 'Ю'), id='Иван, Ю'),
        pytest.param(('Иван', 'Ю-Хунь'), id='Иван, Ю-Хунь'),
        pytest.param(('Иван', 'Surname'), id='Иван, Surname'),
        pytest.param(('Иван', 'Итвчнмыстклчнасдкшбдыоьтнмякудв'), id='Иван, Итвчнмыстклчнасдкшбдыоьтнмякудв'),
        pytest.param(('Иван', 'Ая в'), id='Иван, Ая в')
    ]
)
def test_new_reg_surname(params):
    name, surname = params
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru')
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input').send_keys(name)
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input').send_keys(
        surname)
    driver.find_element(By.ID, 'address').send_keys('1234@mail.com')
    time.sleep(2)
    error_text = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span').text
    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' == error_text


@pytest.mark.parametrize(
    'params',
    [
        pytest.param(('bvhf@.con'), id='bvhf@.con'),
        pytest.param(('com.@main.exampl'), id='com.@main.exampl'),
        pytest.param(('+7234123456'), id='+7234123456'),
        pytest.param(('+37512345678'), id='+37512345678'),
        pytest.param(('examplmail.ru'), id='examplmail.ru')
    ]
)
def test_new_reg_email(params):
    mail_address = params
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru')
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.ID, 'address').send_keys(mail_address)
    driver.find_element(By.ID, 'password').click()
    time.sleep(2)
    error_text = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span').text
    assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' == error_text


@pytest.mark.parametrize(
    'params',
    [
        pytest.param(('qwertyu'), id='qwertyu'),
        pytest.param(('qwertyui'), id='qwertyui'),
        pytest.param(('qwertyui1'), id='qwertyui1'),
        pytest.param(('qwertyui!'), id='qwertyui!'),
        pytest.param(('Йцукенгш1'), id='Йцукенгш1')
    ]
)
def test_new_reg_pass(params):
    password = params
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru')
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'password-confirm').click()
    time.sleep(2)
    error_text = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span').text
    assert 'Длина пароля должна быть не менее 8 символов' or\
           'Пароль должен содержать хотя бы одну заглавную букву' or\
           'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' or \
           'Пароль должен содержать только латинские буквы' == error_text

def test_new_reg_field_empte(browser):
    reg_page = RegPage(browser)
    reg_page.open()
    reg_page.open_reg()
    reg_page.click_button_register()
    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' == reg_page.message_name
    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' == reg_page.message_surname
    assert 'Введите телефон в формате +7ХХХХХХХХХХ или ' \
           '+375XXXXXXXXX, или email в формате example@email.ru' == reg_page.message_post
    assert 'Длина пароля должна быть не менее 8 символов' == reg_page.message_pass
    assert 'Длина пароля должна быть не менее 8 символов' == reg_page.message_conpas


