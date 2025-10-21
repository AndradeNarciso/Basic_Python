from decorator import decorator
class listTestForString:
    list_String: str=[]
    
    @staticmethod
    def add_new_item(something: str):
        list.append(something)
        
    @staticmethod
    def count_all():
        return list.count()
    
    @staticmethod
    def remove_index_item(index: int):
        list.remove(index)
        
    