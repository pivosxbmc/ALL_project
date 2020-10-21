from faker import Faker
#设置中文
class New_Data(object):
	"""docstring for """
	def __init__(self):
		self.faker = Faker('zh_CN')
		self.all_message = self.faker.profile()
	def get_phone(self):
		return self.faker.phone_number()
	def get_name(self):
		return self.all_message['name']
	def get_address(self):
		return self.all_message['address']
	def get_mail(self):
		return self.all_message['mail']
	def get_id_card(self):
		return self.all_message['ssn']
	def get_text(self):
		return self.faker.paragraph()

if __name__ == '__main__':
	faker = Faker('zh_CN')
	test = faker.profile()
	print(test)
	print('>'*10)
	testa = New_Data().get_name()
	print(testa)
