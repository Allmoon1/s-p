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
        if type(self.calories) == str or self.calories < 200:
            return True
        return False

    def is_delicious(self):
        return True

class JellyBean(Dessert):
    def __init__(self, name = None, calories = None, flavor=None):
        super().__init__(name, calories)
        self.__flavor = flavor

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, value):
        self.__flavor = value

    def is_delicious(self):
        return self.__flavor != "black licorice"


#jelly_bean = JellyBean("Cherry Jelly Bean", 20, "cherry")
#print(jelly_bean.is_delicious())  

#jelly_bean.flavor = "black licorice"
#print(jelly_bean.is_delicious())  