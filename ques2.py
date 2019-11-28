try:
    n=int(input('Enter no.: ')) + input()
    
    n.count()

    

except(AttributeError):
    print('OOPS! Attribute Error Occured')

except(TypeError):
    print('OOPS! Type Error Occured')

except(ValueError):
    print('OOPS! Value Error Occured')

   
