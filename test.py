# class C:
#     def __init__(self, size=10):
#         self.size = size
#
#     def getXSize(self):
#         return self.size
#
#     def setXSize(self, value):
#         self.size = value
#
#     def delXSize(self):
#         del self.size
#
#         # 此处应该补充一句代码，程序才能正常运行
#     x = property(getXSize, setXSize, delXSize)



class C:
    def __init__(self, size=10):
      self.size = size

    @property
    def x(self):
        return self.size

    @x.setter
    def x(self, value):
        self.size = value

    @x.deleter
    def x(self):
        del self.size

