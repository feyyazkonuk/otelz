from selenium import webdriver
import time
import userInfo as ui

class Reservation():
	"""docstring for Reservation"""
	def __init__(self, link):
		super(Reservation, self).__init__()
		self.link = link
		self.driver_path = "/Users/pro/desktop/otelz/drivers/chromedriver"
		self.driver = webdriver.Chrome(self.driver_path)
		self.log_file = open("log.text", "a")
		Reservation.goLink(self)
		Reservation.Login(self)
		Reservation.Reserve(self)

	def goLink(self):
		self.driver.get(self.link)
		self.driver.maximize_window()
		time.sleep(5)


	def Login(self):
		self.driver.find_element_by_xpath("//*[@id=\"pageBody\"]/div[4]/header/div/div/div[3]/ul/li[6]/a/span").click()
		time.sleep(2)

		mail = self.driver.find_element_by_xpath("//*[@id=\"pageBody\"]/div[4]/header/div[1]/div[2]/div/div[2]/div/div[1]/label/input")
		password = self.driver.find_element_by_xpath("//*[@id=\"pageBody\"]/div[4]/header/div[1]/div[2]/div/div[2]/div/div[2]/label[1]/input")

		mail.send_keys(ui.mail)
		password.send_keys(ui.password)

		login_button = self.driver.find_element_by_xpath("//*[@id=\"pageBody\"]/div[4]/header/div[1]/div[2]/div/div[2]/div/div[3]/button")
		login_button.click()
		time.sleep(5)

	def Reserve(self):
		reserve_button = self.driver.find_element_by_xpath("//*[@id=\"pageBody\"]/div[4]/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/a")
		reserve_button.click()
		time.sleep(2)

		reserve_now_button = self.driver.find_element_by_xpath("//*[@id=\"ancPriceList\"]/div/div/div[1]/div/div[2]/div/div[2]/a")
		reserve_now_button.click()
		time.sleep(5)


		tel_no = self.driver.find_element_by_xpath("//*[@id=\"CustomerInfoPhone\"]")
		tel_no.send_keys(ui.tel_no)
		time.sleep(2)

		self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		time.sleep(2)

		save_and_continue_button = self.driver.find_element_by_xpath("//*[@id=\"pageBody\"]/div[4]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div[6]/div[2]/button")
		save_and_continue_button.click()
		time.sleep(2)

		complete_reservation_button = self.driver.find_element_by_xpath("//*[@id=\"pageBody\"]/div[4]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[3]/div[2]/button/strong[1]")
		complete_reservation_button.click()
		time.sleep(5)

		message_tr = "Rezervasyonunuz Onaylandı"
		message_en = "Your Reservation Has Been Confirmed"

		message = self.driver.find_element_by_xpath("//*[@id=\"pageBody\"]/div[4]/div/div[1]/div/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div/div/strong[2]").text
													
		if message == message_tr or message_en:
			time.sleep(3)
			self.driver.save_screenshot("/Users/pro/desktop/otelz/Reservation/ss/reservation_test_passed.png")
			timestr = time.strftime("%Y.%m.%d-%H.%M.%S")
			self.log_file.write("\n\n" + "PASSED: İlk Resort Test Otel - Seçilen Giriş: 30.01.2021 Çıkış: 31.01.2021 tarihleri arası ilk rezervasyon başarıyla oluşturuldu. - " + timestr + "\n" + "\n")
			time.sleep(2)
			Reservation.goLink(self)
			time.sleep(3)
			Reservation.againReserve(self)
			
		else:
			timestr = time.strftime("%Y.%m.%d-%H.%M.%S")
			self.log_file.write("\n\n" + "FAILED: Rezervasyon oluşturulamadı! - " + timestr + "\n")
			self.log_file.close()
			time.sleep(5)
			self.driver.quit()

	def againReserve(self):
		reserve_button = self.driver.find_element_by_xpath("//*[@id=\"pageBody\"]/div[4]/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/a")
		reserve_button.click()
		time.sleep(2)

		reserve_now_button = self.driver.find_element_by_xpath("//*[@id=\"ancPriceList\"]/div/div/div[1]/div/div[2]/div/div[2]/a")
		reserve_now_button.click()
		time.sleep(5)

		tel_no = self.driver.find_element_by_xpath("//*[@id=\"CustomerInfoPhone\"]")
		tel_no.send_keys(ui.tel_no)
		time.sleep(2)

		self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		time.sleep(2)

		save_and_continue_button = self.driver.find_element_by_xpath("//*[@id=\"pageBody\"]/div[4]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div[6]/div[2]/button")
		save_and_continue_button.click()
		time.sleep(2)

		complete_reservation_button = self.driver.find_element_by_xpath("//*[@id=\"pageBody\"]/div[4]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[3]/div[2]/button/strong[1]")
		complete_reservation_button.click()
		time.sleep(5)

		message_tr = "Rezervasyonunuz Onaylandı"
		message_en = "Your Reservation Has Been Confirmed"

		message = self.driver.find_element_by_css_selector("#pageBody > div.app-wrapper.no-transition.ng-scope > div > div.content-wrapper > div > div > div > div > div > div.col-sm-8.margin-b-lg > div > div.steps-desktop.step-3.ng-scope > div > div.panel-body > div.text-center > div > div > strong.font-20.text-bolder.text-block.ng-binding.ng-scope").text

		if message == message_tr or message_en:
			self.driver.save_screenshot("/Users/pro/desktop/otelz/Reservation/ss/reservation_test_failed-must_be_warning_message.png")
			timestr = time.strftime("%Y.%m.%d-%H.%M.%S")
			self.log_file.write("\n\n" + "FAILED: İlk Resort Test Otel - Seçilen Giriş: 30.01.2021 Çıkış: 31.01.2021 tarihleri arası tekrar rezervasyon oluşturuldu. Uyarı mesajı gösterilmesi gerekiyor" + "\n" + "\n" + 
				"UYARI MESAJI: Bu otelde aynı giriş tarihinde daha önce rezervasyonunuz bulunmaktadır. Devam etmek istediğinize emin misiniz? Rezervasyonu iptal ettiğiniz taktirde, hesaplanan iptal cezası tesis tarafından sizden talep edilecektir. - " + timestr + "\n" + "\n")
			self.log_file.close()
			time.sleep(3)
			self.driver.quit()

		else:
			self.driver.quit()






