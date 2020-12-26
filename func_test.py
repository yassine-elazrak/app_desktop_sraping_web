from datetime import datetime

class Test:
    var = 9 
    def __init__(self,*args):
        pass
    selfl.f= 80

    def year(self,data):
        string = str(data)
        date_now = datetime.now().year
        if string.isdigit():
            if int(string) >= 2006 and int(string) <= date_now:
                return True
            else:
                return False
        return False

    def month(self, data):
        if string.isdigit():
            if int(string) >= 1 and int(string) <= 12:
                return True
            else:
                return False
        return False

    def hour(self, data):
        if string.isdigit():
            if int(string) >= 0 and int(string) <= 23:
                return True
            else:
                return False
        return False

def main():
    test = Test()
    print("test_mont", test.year("2"))


if __name__ == "__main__":
    main()