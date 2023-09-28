class Dessert:
    def __init__(self, name="", calories=0):
        self._name = name
        self._calories = calories

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_calories(self):
        return self._calories

    def set_calories(self, new_calories):
        self._calories = new_calories

    def is_healthy(self):
        return self._calories < 200

    def is_delicious(self):
        return True


#dessert1 = Dessert("Jam", 1350)
#dessert2 = Dessert("Salad", 150)

#print("Is Dessert 1 healthy?", dessert1.is_healthy())
#print("Is Dessert 1 delicious?", dessert1.is_delicious())

#print("Is Dessert 2 healthy?", dessert2.is_healthy())
#print("Is Dessert 2 delicious?", dessert2.is_delicious())
