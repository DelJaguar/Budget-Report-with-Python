import os
from time import sleep
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import tkinter as tk


LARGE_FONT = ("Verdana", 10)


class windowManager(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)            

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Purchases, MoneyReport, NewCategory, RemovePurchase, ClearLedger):


            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)


    def show_frame(self, cont):
        
        frame = self.frames[cont]                        
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="$$ Money Menu $$", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = tk.Button(self, text="Record Purchase", font=LARGE_FONT, command=lambda: controller.show_frame(Purchases), width=15)
        button.pack()
        
        button2 = tk.Button(self, text="Money Report", font=LARGE_FONT, command=lambda: controller.show_frame(MoneyReport), width=15)
        button2.pack()

        button3 = tk.Button(self, text="New Category", font=LARGE_FONT, command=lambda: controller.show_frame(NewCategory), width=15)
        button3.pack()

        button4 = tk.Button(self, text="Remove Purchase", font=LARGE_FONT, command=lambda: controller.show_frame(RemovePurchase), width=15)
        button4.pack()

        button5 = tk.Button(self, text="Clear Ledger", font=LARGE_FONT, command=lambda: controller.show_frame(ClearLedger), width=15)
        button5.pack()

        button6 = tk.Button(self, text="Quit", font=LARGE_FONT, command=quit, width=15)
        button6.pack()
   



class Purchases(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="$$ Purchase Menu $$", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        label = tk.Label(self, text="Cost", width=10)
        label.pack()

        inputtxt = tk.Entry(self, width=12)
        inputtxt.pack()

        label2 = tk.Label(self, text="Category")
        label2.pack()

        variable = tk.StringVar(self)
        variable.set("Grocery")

        w = tk.OptionMenu(self, variable, "Grocery", "Alcohol","Pets", "Fun/Other")
        w.pack()


        button = tk.Button(self, text="Record Purchase", font=LARGE_FONT, command=purchase, width=15)
        button.pack()
        
        button = tk.Button(self, text="Main Menu", font=LARGE_FONT, command=lambda: controller.show_frame(StartPage), width=15)
        button.pack()

class MoneyReport(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="$$ Report Menu $$", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        
        button = tk.Button(self, text="Generate Report", font=LARGE_FONT, command=viewMoneyReport, width=15)
        button.pack()
        
        button = tk.Button(self, text="Main Menu", font=LARGE_FONT, command=lambda: controller.show_frame(StartPage), width=15)
        button.pack()

class NewCategory(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="$$ Define New Category $$", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = tk.Button(self, text="New Category", font=LARGE_FONT, command=changeCategory, width=15)
        button.pack()
        
        button = tk.Button(self, text="Main Menu", font=LARGE_FONT, command=lambda: controller.show_frame(StartPage), width=15)
        button.pack()

class RemovePurchase(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="$$ Define New Category $$", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = tk.Button(self, text="Remove Purchase", font=LARGE_FONT, command=removePurchase, width=15)
        button.pack()
        
        button = tk.Button(self, text="Main Menu", font=LARGE_FONT, command=lambda: controller.show_frame(StartPage), width=15)
        button.pack()

class ClearLedger(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="$$ Clear Ledger $$", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = tk.Button(self, text="Clear Ledger", font=LARGE_FONT, command=clearLedger, width=15)
        button.pack()
        
        button = tk.Button(self, text="Main Menu", font=LARGE_FONT, command=lambda: controller.show_frame(StartPage), width=15)
        button.pack()


# function to clear the screen.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# function to wipe the ledger files.
def clearLedger():
    selection = input(
        'Select Y/y to clear the ledger. You cannot undo this!\t')
    if selection.lower == 'y':
        try:
            print("\nClearing all purchases")
            os.remove('ledger.csv')
            print("Purchases cleared")
        except:
            print("No purchases to clear")
        



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

            
            #see if we can move the csv write section to it's own function
            with open('ledger.csv', 'a') as f:
                reader = csv.reader(f)
                # next(reader, None)  # discard the header
               
                writer = csv.writer(f)
                writer.writerow([dt, purchaseAmount, purchaseCategory])
                sleep(5)
            purchase()
        elif menuSelection == '2':
            purchaseCategory = "Alcohol"
            with open('ledger.csv', 'a') as f:
                reader = csv.reader(f)
                # next(reader, None)  # discard the header
               
                writer = csv.writer(f)
                writer.writerow([dt, purchaseAmount, purchaseCategory])
                # sleep(5)
            purchase()
        elif menuSelection == '3':
            purchaseCategory = "Pets"
            with open('ledger.csv', 'a') as f:
                reader = csv.reader(f)
                # next(reader, None)  # discard the header
               
                writer = csv.writer(f)
                writer.writerow([dt, purchaseAmount, purchaseCategory])
                sleep(5)
            purchase()
        elif menuSelection == '4':
            purchaseCategory = "Fun/Other"
            with open('ledger.csv', 'a') as f:
                reader = csv.reader(f)
                # next(reader, None)  # discard the header
               
                writer = csv.writer(f)
                writer.writerow([dt, purchaseAmount, purchaseCategory])
                sleep(5)
            purchase()
        else:
            print("Incorrect selection. Exiting entry...")
            getMenu()
    elif menuSelection.lower() == 'q':
        print("Exiting...")
        sleep(4)
        
    else:
        print("Invalid Selection!")
        purchase()



# determines if ledger file has contents and if it does it prints report.
# need to fix pie chart to make it more readable.
def viewMoneyReport():
    cost = 0
    alcoholCost = 0
    groceryCost = 0 
    petsCost = 0
    otherCost = 0
    print("\nWelcome to the Report menu:\n\n")
    # print("Date/Time\t\t     Amount\t\tPurchase Category\n\n")
    try:
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
            ax1.pie(sizes, labels=labels, autopct='%.0f%%')
            # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            plt.show()
        
    except:
        print("No transactions. Exiting...")
        sleep(5)
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

    print(listPurchases.index(selection))
    removePurchase()




# will use to read file and copy contents to ledger.csv file
# need to add ability to check that number of columns
# need to add check that field contents are correct type
def importPurchases():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)
    reader = csv.reader(f, filename)
    num_cols = 3
    with open(filename) as f:
        if num_cols == len(reader.next()): 
            for row in f.readlines():
                print(row)
        else:
            print("Error!!")
    sleep(3)


def main():
    app = windowManager()
    app.mainloop()

if __name__ =="__main__":
    main()
