print("Welcome User!\nIm your personal store assistant")
print("\nCan you provide me with your name to best assist you?")

username = input("")
print("\nHello " + username + "!")

age = input("How old are you?")
#print("\nYou are " + age + " years old!")
def display_options():
  print("\nHow may I assist you today?")
  print(username + ", you can ask me to view the following:")
  print("1:Products")
  print("2:Price")
  print("3:Add to Cart")
  print("4:View Cart")
  print("5:Checkout")
  print("6:Exit")



def user_choice():
  choice = input("Enter your choice: ")
  if choice == "1":
    print("Here are the products we have in stock:")
  elif choice == "2":
   print("Here are the prices:")
  elif choice == "3":
    print("Here is your cart:")
  elif choice == "4":
    print("Here are the items in your cart:")
  elif choice == "5":
    print("Here is your receipt:")
  elif choice == "6":
    print("Thank you for using our services! " + username)
  else:
    print("Invalid input.Enter a number from 1-6")



display_options()
user_choice()
