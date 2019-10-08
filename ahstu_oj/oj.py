from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

if __name__ == '__main__':
    browser = webdriver.Firefox()
    browser.set_page_load_timeout(20)  # 防止页面加载个没完
    browser.get('https://oj.ahstu.cc/JudgeOnline/loginpage.php')

    # browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary btn-block"]').click()  # 点击登录按钮，一般网站该步可省略

    emailInput = browser.find_element_by_xpath('//div[@class="wrapper"]/form[@class="form-signin"]/input[1]')
    emailInput.clear()
    emailInput.send_keys("1881180120")
    passwordInput = browser.find_element_by_xpath('//div[@class="wrapper"]/form[@class="form-signin"]/input[2]')
    passwordInput.clear()
    passwordInput.send_keys("ylyy2311")
    # form = browser.find_element_by_xpath("//form[@class='zu-side-login-box']")
    # form.submit()
    browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-block']").click()
    browser.find_element_by_xpath("//div[@class='htmleaf-container']/li[2]/a[2]").click()

    # html = somedom.find_element_by_xpath("//*").get_attribute("outerHTML")
    browser.quit()