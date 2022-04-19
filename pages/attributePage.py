from locators.locators import Locators

class AttributePage():

	def __init__(self, driver):

		self.driver = driver
		self.attribute_create_page = Locators.attribute_create_page


	def open_create_attribute(self):

		self.driver.get(self.attribute_create_page)