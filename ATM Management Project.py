import tkinter as GUI
from tkinter import messagebox

class Account:
    def __init__(self,ID,name,password,balance):
        self.ID=ID
        self.name=name
        self.password=password
        self.balance=balance
        self.locked=False

    def check_password(self,password):
        if self.locked:
            return False
        return self.password==password

    def lock_account(self):
        self.locked=True

    def withdraw(self,amount):
        if amount>self.balance:
            return False
        self.balance-=amount
        return True

    def get_balance(self):
        return self.balance

    def change_password(self, new_password):
        self.password=new_password


class ATM:
    def __init__(self):
        self.accounts=[]

    def add_account(self,account):
        self.accounts.append(account)

    def account_login(self,account_number):
        for account in self.accounts:
            if account.ID==account_number:
                return account
        return None


class ATMInterface:
    def __init__(self,atm):
        self.atm=atm
        self.current_account=None
        self.password_attempts=0

        self.main_window=GUI.Tk()
        self.main_window.title("ATM")
        self.main_window.geometry("400x300")

        self.label_account=GUI.Label(self.main_window,text="Account number:")
        self.label_account.pack()

        self.entry_account=GUI.Entry(self.main_window)
        self.entry_account.pack()

        self.button_enter=GUI.Button(self.main_window,text="Enter",command=self.enter_account_number)
        self.button_enter.pack()

    def enter_account_number(self):
        account_number=int(self.entry_account.get())
        account=self.atm.account_login(account_number)
        if account is None:
            GUI.messagebox.showerror("Error", "Account number not identified.")
        else:
            self.current_account=account
            self.password_attempts=0
            self.enter_password()

    def enter_password(self):
        self.main_window.destroy()

        self.main_window=GUI.Tk()
        self.main_window.title("ATM")
        self.main_window.geometry("400x300")

        self.label_password=GUI.Label(self.main_window,text="Enter your password:")
        self.label_password.pack()

        self.entry_password=GUI.Entry(self.main_window,show="*")
        self.entry_password.pack()

        self.button_login=GUI.Button(self.main_window,text="Login",command=self.check_password)
        self.button_login.pack()

    def check_password(self):
        password=self.entry_password.get()
        if self.current_account.check_password(password):
            self.show_menu()
        else:
            self.password_attempts+=1
            if self.password_attempts>=3:
                self.current_account.lock_account()
                GUI.messagebox.showerror("Account Locked","Account locked. Please go to the branch.")
            else:
                GUI.messagebox.showerror("Incorrect Password","Incorrect password. Please try again.")
                self.entry_password.delete(0,GUI.END)

    def show_menu(self):
        self.main_window.destroy()

        self.main_window=GUI.Tk()
        self.main_window.title("ATM")
        self.main_window.geometry("400x300")

        self.label_welcome=GUI.Label(self.main_window,text="Welcome, {}!".format(self.current_account.name))
        self.label_welcome.pack()

        self.label_options=GUI.Label(self.main_window, text="Options:")
        self.label_options.pack()

        self.button_withdraw=GUI.Button(self.main_window, text="Cash Withdraw",command=self.cash_withdraw)
        self.button_withdraw.pack()

        self.button_balance=GUI.Button(self.main_window, text="Balance Inquiry",command=self.balance_inquiry)
        self.button_balance.pack()

        self.button_change_password=GUI.Button(self.main_window, text="Password Change",command=self.password_change)
        self.button_change_password.pack()

        self.button_fawry=GUI.Button(self.main_window, text="Fawry Service", command=self.fawry_service)
        self.button_fawry.pack()

        self.button_exit=GUI.Button(self.main_window, text="Exit",command=self.exit)
        self.button_exit.pack()

    def cash_withdraw(self):
        self.main_window.destroy()

        self.main_window=GUI.Tk()
        self.main_window.title("ATM")
        self.main_window.geometry("400x300")

        self.label_withdraw=GUI.Label(self.main_window,text="Enter amount to withdraw:")
        self.label_withdraw.pack()

        self.entry_withdraw=GUI.Entry(self.main_window)
        self.entry_withdraw.pack()

        self.button_withdraw=GUI.Button(self.main_window, text="Withdraw",command=self.perform_withdraw)
        self.button_withdraw.pack()

    def perform_withdraw(self):
        amount=int(self.entry_withdraw.get())
        if amount>5000:
            GUI.messagebox.showerror("Exceeded the maximum amount", "You have exceeded the maximum amount.")
        elif (amount!=(1*100)) and (amount!=(2*100)) and (amount!=(3*100)) and (amount!=(4*100)) and (amount!=(5*100)) and (amount!=(6*100)) and (amount!=(7*100)) and (amount!=(8*100)) and (amount!=(9*100)) and (amount!=(10*100)) and (amount!=(11*100)) and (amount!=(12*100)) and (amount!=(13*100)) and (amount!=(14*100)) and (amount!=(15*100)) and (amount!=(16*100)) and (amount!=(17*100)) and (amount!=(18*100)) and (amount!=(19*100)) and (amount!=(20*100)) and (amount!=(21*100)) and (amount!=(22*100)) and (amount!=(23*100)) and (amount!=(24*100)) and (amount!=(25*100)) and (amount!=(26*100)) and (amount!=(27*100)) and (amount!=(28*100)) and (amount!=(29*100)) and (amount!=(30*100)) and (amount!=(31*100)) and (amount!=(32*100)) and (amount!=(33*100)) and (amount!=(34*100)) and (amount!=(35*100)) and (amount!=(36*100)) and (amount!=(37*100)) and (amount!=(38*100)) and (amount!=(39*100)) and (amount!=(40*100)) and (amount!=(41*100)) and (amount!=(42*100)) and (amount!=(43*100)) and (amount!=(44*100)) and (amount!=(45*100)) and (amount!=(46*100)) and (amount!=(47*100)) and (amount!=(48*100)) and (amount!=(49*100)) and (amount!=(50*100)):
            GUI.messagebox.showerror("Error","The allowed values are multiple of 100 L.E") 
        elif self.current_account.withdraw(amount):
            GUI.messagebox.showinfo("Withdrawal Successful","Withdrawal successful.")
        else:
            GUI.messagebox.showerror("Insufficient Balance","Insufficient balance.")
            
        
        GUI.messagebox.showinfo("Thank You","Thank you for using our ATM. Goodbye!")
        self.show_menu()
        
        
        
    
    def balance_inquiry(self):
        balance=self.current_account.get_balance()
        GUI.messagebox.showinfo("Balance Inquiry","Current balance: {}".format(balance))

    def password_change(self):
        self.main_window.destroy()

        self.main_window=GUI.Tk()
        self.main_window.title("ATM")
        self.main_window.geometry("400x300")

        self.label_new_password=GUI.Label(self.main_window,text="Enter new password:")
        self.label_new_password.pack()

        self.entry_new_password=GUI.Entry(self.main_window,show="*")
        self.entry_new_password.pack()

        self.button_change_password=GUI.Button(self.main_window,text="Change Password",command=self.perform_password_change)
        self.button_change_password.pack()

    def perform_password_change(self):
        new_password=self.entry_new_password.get()
        self.current_account.change_password(new_password)
        GUI.messagebox.showinfo("Password Change", "Password changed successfully.")
        self.show_menu()
    
    def fawry_service(self):
        self.main_window.destroy()

        self.main_window=GUI.Tk()
        self.main_window.title("ATM")
        self.main_window.geometry("400x300")

        self.label_Phone_number=GUI.Label(self.main_window,text="Enter your phone number")
        self.label_Phone_number.pack()

        self.entry_Phone_number=GUI.Entry(self.main_window)
        self.entry_Phone_number.pack()

        self.label_recharge=GUI.Label(self.main_window,text="Enter amount to recharge:")
        self.label_recharge.pack()

        self.entry_recharge=GUI.Entry(self.main_window)
        self.entry_recharge.pack()

        self.button_Orange=GUI.Button(self.main_window, text="Orange Recharge",command=self.perform_recharge_orange)
        self.button_Orange.pack()

        self.button_Etisalat=GUI.Button(self.main_window, text="Etisalat Recharge",command=self.perform_recharge_etisalat)
        self.button_Etisalat.pack()

        self.button_Vodafone=GUI.Button(self.main_window, text="Vodafone Recharge",command=self.perform_recharge_vodafone)
        self.button_Vodafone.pack()

        self.button_We=GUI.Button(self.main_window, text="We Recharge",command=self.perform_recharge_we)
        self.button_We.pack()

    def perform_recharge_orange(self):
        phone_number=self.entry_Phone_number.get()
        amount=int(self.entry_recharge.get())

        if len(phone_number) !=11 or not phone_number.startswith("012"):
            GUI.messagebox.showerror("Invalid Phone Number", "Please enter a valid Orange phone number starting with '012' and is exactly 11 characters long.")
        else:
            self.perform_recharge(phone_number,amount)

    def perform_recharge_etisalat(self):
        phone_number=self.entry_Phone_number.get()
        amount=int(self.entry_recharge.get())

        if len(phone_number) !=11 or not phone_number.startswith("011"):
            GUI.messagebox.showerror("Invalid Phone Number", "Please enter a valid Etisalat phone number starting with '011' and is exactly 11 characters long.")
        else:
            self.perform_recharge(phone_number,amount)

    def perform_recharge_vodafone(self):
        phone_number=self.entry_Phone_number.get()
        amount=int(self.entry_recharge.get())

        if len(phone_number) !=11 or not phone_number.startswith("010"):
            GUI.messagebox.showerror("Invalid Phone Number", "Please enter a valid Vodafone phone number starting with '010' and is exactly 11 characters long.")
        else:
            self.perform_recharge(phone_number,amount)

    def perform_recharge_we(self):
        phone_number=self.entry_Phone_number.get()
        amount=int(self.entry_recharge.get())

        if len(phone_number) !=11 or not phone_number.startswith("015"):
            GUI.messagebox.showerror("Invalid Phone Number", "Please enter a valid We phone number starting with '015' and is exactly 11 characters long.")
        else:
            self.perform_recharge(phone_number,amount)


    def perform_recharge(self,phone_number,amount):

        if self.current_account.withdraw(amount):
            GUI.messagebox.showinfo("Recharge Successful", "Recharge successful.")
        else:
            GUI.messagebox.showerror("Insufficient Balance", "Insufficient balance.")

        GUI.messagebox.showinfo("Thank You", "Thank you for using our ATM. Goodbye!")
        self.show_menu()
     
     


    def exit(self):
        self.main_window.destroy()
        GUI.messagebox.showinfo("Thank You", "Thank you for using our ATM. Goodbye!")


account1=Account(215321701332,'Ahmed Abdelrazek Mohamed','1783',3500166)
account2=Account(203659302214,'Salma Mohamed Fouad','1390',520001)
account3=Account(126355700193,'Adel Khaled Abdelrahman','1214',111000)
account4=Account(201455998011,'Saeed Amin Elsawy','2001',1200)
account5=Account(201122369851,'Amir Salama Elgendy','8935',178933)
account6=Account(201356788002,'Wael Mohamed Khairy','3420',55000)
account7=Account(203366789564,'Mina Sameh Bishoy','1179',18000)
account8=Account(201236787812,'Omnia Ahmed Awad','1430',180350)

atm=ATM()
atm.add_account(account1)
atm.add_account(account2)
atm.add_account(account3)
atm.add_account(account4)
atm.add_account(account5)
atm.add_account(account6)
atm.add_account(account7)
atm.add_account(account8)

interface=ATMInterface(atm)
interface.main_window.mainloop()
