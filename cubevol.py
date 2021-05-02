def volume(side1, side2, side3):

    if isinstance(side1, int) and isinstance(side1, int) and isinstance(side3, int):


     if side1 < 1:
          #  print("No side can be less than 1.")
            return 0
     if side2 < 1:
        #    print("No side can be less than 1.")
            return 0
     if side3 < 1:
         #   print("No side can be less than 1.")
            return 0

     return side1*side2*side3

    else:
     #    print("All inputs must be ints.")
         return 0

    