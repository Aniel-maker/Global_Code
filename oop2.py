class Person:
    def __init__(self, dob:str, name:str, gender:str, status:str, age:int):
        self.dob = dob
        self.name = name
        self.gender = gender
        self.status = status
        self.age = age

    def speak(self):
        print(f"Hello {self.name}")

    def walk(self):
        print("walking away")

    def get_name(self):
         print(self.name)

    def get_age(self):
         print(self.age) 

Person1 = Person("1997", "Ama Banku", "male", "single", 35)  
Person1.speak()
Person1.walk() 
Person1.get_name()
Person1.get_age()