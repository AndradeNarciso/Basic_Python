from Operation import Operation
from Validation import Validation
from Studant import Studant

class Classroom:
   

    @staticmethod
    def menu():

        while(True):
            print("""
            ==== School System ====
            1. Add student
            2. List all student
            3. Global averege
            4. Search for studant
            5. exit
            """)
            input_user= Validation.input_option( int(input("input an option: ")),1,5)

         

            match input_user:
                case 1:
                    name=input("input his/her name: ")
                    age=Validation.valid_age(int(input("input his/her age: ")))
                    grade=Validation.valid_grade(float(input("iput his/her grade; ")))
                    new_studant=Studant(name,age,grade)
                    
                    Operation.add_studant(new_studant)
                case 2:
                    print("All Students: ")
                    Operation.get_all_studante()
                case 3: 
                    print(f" the averege is: {Operation.averege()}")
                case 4: 
                    name=str(input("Input who you looking for: "))
                    Operation.search_studant(name)
                case 5:
                    print("see you next time")
                    break
                
    
          