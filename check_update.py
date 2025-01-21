from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from notify import make_notification
import time
import sys

LOGIN_URL = "https://autograder.ucsd.edu/login"

if len(sys.argv) != 4:
    print("Usage: python check_update.py <email> <password> <queue_url>")
    print("<email>: Your autograder associated ucsd email.")
    print("<password>: Your autograder associated password.")
    print("<queue_url>: Your course queue link, i.e. 'https://autograder.ucsd.edu/queue/778'")
    sys.exit(1)

USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]
QUEUE_URL = sys.argv[3]

def login_and_check_updates_selenium():
    # Set up WebDriver (e.g., ChromeDriver)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")  # Disable GPU (optional, improves compatibility)
    chrome_options.add_argument("--no-sandbox")  # Required for running on some Linux environments
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")
    driver = webdriver.Chrome(options=chrome_options)  # Or use another browser driver
    
    driver.get(LOGIN_URL)

    # Step 1: Enter login credentials
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)  # Submit the login form

    # Step 2: Wait for login to complete
    time.sleep(3)

    # Step 3: Navigate to the queue page
    driver.get(QUEUE_URL)
    time.sleep(3)

    # Step 4: Extract dynamically loaded content
    # Adjust the selector based on the content you need
    ticket_count = int(driver.title.split(" ")[0])
    print("Ticket Count:", ticket_count)
    if ticket_count > 0:
        make_notification()
    return ticket_count
    

count = 0
errcnt = 0
while count < 1:
    if errcnt > 10:
        make_notification()
    try:
        errcnt = 0
        count = login_and_check_updates_selenium()
    except:
        errcnt += 1
        continue


