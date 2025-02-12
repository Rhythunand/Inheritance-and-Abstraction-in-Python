class Shapes :
  print("Enter the number of the shape that you want the area of")
  print("If you want to get he perimeter type 5")
  print("1.Square")
  print("2.Rectangle")
  print("3.Triangle")
  print("4.Circle")
  user = input()

  if user not in ['1', '2', '3', '4', '5'] :
    print("Invalid response enter the number that your is written before your shape")

  else :
    user = int(user)

  if user == 1 :
    num1 = int(input("Enter the lengh of a side in your square : "))
    print(num1*num1)

  elif user == 2 :
    num1 = int(input("Enter the height of your rectangle : "))
    num2 = int(input("Enter the  width of your rectangle: "))
    print(num1*num2)
  
  elif user == 3 :
    num1 = int(input("Enter the height of your triangle"))
    num2 = int(input("Enter the base of your triangle"))
    print(num1*num2/2)
  elif user == 4 :
    num1 = int(input("Enter the radius for your circle : "))
    print(3.14*num1*num1)

  elif user == 5 :
    print("Which shape do you want the perimeter of ")
    user_choice = input()
    if user_choice not in ['1', '2', '3', '4'] :
      print("Invalid response enter the number that your is written before your shape")

    else :
      user_choice = int(user_choice)

    if user_choice == 1 :
      num1 = int(input("Enter the length of a side in your square : "))
      print(num1*4)

    elif user_choice == 2 :
      num1 = int(input("Enter the height of your rectangle : "))
      num2 = int(input("Enter the  width of your rectangle: "))
      print(2*(num1+num2))

    elif user_choice == 3 :
      num1 = int(input("Enter the side of your triangle"))
      num2 = int(input("Enter the other side of your triangle"))
      num3 = int(input("Enter the base of your triangle"))
      print(num1+num2+num3)

    elif user_choice == 4 :
      num1 = int(input("Enter the radius for your circle : "))
      print(3.14*2*num1)
   
obj = Shapes()
print(obj)