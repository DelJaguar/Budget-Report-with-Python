import os
from time import sleep
from datetime import datetime
import csv
import matplotlib.pyplot as plt

################################################## IDEA NOTES!!! ####################################################################
#                                                                                                                                   #
#   Add ability to view purchase by week, by month, by year...                                                                      #
#   Add option to view money purchased on average per day                                                                           #
#####################################################################################################################################


#look to move DT/time into function instead of global variable

totalPurchases = 0.0
listPurchases = []




def main():
    clear()
    getMenu()
    exit()

# function to get files. deprecated.
# def getFiles():
    # pass

# function to clear the screen.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# function to wipe the ledger files.
def clearLedger():
    selection = input(
        'Select Y/y to clear the ledger. You cannot undo this!\t')
    if selection == 'y':
        print("\nClearing all purchases")
        sleep(5)
        os.remove('ledger.csv')
        clear()
        getMenu()
    else:
        getMenu()

# function to start program and bring up customer menu options to route the application.
def getMenu():
    menuSelection = ''

    while menuSelection != '5':

        menuSelection = input(
            "\nWhat do you want to do?\n\n1.) Record Purchase\n2.) View Money Spent\n3.) Define New category\n4.) Remove Purchase\n5.) Clear Ledger\n6.) Quit\n7.) Find Transaction\n\n")
        clear()
        menuAction(menuSelection)

# receives and process menu selection from cli input
def menuAction(menuSelection):
    global totalPurchases, listPurchases
    if menuSelection == '1':
        purchase()
        # totalPurchases, listPurchases = modifyPurchases(purchaseAmount, purchaseCategory)
        while 1 == 1:
            purchase()
        sleep(15)
    elif menuSelection == '2':
        viewMoneyReport()
    elif menuSelection == '3':
        changeCategory()
    elif menuSelection == '4':
        removePurchase()
    elif menuSelection == '5':
        clearLedger()
    elif menuSelection == '6':
        clear()
        quit()
    elif menuSelection == '7':
        clear()
        findPurchase()
    else:
        print("\n\nInvalid entry. Please try again.")

    clear()

# adds purchase to ledger
def purchase():
    global dt
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")
    
    count = 0
    clear()
    print("\nWelcome to the record purchase menu:\n\n")

    menuSelection = input(
        "Press 1 to record a purchase.\nPress Q to quit.\n\n")
    clear()
    if menuSelection == '1':
        purchaseAmount = input("\nInput cost:\t")
        clear()
        print("\nInput Category:\n\t1. Grocery \n\t2. Alcohol \n\t3. Pets \n\t4. Fun/Other")
        menuSelection = input("\nMake your selection: ")
        if menuSelection == '1':
            purchaseCategory = "Grocery"
            # section needs to be touched up so it can write to specific files and colums
            # Will need logic to write and move logic for search to it's own function 
            #
            # Commenting out file open to replace txt with a csv
            # with open(ledger, 'a') as f:
            #     f.write(f'{dt}, {purchaseAmount}, {purchaseCategory}\n')
            
            #see if we can move the csv write section to it's own function
            with open('ledger.csv', 'a') as f:
                reader = csv.reader(f)
                # next(reader, None)  # discard the header
               
                writer = csv.writer(f)
                writer.writerow([dt, purchaseAmount, purchaseCategory])
                sleep(5)
            return dt, purchaseAmount, purchaseCategory
        elif menuSelection == '2':
            purchaseCategory = "Alcohol"
            with open('ledger.csv', 'a') as f:
                reader = csv.reader(f)
                # next(reader, None)  # discard the header
               
                writer = csv.writer(f)
                writer.writerow([dt, purchaseAmount, purchaseCategory])
                sleep(5)
            return dt, purchaseAmount, purchaseCategory
        elif menuSelection == '3':
            purchaseCategory = "Pets"
            with open('ledger.csv', 'a') as f:
                reader = csv.reader(f)
                # next(reader, None)  # discard the header
               
                writer = csv.writer(f)
                writer.writerow([dt, purchaseAmount, purchaseCategory])
                sleep(5)
            return dt, purchaseAmount, purchaseCategory
        elif menuSelection == '4':
            purchaseCategory = "Fun/Other"
            with open('ledger.csv', 'a') as f:
                reader = csv.reader(f)
                # next(reader, None)  # discard the header
               
                writer = csv.writer(f)
                writer.writerow([dt, purchaseAmount, purchaseCategory])
                sleep(5)
            return dt, purchaseAmount, purchaseCategory
        else:
            print("Incorrect selection. Exiting entry...")
            getMenu()
    elif menuSelection.lower() == 'q':
        print("Exiting...")
        sleep(4)
        getMenu()
    else:
        print("Invalid Selection!")
        purchase()

# FIX ME: Currently no idexing for purchases. Function not usable.
#function to find purchase by field.
def findPurchase():
    count = 0
    print("Welcome to the find the purchase.\n")
    selection = input("Please input the date(DD/MM/YYYY), Purchase Amount or Purchase Category:\t")
    with open('ledger.csv', 'r') as f:
                reader = csv.reader(f)
                # next(reader, None)  # discard the header
                
                for row in reader:
                    count += 1
                    for field in row:
                        
                        if field.lower() == str(selection).lower():
                            print(row)

                sleep(5)
    


# determines if ledger file has contents and if it does it prints report.
def viewMoneyReport():
    cost = 0
    alcoholCost = 0
    groceryCost = 0 
    petsCost = 0
    otherCost = 0
    print("\nWelcome to the Report menu:\n\n")
    # print("Date/Time\t\t     Amount\t\tPurchase Category\n\n")
    if os.stat('ledger.csv').st_size != 0:
        with open('ledger.csv') as f:
            reader = csv.DictReader(f, fieldnames=("Time", "Price", "Category"))
            for row in reader:
                if row["Category"].lower() == "alcohol":
                    alcoholCost += float(row["Price"])
                if row["Category"].lower() == "grocery":
                    groceryCost += float(row["Price"])
                if row["Category"].lower() == "pets":
                    petsCost += float(row["Price"])
                if row["Category"].lower() == "fun/other":
                    otherCost += float(row["Price"])
                # newline = line.replace(',', ' ')
                # print(newline)
                cost += alcoholCost + groceryCost + otherCost + petsCost
            print(f'You spent ${alcoholCost} on Booze.\nYou spent ${groceryCost} on Groceries.\nYou spent ${petsCost} on Pets.\nYou spent ${otherCost} on other items.')
        print(f'Total amount spent: ${cost}.')
        labels = 'Alcohol', 'Grocery', 'Pets', 'Other'
        sizes = [alcoholCost, groceryCost, petsCost, otherCost]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()
    else:
        print("No transactions. Exiting...")
        sleep(10)

# FIX ME: not current ability to pull from category. Need to be able to be selected via a list or dict.
def changeCategory():
    print("\nWelcome to the Change Category menu:\n\n")
    sleep(2)
    pass

#need to add section to remove row. can use previous code from find purchase function?
def removePurchase():
    global listPurchases

    print(
        f'\nWelcome to the remove purchase menu:\n\nWhat purchase do you want to remove? {listPurchases}')
    selection = int(
        input("Pick dollar amount of the purchase you want to remove: "))
    # if selection in listPurchases:
    #     print(listPurchases.index(selection))
    # else:
    #     print("Error!!!")
    #     print(listPurchases[selection])
    print(listPurchases.index(selection))
    removePurchase()


def modifyPurchases(purchaseAmount, purchaseCategory):
    clear()
    global totalPurchases, listPurchases
    totalPurchases += purchaseAmount
    listPurchases.append([purchaseCategory, purchaseAmount])
    print(
        f'You have spent {totalPurchases} so far. Here is your list of purchases\n{listPurchases}')
    sleep(3)
    print("\nReturning to purchase Menu....")
    sleep(3)
    clear()
    return totalPurchases, listPurchases


main()
