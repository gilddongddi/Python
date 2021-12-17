class CSS:
    def __init__(self):
        self.name = input("이름 :")
        self.age = input("나이 :")

    def show(self):
        print("나의 이름은 {}, 나이는 {}세 입니다." .format(self.name, self.age))


class CSS2(CSS):
    def __init__(self):
        super().__init__()
        self.gender = input("성별 :")
    def show(self):
        print("나의 이름은 {}, 성별은 {}자, 나이는 {}세입니다.".format(self.name, self.gender, self.age))
        

class CSS3(CSS2):
    def __init__(self):
        super().__init__()
        self.grade = input("학력 :")
    def show(self):
        super().show()
        print("학력은 {}입니다.".format(self.grade))
        
a = CSS3()
a.show()


