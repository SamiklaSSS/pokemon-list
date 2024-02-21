
import csv

pokemons = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

# print(pokemons)

print("Pokemon list command:")

while True:
    print("1. Get Pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by text in name")
    print("5. Search by length of name")
    print("6. First 10 Pokemons")
    print("7. Last 10 Pokemons")
    print("8. List of 10 Pokemons") #nav pabeigta
    print("9. Exit")
    print("Please write everything with the big first letter!!!")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        # https://www.w3schools.com/python/python_lists_access.asp
        print(pokemons[int(input("Enter Pokemon's number!"))-1])
        pass
    
    elif choice == '2':
        # https://www.w3schools.com/python/python_lists_sort.asp
        pokemons.sort()
        print(pokemons)
        pass
    
    elif choice == '3':
        # https://www.w3schools.com/python/python_lists_sort.asp
        pokemons.reverse()
        print(pokemons)
        pass
    
    elif choice == '4':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/ref_string_startswith.asp
        txt = input("Enter Pokemon's name or part of the name!")
        newlist = []
        for pokemon in pokemons:
            if txt in pokemon:
                newlist.append(pokemon)
        print(newlist)
        pass
    
    elif choice == '5':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        len_txt = input("Enter Pokemon's name's length!")
        newlist = []
        for pokemon in pokemons: 
           if int(len_txt) == int(len(pokemon)):
               newlist.append(pokemon)
        print(newlist)
        pass

    elif choice == '6':
        print(pokemons[:10])
        pass

    elif choice == '7':
        print(pokemons[-10:])
        pass
    
    elif choice == '8': #nav pabeigta
        a = 0
        b = 10
        b < 801
        print(pokemons[a:b])
        choice2 = input("If you want to continue the list enter 'n', if not enter 'q'!")
        while choice2 == 'n':
         input("You really want to conyinue the list?")
         if choice2 == 'Yes':
             a = a + 10
             b = b + 10
         print(pokemons[a:b])
        pass

    elif choice == '9':
        print("Exiting")
        break
    
    else:
        print("Invalid choice, choose from 1 to 8")

    print("==========================")

