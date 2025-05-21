from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:

    # Target test site
    URL = "https://testsheepnz.github.io/BasicCalculator.html"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    # Ensure page load checking for header    
    def load(self):
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "intro-heading")))

    # Calculator input "First Number"
    @property
    def num1(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "number1Field")))

    # Calculator input "Second Number"
    @property
    def num2(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "number2Field")))

    # Calculator select "Operation"
    @property
    def operation_select(self):
        elem = self.wait.until(EC.presence_of_element_located((By.ID, "selectOperationDropdown")))
        return Select(elem)
    
    # Calculator checkbox "Integers only"
    @property
    def integer_only_checkbox(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "integerSelect")))

    # Calculator button "Calculate"
    @property
    def calculate_btn(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "calculateButton")))
    
    # Calculator output "Answer"
    @property
    def answer(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "numberAnswerField"))).get_attribute("value")

    # Calculator error popup
    @property
    def error_message(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "errorMsgField"))).text

    # Operate calculator UI
    def calculate(self, a, b, op_value, integer_only=False):
        # Clear and input values
        self.num1.clear()
        self.num1.send_keys(str(a))
        self.num2.clear()
        self.num2.send_keys(str(b))

        # Handle integer-only checkbox only if operation is NOT concatenate
        if str(op_value) != "4":  # "4" is concatenate
            checkbox = self.integer_only_checkbox
            if checkbox.is_selected() != integer_only:
                checkbox.click()
        else:
            # Ensure checkbox is unchecked (safe default) for concatenate
            checkbox = self.integer_only_checkbox
            if checkbox.is_selected():
                checkbox.click()

        # Select the operation
        self.operation_select.select_by_value(str(op_value))

        # Click calculate
        self.calculate_btn.click()

        # Wait for the result to update
        WebDriverWait(self.driver, 5).until(
            lambda d: d.find_element(By.ID, "numberAnswerField").get_attribute("value") != ""
        )

        # Re-fetch answer and error to ensure fresh state
        answer = self.driver.find_element(By.ID, "numberAnswerField").get_attribute("value")
        error = self.driver.find_element(By.ID, "errorMsgField").text.strip()

        return {
            "answer": answer,
            "error": error if error else None
        }
