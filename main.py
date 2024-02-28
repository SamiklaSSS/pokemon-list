import csv

apartments = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('jurmala.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        apartments.append(row)

# remove header row
apartments.pop(0)

# print(apartments)

n = 1 -2

Ch = 0
Ex = 0

def Hprice (apartments):
    323 > n
    n = n +1
    return apartments[n][8]

def Lprice (apartments):
    323 > n
    n = n +1
    return apartments[n][8]



while True:
    print("1. Get apartments by sequence number")
    print("2. Top 10 by highest price")
    print("3. Top 10 by lowest price")
    print("4. 20 items, cheaper than price")
    print("5. 20 items, expensive than price")
    print("6. -- Filter of your choice --")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        print(apartments)
        # https://www.w3schools.com/python/python_lists_access.asp
        pass
    elif choice == '2':
        apartments.sort(key = Hprice)
        print(apartments[:10])
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '3':
        apartments.sort(key = Lprice)
        print(apartments[-10:])
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
        Ch = input("Cheaper than what price, apartments are you searching for?")
        newlistCh = []
        for apartment in apartments:
            323 > n
            n = n +1
            if Ch < apartment[n][8]:
                newlistCh.append(apartment)
        print(newlistCh[:20])
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        pass
    elif choice == '5':
        Ex = input("More expencive than what price, apartments are you searching for?")
        newlistEx = []
        for apartment in apartments:
            323 > n
            n = n +1
            if Ex > apartment[n][8]:
                newlistEx.append(apartment)
        print(newlistEx[-20:])
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        pass

    elif choice == '6':
        print("Error - ???")
        pass
    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 7")

    print("==========================")
