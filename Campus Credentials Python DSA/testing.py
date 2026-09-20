def food(d):
    print(d)
    # Original lookup raised KeyError when key 2 was absent:
    # print(d[2])
    print(d.get(2, "No item found"))



d = {1:"Pizza", 2:"Burger", 3:"Pasta"}
food(d)

def funNihal():
    # Original nested function was never called and returned None:
    # @staticmethod
    # def funNihal():
    #     return "Lenovo"
    return "Lenovo"


def shivam():
    laptop = funNihal()
    print("from nihal:", laptop) # Lenovo

def hassan():
    pass

shivam()