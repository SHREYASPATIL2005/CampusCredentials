def food(d):
    print(d)
    print(d.get(2, "No item found"))



d = {1:"Pizza", 2:"Burger", 3:"Pasta"}
food(d)

def funNihal():
    return "Lenovo"


def shivam():
    laptop = funNihal()
    print("from nihal:", laptop) # Lenovo

def hassan():
    pass

shivam()