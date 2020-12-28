from datetime import datetime
from os import path
class Test:

    def __init__(self,*args):
        pass

    def test_file(self, data):
        return path.isfile(data)

    def test_dir(self, data):
        return path.isdir(data)
    

# def main():
#     test = Test()
#     print("test_mont", test.year("2"))


# if __name__ == "__main__":
#     main()