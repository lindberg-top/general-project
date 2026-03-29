# class Human:
#     name = None
#     age = None
#     country = None
    
#     def __init__(self, name, age, country = None):
#         self.name = name
#         self.age = age
#         self.country = country
        
#         self.set_data()
        
        
#     def set_data(self):
#         print("Моё имя: ", self.name, "Возраст: ", self.age, "Страна: ", self.country)
                  

# human1 = Human("Nikolay", 20, "Russian Federation")
# human2 = Human("Sofia", 20, "Hungary")

# human1.__init__("Nikolay", 20)

class Building():
    year = None
    city = None
    
    def __init__(self, year, city):
        self.year = year
        self.city = city
        
        
    def get_info(self):
        print("Year:", self.year, "City:", self.city)
        


class School(Building):
    pass
    
class House(Building):
    pass
    
class Shop(Building):
    pass

    
            
school = School(2000, "Moscow")
school.get_info()
house = House(2000, "Moscow")
shop = Shop(2000, "Moscow")
        