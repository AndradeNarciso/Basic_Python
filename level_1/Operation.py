

class Operation:

    studants = [] #BD
    length=0

    @staticmethod
    def add_studant(studant):
        Operation.studants.append(studant)
        Operation.length+=1
     
    @staticmethod   
    def   get_all_studante():
        for i in Operation.studants:
            print(f"Name: {i.get_name()}\nAge: {i.get_age()} \nGrade: {i.get_grade()}\n\n\n")
      
    @staticmethod      
    def averege():
        avr=0
        for i in Operation.studants:
            avr+=i.get_grade()
            
        return avr/Operation.length
    
    @staticmethod 
    def search_studante(name):
        is_there=False
        for i in Operation.studants:
            if(i.get_name==name):
                is_there=True
                return f"Name: {i.get_name()}\nAge: {i.get_age()} \n Grade: {i.get_grade()}\n\n\n"
        
        if(is_there):
            return f" Student {name} was not found"
        