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

class JellyBean(Dessert):
    def __init__(self, name, calories, flavor=None):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def is_delicious(self):
        return self._flavor != "black licorice"


#jelly_bean = JellyBean("Cherry Jelly Bean", 20, "cherry")
#print(jelly_bean.is_delicious())  

#jelly_bean.flavor = "black licorice"
#print(jelly_bean.is_delicious())  