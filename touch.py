from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def point_touch(self, point, action):
	self.touch(point.x, point.y, action)
	
MonkeyDevice.point_touch = point_touch

device = MonkeyRunner.waitForConnection()

start = Point(200,1000)
end = 	Point(200,200)

device.point_touch(start, MonkeyDevice.DOWN)
time.sleep(0.1)
device.point_touch(end, MonkeyDevice.MOVE)
time.sleep(0.1)
device.point_touch(end, MonkeyDevice.UP)
