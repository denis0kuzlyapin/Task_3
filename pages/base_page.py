from selenium.webdriver.common.action_chains import ActionChains


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from locators.base_locators import BaseLocators


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.base_locators = BaseLocators()

    def open_page(self, test_page):
        self.driver.get(test_page)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def wait_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_url_to_be(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    def send_keys(self, locator, value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def click_safe(self, locator, overlay_locator=None):
        if overlay_locator is None:
            overlay_locator = self.base_locators.overlay

        try:
            WebDriverWait(self.driver, 2).until(
                EC.invisibility_of_element_located(overlay_locator)
            )
        except TimeoutException:
            pass

        # Кликаем через JS
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def wait_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def find_element(self, locator, timeout=10):
        timeout = timeout or 10
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def get_ingredient_counter(self, locator):
        counter = self.find_element(locator)
        return int(counter.text)

    def get_order_id(self, locator):
        order_id = self.find_element(locator)
        return int(order_id.text)

    def get_current_url(self):
        return self.driver.current_url

    def is_element_present(self, locator, timeout=3):
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    def drag_and_drop_js(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        script = """
            function simulateDragDrop(source, target) {
                var dragStartEvent = new MouseEvent('dragstart', {
                    view: window,
                    bubbles: true,
                    cancelable: true,
                    clientX: source.getBoundingClientRect().left,
                    clientY: source.getBoundingClientRect().top
                });
                var dropEvent = new MouseEvent('drop', {
                    view: window,
                    bubbles: true,
                    cancelable: true,
                    clientX: target.getBoundingClientRect().left,
                    clientY: target.getBoundingClientRect().top
                });
                var dragEndEvent = new MouseEvent('dragend', {
                    view: window,
                    bubbles: true,
                    cancelable: true,
                    clientX: target.getBoundingClientRect().left,
                    clientY: target.getBoundingClientRect().top
                });
                source.dispatchEvent(dragStartEvent);
                target.dispatchEvent(dropEvent);
                source.dispatchEvent(dragEndEvent);
            }
            simulateDragDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(script, source, target)

    def scroll_to_element_in_container(self, container_locator, element_locator):
        container = self.find_element(container_locator)
        element = self.find_element(element_locator)
        self.driver.execute_script(
            """
            arguments[0].scrollTop = arguments[1].offsetTop - arguments[0].offsetHeight/2;
        """,
            container,
            element,
        )
