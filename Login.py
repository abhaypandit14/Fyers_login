from seleniumbase import Driver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyotp as t
from fyers_apiv3 import fyersModel
#-----------------------------------------------------------
def write_file(token):
    with open("fyers_access_token.txt", "w") as f:
        f.write(token)
#-----------------------------------------------------------
client_id = "105*******-100"
secret_key = "H97*******"
redirect_uri = "https://trade.fyers.in/api-login/redirect-uri/index.html"
response_type = "code"  
state = ""
grant_type = "authorization_code"  
#-----------------------------------------------------------
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key, 
    redirect_uri=redirect_uri, 
    response_type=response_type, 
    grant_type=grant_type)
#-----------------------------------------------------------
while True:
    try:
        response1 = session.generate_authcode()
        driver=Driver(uc=True)
        url=response1
        driver.uc_open_with_reconnect(url,4)
        driver.uc_gui_click_captcha()
        driver.find_element(By.XPATH, '//*[@id="mobile-code"]').click()
        time.sleep(2)
        mobilenumber=1234567890
        driver.find_element(By.XPATH, '//*[@id="mobile-code"]').send_keys(mobilenumber)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="mobileNumberSubmit"]').click()
        time.sleep(2)
        totp_key = "PIMA757UIY3WAEPRTB5UY7JET4CJ4MUT"
        k=t.TOTP(totp_key).now()
        driver.find_element(By.XPATH, '//*[@id="first"]').click()
        driver.find_element(By.XPATH, '//*[@id="first"]').send_keys(k[0])
        driver.find_element(By.XPATH, '//*[@id="first"]').send_keys(Keys.TAB)
        driver.find_element(By.XPATH, '//*[@id="second"]').send_keys(k[1])
        driver.find_element(By.XPATH, '//*[@id="second"]').send_keys(Keys.TAB)
        driver.find_element(By.XPATH, '//*[@id="third"]').send_keys(k[2])
        driver.find_element(By.XPATH, '//*[@id="third"]').send_keys(Keys.TAB)
        driver.find_element(By.XPATH, '//*[@id="fourth"]').send_keys(k[3])
        driver.find_element(By.XPATH, '//*[@id="fourth"]').send_keys(Keys.TAB)
        driver.find_element(By.XPATH, '//*[@id="fifth"]').send_keys(k[4])
        driver.find_element(By.XPATH, '//*[@id="fifth"]').send_keys(Keys.TAB)
        driver.find_element(By.XPATH, '//*[@id="sixth"]').send_keys(k[5])
        driver.find_element(By.XPATH, '//*[@id="confirmOtpSubmit"]').click()
        time.sleep(2)
        driver.find_element(By.ID,"verifyPinForm").find_element(By.ID,"first").send_keys(1)
        driver.find_element(By.ID,"verifyPinForm").find_element(By.ID,"second").send_keys(2)
        driver.find_element(By.ID,"verifyPinForm").find_element(By.ID,"third").send_keys(3)
        driver.find_element(By.ID,"verifyPinForm").find_element(By.ID,"fourth").send_keys(4)
        driver.find_element(By.XPATH, '//*[@id="verifyPinSubmit"]').click()
        time.sleep(2)
        auth_code=driver.find_element(By.XPATH, '//*[@id="s_auth_code"]').text
        session.set_token(auth_code)
        response = session.generate_token()
        access_token=response['access_token']
        write_file(access_token)
        print("Access token Generated")
        break
    
    except Exception as e:
        print(f"Error Occured Retrying in 10 seconds...")
        time.sleep(10)


    


