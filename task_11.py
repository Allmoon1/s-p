class Dessert:
    def __init__(self, name="", calories=0):
        self.__name = name
        self.__calories = calories

    def name(self):
        return self.__name

    def name(self, new_name):
        self.__name = new_name

    def calories(self):
        return self.__calories

    def calories(self, new_calories):
        self.__calories = new_calories

    def is_healthy(self):
        if self.calories < 200:
            return True
        return False

    def is_delicious(self):
        return True





dessert = Dessert()
dessert.name = "test_name"
print(dessert.name)
dessert.name = "test_name2"
print(dessert.name)
if dessert.name != "test_name2": raise Exception("Setter for name is not working")
dessert.calories = "test_calories"
print(dessert.calories)
dessert.calories = "test_calories2"
print(dessert.calories)
if dessert.calories != "test_calories2": raise Exception("Setter for calories is not working")
print(dessert.is_delicious())
if not dessert.is_delicious(): raise Exception("Invalid method result")
print(dessert.is_healthy())
dessert.calories = 300
print(dessert.calories)
print(dessert.is_healthy())
if dessert.is_healthy(): raise Exception("Logical error. Method must return False")

