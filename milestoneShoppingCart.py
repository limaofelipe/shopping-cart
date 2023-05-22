# As a creativity criterion this week, in addition to making the project, I put requirements for certain questions to accept only certain types of characters.
# for example:
# What item would you like to add? (type 'quit' to return to main menu)
# In this question only numbers are accepted, I cannot write "10" but I can write 10 perfumes.
# and so the code works accepting only specific characters from each question

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
        while True:
            new_item = input("What item would you like to add? (type 'quit' to return to main menu) \n")
            if any(c.isalpha() for c in new_item) and new_item.strip().replace(" ", "").isalnum():
                break
            else:
                print("Invalid input. Please enter only words.")
        # new_item = input("What item would you like to add? (type 'quit' to return to main menu) \n")
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
  
  elif action =="3":
      print("-------------------------------------------")
      print("These are the items in your cart: \n")
      for i in range(len(items)):
          items_count = i+1
          print(f" {items_count}. {items[i]}: US$ {item_price[i]:,}")
      while True:
            remove_item = int(input("What item would you like to remove? (Please type only numbers) "))
            array_quantity = len(items)
            try:
                if remove_item > 0 and remove_item <= array_quantity:
                    remove_item = int(remove_item)
                    break
                else:
                    print('')
                    print("Please type a valid value:")
                    for i in range(len(items)):
                        items_count = i+1
                        print(f" {items_count}. {items[i]}: US$ {item_price[i]:,}")
                    print('')
            except ValueError:
                print("Invalid input. Please enter only numbers.")
      print(f"{items[remove_item - 1]} was removed")
      items.pop(remove_item - 1)
      item_price.pop(remove_item - 1)
  elif action == "4":
      total_amount = 0
      for price in item_price:
        total_amount = total_amount + price
      print(f"The total price of the items in the shopping cart is U$ {total_amount}")

print("Thank you. Goodbye.")
