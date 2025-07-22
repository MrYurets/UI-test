
import allure
from web_pages.login_page import LoginPage
from web_pages.client_page import ClientPage

login_link = "https://stage-mgt.antisleep.ru/login"
client_link = "https://stage-mgt.antisleep.ru/client-113"


@allure.feature("Регистрация пользователя")
class TestRegistrationPage:
    @allure.story("Пользователь может зарегистрироваться")
    @allure.step("Открытие страницы логина")
    def test_can_register_user(self, browser):
        page = LoginPage(browser, login_link)

        # Открытие страницы логина
        page.open()
        allure.attach("Открыта страница регистрации", "Страница успешно загружена")

        # Логинимся в систему
        page.authorization_user("demo@demo.ru", "Demo1704@demo.ru")
        allure.attach("Пользователь успешно авторизован", "Данные введены и отправлены")

        # Проверяем переход на страницу клиента
        current_url = browser.current_url
        assert current_url == client_link, f"Expected URL {client_link}, but got {current_url}"
        allure.attach("Проверка перехода на страницу", f"переход на {client_link} успешен")

        # Переход на страницу клиента
        client_page = ClientPage(browser, client_link)
        client_page.open()
        allure.attach("Переход на страницу клиента", "Страница клиента открыта")

        # Нажимаем на кнопку 'Устройства'
        client_page.click_on_devices_button()
        allure.attach("Нажата кнопка 'Устройства'", "Переход на страницу устройств")

        # Нажимаем на кнопку 'Переключить столбцы'
        client_page.click_on_toggle_columns_button()
        allure.attach("Нажата кнопка 'Переключить столбцы'", "Изменение столбцов")

        # Нажимаем на кнопку закрыть попап
        client_page.click_on_close_popup()
        allure.attach("Закрыт попап", "Попап был закрыт")

        # Нажимаем на кнопку скачать отчет
        client_page.click_on_download_button()
        allure.attach("Нажата кнопка 'Скачать отчет'", "Запуск скачивания отчета")

        # Нажимаем на ссылку скачать отчет
        client_page.click_on_download_link()
        allure.attach("Нажата ссылка для скачивания отчета", "Ссылка для скачивания отчета нажата")