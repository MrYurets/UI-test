
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from .base_page import BasePage
from .locators import ClientPageLocators
import time

class ClientPage(BasePage):
    def should_be_client_page(self):
        """Проверяем, что находимся на странице клиента"""
        self.should_be_client_url()  # Проверка URL
        self.should_see_devices_button()

    def should_be_client_url(self):
        """Проверяем, что URL страницы клиента соответствует ожидаемому"""
        WebDriverWait(self.browser, 10).until(
            EC.url_contains("client-113")
        )
        current_url = self.browser.current_url
        assert "client-113" in current_url, f"Expected URL to contain 'client-113', but got {current_url}"

    def should_see_devices_button(self):
        """Проверяем, что кнопка 'Устройства' присутствует на странице"""
        WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located(ClientPageLocators.DEVICES_BUTTON)
        )

    def click_on_devices_button(self):
        """Нажимаем на кнопку 'Устройства'"""
        devices_button = WebDriverWait(self.browser, 15).until(
            EC.element_to_be_clickable(ClientPageLocators.DEVICES_BUTTON))
        devices_button.click()

    def click_on_toggle_columns_button(self):
        """Нажимаем на кнопку 'Переключить столбцы'"""
        toggle_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ClientPageLocators.TOGGLE_COLUMNS_BUTTON))
        toggle_button.click()

    def click_on_close_popup(self):
        """Закрываем попап"""
        close_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ClientPageLocators.CLOSE_POPUP_BUTTON))
        close_button.click()

    def click_on_download_button(self):
        """Нажимаем на кнопку скачать отчет"""
        try:
            download_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(ClientPageLocators.DOWNLOAD_BUTTON)
            )
            download_button.click()
        except TimeoutException:
            raise TimeoutException("Превышено время ожидания при ожидании доступности кнопки 'Скачать отчет'.")
        except Exception as e:
            raise Exception(f"Ошибка при нажатии на кнопку 'Скачать отчет': {e}")

    def click_on_download_link(self, retries=3, delay=2):
        """Нажимаем на ссылку в попапе с отчетом, несколько попыток."""
        attempt = 0
        while attempt < retries:
            try:
                # Пытаемся найти и кликнуть на элемент
                download_link = WebDriverWait(self.browser, 20).until(
                    EC.element_to_be_clickable(ClientPageLocators.DOWNLOAD_LINK)
                )
                download_link.click()
                return  # Если клик прошел успешно, выходим из метода
            except Exception as e:
                # Если элемент не найден или не кликабельный, ждем и пытаемся снова
                print(f"Попытка {attempt + 1} не удалась: {str(e)}. Пытаемся снова...")
                time.sleep(delay)  # Задержка перед следующей попыткой
                attempt += 1

        # Если все попытки не удались, выбрасываем исключение
        raise Exception(f"Не удалось найти и кликнуть по ссылке после {retries} попыток.")
