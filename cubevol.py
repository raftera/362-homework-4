def volume(side1, side2, side3):

    if side1.isnumeric() and side2.isnumeric() and side3.isnumeric():


     if side1 < 1:
            print("No side can be less than 1.")
            return 0
     if side2 < 1:
            print("No side can be less than 1.")
            return 0
     if side3 < 1:
            print("No side can be less than 1.")
            return 0

     return side1*side2*side3

    else:
         print("All inputs must be ints.")
         return 0

    