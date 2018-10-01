class Nint(int):

    def __init__(self, x):
        try:
            self.x = int(x)
        except:
            self.x = ord(x)
    