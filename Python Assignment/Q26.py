class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def displayError(self):
	print self.msg

error = MyError("Error")
error.displayError()