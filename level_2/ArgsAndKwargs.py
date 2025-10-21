class multInputFromUser:
    
    @staticmethod
    def get_mult_param_args(*mult_input: int )->int:
        sum=0
        for i in mult_input:
            sum+=i
        
        return sum
    
    @staticmethod
    def get_mult_param_kwargs(**mult_input: int)-> int:
        sum=0
        for i in mult_input.values():
            sum+=i
            
        return sum
