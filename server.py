from selenium import webdriver

import time
phone = "9779779797"
password = "password"
email = "test@test.ru"



driver = webdriver.Chrome(executable_path='D:\work\selenium\driver\chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(30)
driver.get("https://www.avito.ru/additem")
window_before = driver.window_handles[0]
#driver.find_element_by_css_selector('a[data-marker="header/login-button"]')
driver.find_element_by_css_selector('span[data-marker="social-network-item(vk)"]').click()
window_after = driver.window_handles[1]


driver.switch_to.window(window_after)
driver.find_element_by_css_selector('input[name="email"').send_keys(phone)
driver.find_element_by_css_selector('input[name="pass"').send_keys(password)
driver.find_element_by_css_selector('#install_allow').click()

driver.switch_to.window(window_before)

driver.find_element_by_css_selector('a[href="/profile"]').click()
driver.find_element_by_css_selector('a[href="/additem"]').click()
time.sleep(5)
#'.cascader-table-category-2PKmD:nth-child(10)').click()
driver.execute_script("document.getElementsByClassName('cascader-table-category-2PKmD')[8].click()")

#driver.execute_script("document.getElementsByClassName('comment-user')[0].click()")
#driver.find_element_by_link_text("Животные")
#driver.find_elements_by_css_selector('.cascader-table-category-2PKmD:nth-child(10)').click()

#for x in driver.find_elements_by_link_text("Животные"):
#    link = webdriver.ActionChains(driver).move_to_element(x).click(x).perform()

driver.find_elements_by_css_selector('#title')[0].send_keys("testСобачкаtitle")
time.sleep(5)
driver.find_elements_by_css_selector('.category-button-1y16l')[0].click() #.send_keys("Собака")
driver.find_elements_by_css_selector('.cascader-table-column-2cmhR:nth-child(2) > .cascader-table-category-2PKmD:nth-child(2)')[0].click()
#dropdown
driver.find_element_by_css_selector('#params\\[211\\]').click()
driver.find_element_by_css_selector('.suggest-suggest-13bdM:nth-child(1)').click()
driver.find_element_by_css_selector('#params\\[2812\\]').click()
driver.find_element_by_css_selector('#params\\[2812\\] > option:nth-child(2)').click()
driver.find_element_by_css_selector('#title').send_keys("theСобака")
driver.find_element_by_css_selector('#description').send_keys("theСобака")
driver.find_element_by_css_selector('#price').send_keys("0")

#upload file
driver.find_element_by_css_selector('input[type="file"]').send_keys("D:\work\selenium\driver\chromedriver_win32\image.PNG")



driver.find_element_by_css_selector('#email').send_keys(email)
driver.find_element_by_css_selector('#phone').send_keys(phone)
#submint
driver.find_element_by_css_selector('button[data-marker="item-edit/button-next"]').click()

#driver.find_element_by_css_selector('input[data-marker="login-form/login"]').send_keys("pet015@yandex.ru")
#driver.find_element_by_css_selector('input[data-marker="login-form/password"]').send_keys("W47")
#driver.find_element_by_css_selector('button[name="submit"]').click()
#driver.find_element_by_css_selector('abc')


driver.switch_to.window(window_after)
driver.find_element_by_css_selector('input[name="email"').send_keys("7975675672776575617")
driver.find_element_by_css_selector('input[name="pass"').send_keys("rdhytfr")
driver.find_element_by_css_selector('#install_allow').click()

driver.switch_to.window(window_before)

driver.find_element_by_css_selector('a[href="/profile"]').click()
driver.find_element_by_css_selector('a[href="/additem"]').click()
driver.find_elements_by_css_selector('.cascader-table-column-2cmhR:nth-child(1)')[6].click()


driver.find_element_by_css_selector('input[data-marker="login-form/login"]').send_keys("pet015@yandex.ru")
driver.find_element_by_css_selector('input[data-marker="login-form/password"]').send_keys("W47")
driver.find_element_by_css_selector('button[name="submit"]').click()
driver.find_element_by_css_selector('abc')



