from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


MESSAGE = "salam"

LIST_OF_DIRECTS = ['#@']

SEND_TIME = "01:53"

time_delay = random.randint(4,12)


def send_message(driver, message, list_of_directs):
    for directs in list_of_directs:
        try:
            driver.get(f"https://web.telegram.org/k/{directs}")
            time.sleep(time_delay)

            message_input = driver.find_element(By.CSS_SELECTOR,
                                                "#column-center > div > div.chat.tabs-tab.can-click-date.active > div.chat-input.chat-input-main > div > div.rows-wrapper-wrapper > div > div.new-message-wrapper.rows-wrapper-row > div.input-message-container > div:nth-child(1)")
            message_input.send_keys(message)
            time.sleep(time_delay)
            message_input.send_keys(Keys.ENTER)
            time.sleep(time_delay)

            print(f"Message sent to {directs} successfully.")

        except Exception as e:
            print(f"Failed to send message to {directs}: {e}")


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://web.telegram.org")

    while True:
        current_time = time.strftime("%H:%M")
        if current_time == SEND_TIME:
            time.sleep(time_delay)
            send_message(driver, MESSAGE, LIST_OF_DIRECTS)
            time.sleep(time_delay)

        time.sleep(time_delay)
