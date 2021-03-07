from selenium import webdriver
import time

edge_driver_path = "C:\Development\msedgedriver.exe"
driver = webdriver.Edge(executable_path=edge_driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")


cookie = driver.find_element_by_id("bigCookie")


end_game = time.time() + 60 * 5  # 5 minutes
check_upgrade = time.time() + 5

while True:
    if time.time() > end_game:
        break

    cookie.click()

    if time.time() > check_upgrade:
        click_product_list = []
        price_product_list = []
        product_available = driver.find_elements_by_css_selector("#products .enabled")
        for product in product_available:
            price = product.find_element_by_css_selector(".content .price").text
            price = price.replace(",", "")
            price_product_list.append(int(price))
            click_product_list.append(product)
        click_product_list[price_product_list.index(max(price_product_list))].click()
        check_upgrade += 5


cookies_per_second = driver.find_element_by_css_selector("#cookies div").text
cookies_per_second = cookies_per_second.split(":")[1]
print(f"cookies/second: {cookies_per_second}")

