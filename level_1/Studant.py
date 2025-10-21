class Studant:
    def __init__(self,name, age, grade):
        self.__name=name
        self.__age=age
        self.__grade=grade
    
    def get_name(self):
        return self.__name
    
    def get_grade(self):
        return self.__grade
        
    def get_age(self):
        return self.__age
           
    