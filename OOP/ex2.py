class PG:
    x=0
    def __init__(self):
        print("created")
    def bark(self):
        self.x=self.x+1
        print(self.x)
    def __del__(self):
        print("deleted")


an=PG()
an.bark()
an.bark()
an.bark()

an=42
print(an)