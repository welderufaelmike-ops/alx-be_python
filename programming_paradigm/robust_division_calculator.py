def safe_divide(numerator, denominator):
    '''' 
    Divides the numerator by the denominator.

    Args:
        nomenmetor (float or int): The numerator.
        denemonetor (float or int): The denominator.

    Returns:
        float: The result of the division.
    
    Raises:
        ZeroDivisionError: If the denominator is zero. '''
    
    try:
       return  numerator / denominator
    except ZeroDivisionError :
        print("Error: cannot divide by zero" )
        
    except TypeError:
        print("Error: Please enter numeric values only." )
        return numerator /denominator 

    
