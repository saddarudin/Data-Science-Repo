class Human:
    def __init__(self, n, o, s):
        self.name = n
        self.occupation = o
        self.status = s

    def work(self):
        print(f"{self.name} has started working")

    def run(self):
        print(f"{self.name} has started running")

    def describe(self):
        print(f"My name is {self.name}, I am a {self.occupation} and I am {self.status}")


sdb = Human("Saddar", "Student", "Single")
sdb.work()
sdb.run()
sdb.describe()
