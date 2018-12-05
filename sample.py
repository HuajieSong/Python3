import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):  #类里面的参数可以是一个集合？

	def setUp(self):  #这句如果不加参数可以不
		#setup appium
		app=os.path.abspath('../../apps/TestApp/build/release-iphonesimulator/TestApp-iphonesimulator.app') #绝对路径和相对路径？
		self.driver=webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub') #这个IP和目录是什么意思？
		desired_capabilities={
	        'app':app ,
	        'platformName':'iOS',
	        'platformVersion':'10.1',
	        'deviceName':'iPhone 6'		
	        })
    def tearDown(self):
    	self.driver.quit()
    def _populate(self): #查找元素
    	els=[self.driver.find_element_by_accessibility_id('TextField1'),
    	     self.driver.find_element_by_accessibility_id('TextField2')]
        self._sum=0
        for i in range(2):
        	rnd=randint(0,10)
        	els[i].send_keys(rnd)  #依次在两个文本框中输入0到10随机数
        	self._sum+=rnd 
    def test_ui_computation(self):
    	self._populate()
    	#计算两个文本框中数据之和
        self.driver.find_element_by_accessibility_id('ComputeSumButton').click()
        sum=self.driver.find_element_by_accessibility_id('Answer').text
        self.assertEqual(int(sum),self._sum)   #断言 这个返回什么结果？？？
    def test_scroll(self):
    	els=self.driver.find_element_by_class_name('XCUIElementTypeButton')
    	els[5].click()
    	try:  
    		el=self.driver.find_element_by_accessibility_id('Allow')
    		el.click()
    		sleep(1)
    	except:
    		pass
    		#这段可以直接拿来用，当出现权限获取通知时抛出异常，直接点允许

    		el=self.driver.find_element_by_xpath('//XCUIElementTypeMap[1]')
    		location=el.location
    		self.driver.swipe(start_x=location['x'],start_y=location['y'],end_x=0.5,end_y=location['y'],duration=800)


    if_name_=='_main_'：
       suite=unittest.TestLoader().loadTestFromTestCase(SimpleIOSTest)
       unittest.TextTestRunner(verbosity=2).run(suite)












 






