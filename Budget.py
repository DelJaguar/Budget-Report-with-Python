import os
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk


LARGE_FONT = ("Verdana", 10)
# FIX ME importPurchases function doesn't import and write file to ledger.csv that needs to be further developed.

class windowManager(tk.Tk):
    
    def __init__(self, *args, **kwargs):


        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="moneybag.ico")
        tk.Tk.wm_title(self, "Budget")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)            
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Purchases, MoneyReport, NewCategory, RemovePurchase, ClearLedger, LedgerCleared):


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
        
        button = ttk.Button(self, text="Record Purchase", command=lambda: controller.show_frame(Purchases), width=15)
        button.pack()
        
        button2 = ttk.Button(self, text="Money Report", command=lambda: controller.show_frame(MoneyReport), width=15)
        button2.pack()

        button3 = ttk.Button(self, text="New Category", command=lambda: controller.show_frame(NewCategory), width=15)
        button3.pack()

        button4 = ttk.Button(self, text="Remove Purchase", command=lambda: controller.show_frame(RemovePurchase), width=15)
        button4.pack()

        button5 = ttk.Button(self, text="Clear Ledger", command=lambda: controller.show_frame(ClearLedger), width=15)
        button5.pack()

        button6 = ttk.Button(self, text="Quit", command=quit, width=15)
        button6.pack()
   



class Purchases(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="$$ Purchase Menu $$", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        label = ttk.Label(self, text="Cost", width=10)
        label.pack()

        inputtxt = ttk.Entry(self, width=12)
        inputtxt.pack()

        label2 = tk.Label(self, text="Category")
        label2.pack()

        variable = tk.StringVar(self)
        variable.set("Grocery")

        w = ttk.OptionMenu(self, variable, "Grocery", "Alcohol","Pets", "Fun/Other")
        w.pack()


        button = ttk.Button(self, text="Record Purchase", command=getEntry, width=15)
        button.pack()
        
        button = ttk.Button(self, text="Main Menu", command=lambda: controller.show_frame(StartPage), width=15)
        button.pack()

class MoneyReport(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="$$ Report Menu $$", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        
        button = ttk.Button(self, text="Generate Report", command=viewMoneyReport, width=15)
        button.pack()
        
        button = ttk.Button(self, text="Main Menu", command=lambda: controller.show_frame(StartPage), width=15)
        button.pack()

class NewCategory(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="$$ Define New Category $$", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = ttk.Button(self, text="New Category", command=changeCategory, width=15)
        button.pack()
        
        button = ttk.Button(self, text="Main Menu", command=lambda: controller.show_frame(StartPage), width=15)
        button.pack()

class RemovePurchase(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="$$ Define New Category $$", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = ttk.Button(self, text="Remove Purchase", command=removePurchase, width=15)
        button.pack()
        
        button = ttk.Button(self, text="Main Menu",  command=lambda: controller.show_frame(StartPage), width=15)
        button.pack()

class ClearLedger(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="$$ Clear Ledger $$", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = ttk.Button(self, text="Yes", command=lambda: [clearLedger("y"),controller.show_frame(LedgerCleared)], width=5)
        
        button.pack()
        
        button2 = ttk.Button(self, text="No", command=lambda: controller.show_frame(StartPage), width=5)
        button2.pack()

class LedgerCleared(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Ledger Cleared!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Main Menu", command=lambda: [clearLedger("y"),controller.show_frame(StartPage)])
        button.pack()

def main():
    app = windowManager()
    app.mainloop()


def getEntry():
    e_text=tk.Entry.get()
    print(e_text)




# function to clear the screen.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# function to wipe the ledger files.
def clearLedger(selection):
    
    if selection.lower() == 'y':
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
                
            purchase()
        elif menuSelection == '2':
            purchaseCategory = "Alcohol"
            with open('ledger.csv', 'a') as f:
                reader = csv.reader(f)
                # next(reader, None)  # discard the header
               
                writer = csv.writer(f)
                writer.writerow([dt, purchaseAmount, purchaseCategory])
                
            purchase()
        elif menuSelection == '3':
            purchaseCategory = "Pets"
            with open('ledger.csv', 'a') as f:
                reader = csv.reader(f)
                # next(reader, None)  # discard the header
               
                writer = csv.writer(f)
                writer.writerow([dt, purchaseAmount, purchaseCategory])
                
            purchase()
        elif menuSelection == '4':
            purchaseCategory = "Fun/Other"
            with open('ledger.csv', 'a') as f:
                reader = csv.reader(f)
                # next(reader, None)  # discard the header
               
                writer = csv.writer(f)
                writer.writerow([dt, purchaseAmount, purchaseCategory])
                
            purchase()
        else:
            print("Incorrect selection. Exiting entry...")
            getMenu()
    elif menuSelection.lower() == 'q':
        print("Exiting...")
        
        
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
        
# FIX ME: not current ability to pull from category. Need to be able to be selected via a list or dict.
def changeCategory():
    print("\nWelcome to the Change Category menu:\n\n")
    
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
    

if __name__ =="__main__":
    main()
