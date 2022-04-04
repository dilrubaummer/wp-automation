from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


#Downlod image from url
# import urllib.request
# urllib.request.urlretrieve('https://dummyimage.com/600x400/000/fff&text=ok', "logo.png")
# print(html)

#Create random images by python
# from PIL import Image
# import random
# width = 400
# height = 300
# for i in range(1,1000):
# 	img  = Image.new( mode = "RGB", size = (width, height), color = tuple(random.choices(range(256), k=3)) )
# 	img.save("images/new_img_"+str(i)+".jpg")
# driver.close()


#start
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://localhost:8888/development-pro/wp-admin/post.php?post=2379&action=edit')

#Login
driver.find_element_by_xpath('//*[@id="user_login"]').clear()
driver.find_element_by_xpath('//*[@id="user_login"]').send_keys('development_pro')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="user_pass"]').clear()
driver.find_element_by_xpath('//*[@id="user_pass"]').send_keys('development_pro@123')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="wp-submit"]').click()
time.sleep(2)


#Create  Local Attributes and Terms

# driver.find_element_by_xpath('//*[@id="woocommerce-product-data"]/div[2]/div/ul/li[5]/a').click()
# time.sleep(2)

# i=0
# time.sleep(2)
# elem = driver.find_element_by_xpath("//button[@class='button add_attribute']")
# for j in range(97,101):
# 	terms = ''
# 	time.sleep(3)
	
# 	driver.execute_script("arguments[0].click();", elem)
# 	time.sleep(3)
# 	driver.find_element_by_name('attribute_names['+str(i)+']').send_keys('attr_'+chr(j))
# 	time.sleep(2)
	
# 	for k in range(97,103):
# 		terms = terms+'|'+ (chr(j)+'-'+chr(k))  if terms else (chr(j)+'-'+chr(k))
# 	time.sleep(2)
# 	driver.find_element_by_name('attribute_values['+str(i)+']').send_keys(terms)
# 	time.sleep(2)
# 	driver.find_element_by_name('attribute_variation['+str(i)+']').click()
# 	time.sleep(2)
# 	i+=1

# time.sleep(4)
# driver.find_element_by_xpath('//*[@id="product_attributes"]/div[3]/button').click()
# time.sleep(4)


#Create variations

# driver.find_element_by_xpath('//*[@id="woocommerce-product-data"]/div[2]/div/ul/li[6]/a').click()
# time.sleep(2)
# Select(driver.find_element_by_xpath('//*[@id="field_to_edit"]')).select_by_value('link_all_variations')
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="variable_product_options_inner"]/div[2]/a').click()
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="variable_product_options_inner"]/div[4]/button[1]').click()


#Apply Price
time.sleep(2)
driver.find_element_by_xpath('//*[@id="woocommerce-product-data"]/div[2]/div/ul/li[6]/a').click()

time.sleep(4)
a = ActionChains(driver)
for i in range(2,16):
	time.sleep(4)
	n  = driver.find_element_by_xpath('//*[@id="variable_product_options_inner"]/div[3]/div['+str(i)+']/h3/div[1]')
	# hover over element and click
	a.move_to_element(n).click().perform()
	time.sleep(2)
	p = i-2
	driver.find_element_by_xpath('//*[@id="variable_regular_price_'+str(p)+'"]').send_keys(20+i)
	time.sleep(2)
	a.move_to_element(n).click().perform()
	time.sleep(2)

time.sleep(3)
driver.find_element_by_xpath('//button[@class="button-primary save-variation-changes"]').click()
time.sleep(2)



# driver.find_element_by_xpath('//*[@id="variable_product_options_inner"]/div[2]/div[1]/span[3]/a[3]').click()
# time.sleep(4)

# for i in range(2,14):
# 	time.sleep(2)
# 	n  = driver.find_element_by_xpath('//*[@id="variable_product_options_inner"]/div[3]/div['+str(i)+']/h3/div[1]')
# 	# hover over element and click
# 	a.move_to_element(n).click().perform()
# 	time.sleep(2)
# 	p = i-2
# 	driver.find_element_by_xpath('//*[@id="variable_regular_price_'+str(p)+'"]').send_keys(20)
# 	time.sleep(2)
# 	a.move_to_element(n).click().perform()
# 	time.sleep(2)

# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="variable_product_options_inner"]/div[4]/button[1]').click()
# time.sleep(2)

#ex




# driver.find_element_by_xpath('//*[@id="woocommerce-product-data"]/div[2]/div/ul/li[7]/a').click()
# time.sleep(4)
# driver.find_element_by_xpath('//*[@id="custom_variations_inner"]/div[1]').click()
# time.sleep(3)

#en

# Select(driver.find_element_by_xpath('//*[@id="custom_variations_inner"]/div[1]/div/table/tbody/tr[1]/td/p/select')).select_by_value('image')
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="publish"]').click()
# time.sleep(2)

# driver.find_element_by_xpath('//*[@id="custom_variations_inner"]/div[1]/div/table/tbody/tr[5]/td/table[2]/tbody/tr[1]/td/h3').click()
# time.sleep(2)


#select Image



# driver.find_element_by_xpath('//*[@id="custom_variations_inner"]/div[1]/div/table/tbody/tr[5]/td/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/div/div[2]/button[1]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="menu-item-upload"]').click()
# time.sleep(3)
# input_file = "//input[starts-with(@id,'html5_')]"
# driver.find_element_by_xpath(input_file).send_keys("/Applications/images/new_img_4.jpg")
# time.sleep(2)
# driver.find_element_by_css_selector('.button.media-button.button-primary.button-large.media-button-select').click()
# # //button[contains(@class,'button media-button')]
# time.sleep(2)

# element = driver.find_element_by_xpath("(//input[@name='save'])[2]")
# # button = driver.find_element_by_xpath("xpath")
# driver.execute_script("arguments[0].click();", element)

# time.sleep(2)




