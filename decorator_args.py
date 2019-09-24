def pre_decor(prefix):
    print("from pre_decor--->",prefix)
    def decorator_function(original_function):
        print("from decor_func---->",original_function.__name__,'\n')
        def wrapper_function(*args,**kwargs):
            print("from wrapper function")
            print(prefix,'executed before')
            result=original_function(*args,**kwargs)
            print(prefix,'executed after')
            print("from wrapper function")
            return result
        return wrapper_function
    return decorator_function
@pre_decor('log::')
def display_info(name,age):
    print('display_info ran with arguments({},{})'.format(name,age))
display_info('hima',28)
#display_info('himavardhan',14417)

    
        
