from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

# 셀레니움 열기
#driver = webdriver.Chrome('/path/to/chromedriver')
driver = webdriver.Chrome()
driver.get('https://ticket.interpark.com/Gate/TPLogin.asp?CPage=B&MN=Y&tid1=main_gnb&tid2=right_top&tid3=login&tid4=login')

# 아이디, 패스워드 입력
driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
id = driver.find_element(By.ID,'userId')
# id = driver.find_element(by= By.ID, value = "userId")
#id = driver.find_element(By.XPATH, '/html/body/form[1]/div/div/div[1]/ul/li[1]/div/input')

id.send_keys('sesnos2000')
# password = driver.find_element(By.ID, 'userPwd')
# password = driver.find_element(by= By.ID, value = "userPwd")
password = driver.find_element(By.XPATH, '/html/body/form[1]/div/div/div[1]/ul/li[2]/div/input')
password.send_keys('yumyum!227')

# 로그인 버튼 클릭
#login_button = driver.find_elements('#logstatus > a.login > img')
login_button = driver.find_element(By.XPATH, '/html/body/form[1]/div/div/div[1]/div[2]/input')
login_button.click()
time.sleep(3)

# 티켓 예약 사이트로 이동
#driver.get('https://tickets.interpark.com/goods/23009197')
target_concert = driver.find_element(By.XPATH, '/html/body/div[9]/div[6]/div[3]/div[2]/div/div[1]/ul/li[3]/a')
target_concert.click()
time.sleep(3)

# 날짜 선택
#date_button = driver.find_elements_by_xpath("//button[@data-value='2023-04-01']")
date_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[11]')
#date_button.click()
time.sleep(1)

# 회차 선택
time_selector = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/ul/li/a')
#time_selector.click()
time.sleep(1)

# 예매하기 버튼 클릭
book_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div[3]/div/div[2]/a[1]')
book_button.click()
time.sleep(1)

# 좌석 선택
seat_button = driver.find_elements('#ifrmSeat > div.seatL > ul > li:nth-child(2) > div > a')
seat_button.click()
time.sleep(1)

# 좌석 선택 완료 버튼 클릭
seat_select_button = driver.find_elements('#ifrmSeatDetail > div.wrap_bk_btn > a')
seat_select_button.click()
time.sleep(1)

# 매수 선택
ticket_num_selector = Select(driver.find_elements('#CountSelect'))
ticket_num_selector.select_by_visible_text('1')
time.sleep(1)

# 다음단계 버튼 클릭
next_button1 = driver.find_elements('#LargeNextBtn')
next_button1.click()
time.sleep(1)

# 생년월일 입력
birth_year = driver.find_elements('#YY')
birth_year.send_keys('YYYY')
birth_month = driver.find_elements('#MM')
birth_month.send_keys('MM')
birth_day = driver.find_elements('#DD')
birth_day.send_keys('DD')
time.sleep(1)

# 다음단계 버튼 클릭
next_button2 = driver.find_elements('#LargeNextBtn')
next_button2.click()
time.sleep(1)

# 무통장입금 선택
payment_option_button = driver.find_elements('#PayMethodList > li:nth-child(2) > label')
payment_option_button.click()
time.sleep(1)

# 입금 은행 선택
bank_selector = Select(driver.find_elements('#BankCode'))
bank_selector.select_by_visible_text('은행이름')
time.sleep(1)

# 다음단계 버튼 클릭
next_button3 = driver.find_elements('#LargeNextBtn')
next_button3.click()
time.sleep(1)

# 체크 버튼 클릭
check_button = driver.find_elements('#Agree')
check_button.click()
time.sleep(1)

# 결제하기 버튼 클릭
pay_button = driver.find_elements('#LargeNextBtn')
pay_button.click()