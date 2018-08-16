class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            f = open(self.filename, "r")
            result = f.read()
            f.close()
        except IOError:
            return ""
        else:
            return result