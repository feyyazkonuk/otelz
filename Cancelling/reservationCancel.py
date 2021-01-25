from selenium import webdriver
import time
import BookingInfo as bi
from selenium.webdriver.support.select import Select

class ReservationCancel():
	"""docstring for ReservationCancel"""
	def __init__(self, link):
		super(ReservationCancel, self).__init__()
		self.link = link
		self.driver_path = "/Users/pro/desktop/otelz/drivers/chromedriver"
		self.driver = webdriver.Chrome(self.driver_path)
		self.log_file = open("log.txt" , "a")

		ReservationCancel.goLink(self)
		ReservationCancel.goChangeBooking(self)
		ReservationCancel.cancelReservation(self)


	def goLink(self):
		self.driver.get(self.link)
		self.driver.maximize_window()
		time.sleep(5)


	def goChangeBooking(self):
		self.driver.find_element_by_xpath("//*[@id=\"pageBody\"]/div[4]/header/div[2]/div/div[3]/ul/li[5]/a/span").click()
		time.sleep(5)

		booking_no = self.driver.find_element_by_xpath("//*[@id=\"pageBody\"]/div[4]/header/div[1]/div[2]/div/div/div/label[1]/input")
		pin_no = self.driver.find_element_by_xpath("//*[@id=\"pageBody\"]/div[4]/header/div[1]/div[2]/div/div/div/label[2]/input")

		booking_no.send_keys(bi.booking_no)
		pin_no.send_keys(bi.pin_no)

		check_button = self.driver.find_element_by_xpath("//*[@id=\"pageBody\"]/div[4]/header/div[1]/div[2]/div/div/div/div[1]/button")
		check_button.click()
		time.sleep(5)

	def cancelReservation(self):
		cancel_button = self.driver.find_element_by_css_selector("#userPageView > div > div > div > div.res-management-wrapper.ng-scope > div.res-detail-actions.ng-scope > button.btn.btn-danger.btn-outline > span")
		cancel_button.click()
		time.sleep(3)

		self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		time.sleep(2)

		irreversible_button = self.driver.find_element_by_css_selector("#panelActions > div > div > div.panel-body > div.action-content > button.btn.btn-danger")
		irreversible_button.click()
		time.sleep(3)

		choose = Select(self.driver.find_element_by_css_selector("#cancellationReason > div > div.row > div > span > select"))
		choose.select_by_index(4)
		time.sleep(5)

		yes_button = self.driver.find_element_by_css_selector("#pageBody > div.modal.ng-scope.pop-master.res-detail-modal.cancellation-reason-modal.near-top > div.modal-dialog.modal-lg.fastest.from-top > div > div.custom-footer.action-content.modal-footer > button.btn.btn-danger.margin-b")
		yes_button.click()
		time.sleep(5)

		message_tr = "Rezervasyonunuz İptal Edildi"
		message_en = "Your Reservation Has Been Cancelled"

		message = self.driver.find_element_by_xpath("//*[@id=\"userPageView\"]/div/div/div/div[1]/div/div/div[2]/div[1]/h3/span").text

		if message == message_tr or message_en:
			timestr = time.strftime("%Y.%m.%d-%H.%M.%S")
			self.log_file.write("\n\n" + "PASSED: Testi başarıyla tamamlamıştır. Rezervasyon beklenildiği gibi iptal edilmiştir. - " + timestr + "\n")
			self.driver.save_screenshot("/Users/pro/desktop/otelz/Cancelling/ss/cancel_test_passed.png")
			time.sleep(3)
			self.driver.quit()
		else:
			timestr = time.strftime("%Y.%m.%d-%H.%M.%S")
			self.driver.save_screenshot("/Users/pro/desktop/otelz/Cancelling/ss/failed.png")
			self.log_file.write("\n\n" + "FAILED: Test başarısız. Rezervasyon iptal işlemi gerçekleşmedi. - " + timestr + "\n")
			time.sleep(3)
			self.driver.quit()













		