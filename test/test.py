from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
report = Report()
driver =webdriver.Chrome()
report.setup(
report_folder=r'D:\\social_book\\social_book\\social_book\\test',
module_name='Report',
release_name='Release 1',
selenium_driver=driver
)
driver.get('http://127.0.0.1:8000/signin')
test_number=0


try:
# Test1
    test_number=test_number+1
    report.write_step(
    'Long in testing',
    status=report.status.Start,
    test_number=test_number
    )

    driver.find_element(By.NAME, "username").send_keys("pizza")
    print("find username field\n")
    driver.find_element(By.NAME, "password").send_keys("12345")
    print("find password field\n")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(4)
   
  
    time.sleep(2)
    print("Thank You")
    # Test Steps
    report.write_step(
    'Long in successfully',
    status=report.status.Pass,
    screenshot=True
    )
except AssertionError:
    report.write_step(
    'Fall to long in',
    status=report.status.Fail,
    screenshot=True
    )
except Exception as e:
    report.write_step(
    f'Something went wrong during execution!</br>{e}',
    status=report.status.Warn,
    screenshot=True
    )

    
finally:
    report.generate_report()
    driver.quit()