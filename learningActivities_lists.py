clients = ["Felipe", "Iana", "Gustavo", "Ysadora"]


new_clients = clients.append(input("Who is the new Client? "))

for client in clients:
    print(client)

#Working with lists of numbers
ages = [25, 29, 20, 15]

total_ages= 0

for age in ages:
    total_ages += age

print(total_ages)