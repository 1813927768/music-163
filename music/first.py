from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()     # 打开 Chrome 浏览器

# driver = self.driver
driver.get("https://morvanzhou.github.io/tutorials/data-manipulation/scraping/5-01-selenium/")
driver.find_element_by_link_text(u"莫烦Python").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='近期更新'])[1]/following::img[5]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='«'])[1]/following::i[1]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='加速爬虫: 多进程分布式'])[1]/following::i[1]").click()
driver.find_element_by_xpath("//body").click()

# 得到网页 html, 还能截图
html = driver.page_source       # get html
driver.get_screenshot_as_file("./img/sreenshot1.png")
driver.close()