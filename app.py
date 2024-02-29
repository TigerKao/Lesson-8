class Student: # 大寫開頭的是 Class，小寫開頭的是 Function
    def __init__(self, name, score) : # initialize 初始化的意思
        self.name = name # 使用 Self 來增加身上的屬性（attributes），透過 Self 來共用身上的屬性
        self.score = score
        print("I'm here!")

    def do_hw(self, hw): # 使用 Self 來存取自身上的 Function
        print("Homework!!!!")

    def study(self):
        print("Reading!?")
        self.score += 5

s1 = Student("John", 100)
s2 = Student("Mike", 95)

students = [s1, s2]

for s in students:
    print(s.name, "的分數是", s.score)