#Accessing items in a list via their index
clients = ["Felipe", "Iana", "Gustavo", "Ysadora"]

index = int(input("Which index would you like to get? "))
user_choice = clients[index] # gets the item at the index the user typed

print(user_choice)

#Finding the size of the list
number_of_clients = len(clients)

for client in range(len(clients)):
    client = clients[client]
    print(clients) # print each client to the screen.
    
#Printing indexes
for i in range(len(clients)):
    client = clients[i]
    print(f"{i}. {client}")