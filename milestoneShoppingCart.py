
items = []
item_price = []
new_item = ""
new_price = ""
action=""

print("Welcome to the Shopping Cart Program!")
while action != "5":
  print("")
  print("Please select one of the following(Please enter only numbers): \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit")

  action = input("Please enter an action: ")
  if action == "1":
      new_item = ""
      new_price = ""

      while new_item != "quit":
          print("")
          new_item = input("What item would you like to add? \n")
          if new_item == "quit":
            print("-------------------------------------------")
            print("Ok. we're backing to the main menu!")
            print("-------------------------------------------")

          else:
             print("")
             while True:
                  new_price = input(f"What is the price of '{new_item}'? (Please enter only numbers)\n")
                  try:
                      new_price = float(new_price)
                      items.append(new_item)
                      item_price.append(new_price)
                      print(f"{new_item} has been added to the cart.")
                      break  # If the value is a valid number, exit the loop
                  except ValueError:
                      print("Invalid input. Please enter only numbers.")


            # print("")
            # new_price = float(input(f"What is the price of '{new_item}'? (Please enter only numbers)\n"))
            # items.append(new_item)
            # item_price.append(new_price)
            # print(f"{new_item} has been added to the cart.")
  elif action == "2":
      print("")
      print("-------------------------------------------")
      print("The contents of the shopping cart are:")
      for i in range(len(items)):
          items_count = i+1
          print(f" {items_count}. {items[i]}: US$ {item_price[i]:,}")
      print("-------------------------------------------")
      print("")
print("Thank you. Goodbye.")
