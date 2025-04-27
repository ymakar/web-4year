from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def scrape_example():
    driver = webdriver.Chrome()

    try:
        driver.get("https://example.com/login")

        # Авторизація
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys("admin")
        password_input.send_keys("password123")
        password_input.send_keys(Keys.RETURN)

        time.sleep(2)  # чекаємо на перехід

        # Перехід на сторінку профілю
        driver.get("https://example.com/profile")
        time.sleep(2)

        # Скрейп даних
        email_element = driver.find_element(By.ID, "email")
        email = email_element.text
        print(f"User email: {email}")

    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_example()
