from ArgsAndKwargs import multInputFromUser

def main():
    sum_one =multInputFromUser.get_mult_param_args(12,32,43,45,65,34,64,34,4,54,12)
    sum_two =multInputFromUser.get_mult_param_kwargs(a=12,b=32,c=43,d=45,e=65,f=34,g=64,h=34,i=4,j=54,k=12)
    
    print(sum_one)
    print(sum_two)
    
main()