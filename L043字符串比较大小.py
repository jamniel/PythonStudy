class Word(str):

    def __lt__(self, other):
        return True if len(self.split(' ', 1)[0]) < len(other.split(' ', 1)[0]) else False

    def __le__(self, other):
        return True if len(self.split(' ', 1)[0]) <= len(other.split(' ', 1)[0]) else False

    def __eq__(self, other):
        return True if len(self.split(' ', 1)[0]) == len(other.split(' ', 1)[0]) else False

    def __ne__(self, other):
        return True if len(self.split(' ', 1)[0]) != len(other.split(' ', 1)[0]) else False

    def __gt__(self, other):
        return True if len(self.split(' ', 1)[0]) > len(other.split(' ', 1)[0]) else False

    def __ge__(self, other):
        return True if len(self.split(' ', 1)[0]) >= len(other.split(' ', 1)[0]) else False




