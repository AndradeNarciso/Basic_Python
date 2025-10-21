class Validation:
    
    @staticmethod
    def valid_age(age):
        while(age >60 or age <5):
            age=float(input("Invalid age (5-60), try again: "))
        
        return age
    
    @staticmethod 
    def input_option(option, min, max):
        while(option<min or option>max):
            option=int(input(f"Invalid option ({min}-{max})"))
        return option
    
    @staticmethod
    def valid_grade(grade):
        while(grade<1 or grade>10):
            grade=float(input("Invalid grade(1-10), try again: "))
        return grade