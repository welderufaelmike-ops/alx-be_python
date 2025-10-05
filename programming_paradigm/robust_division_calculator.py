def safe_divide(numerator=5, denominator=5):
    
    try:
       
       numerator=float(numerator)
       denominator=float(denominator)
       result= numerator / denominator
       return F"The result of the division is {result}" 
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
print(safe_divide())
    

    
