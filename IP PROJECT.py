import pandas as pd
import numpy as np
from datetime import datetime
import random
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.colheader_justify", "center")

def home_page():
   
    while True:
        print("""

                    __        __   _                            _           ____  _      _   _  ____  ____  _    _  ____     _
                    \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___    | __ )| |    | | | || ___|| __ )| |  | |/ ___|   | |   
                     \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \   |  _ \| |    | | | || __| |  _ \| |  | |\___ \   | |
                      \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |  | |_) | |___ | |_| || |__ | |_) | |__| | ___) |  |_|
                       \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   |____/|_____| \___/ |____||____/ \____/ |____/   (_)
                     

 
""")
        print("Where do you want to explore today ? ")

        print("""
        1)Book a ticket
        2)My booking
        3)Cancellation
        4)About us
        5)Reviews
        6)Help
        7)Exit
        """)
        print("______________________________________________________________________________________________________________________________________________________")
        choice=int(input("Enter your choice : "))
        if choice==1:
            print(r"""
                                                  ____              _              _____ _      _        _   
                                                 | __ )  ___   ___ | | __   __ _  |_   _(_) ___| | _____| |_ 
                                                 |  _ \ / _ \ / _ \| |/ /  / _` |   | | | |/ __| |/ / _ \ __|
                                                 | |_) | (_) | (_) |   <  | (_| |   | | | | (__|   <  __/ |_ 
                                                 |____/ \___/ \___/|_|\_\  \__,_|   |_| |_|\___|_|\_\___|\__|""")
                                                                 

            page_book()
        elif choice==2:
            print(r"""  
                                                   __  __         ____              _    _             
                                                  |  \/  |_   _  | __ )  ___   ___ | | _(_)_ __   __ _ 
                                                  | |\/| | | | | |  _ \ / _ \ / _ \| |/ / | '_ \ / _` |
                                                  | |  | | |_| | | |_) | (_) | (_) |   <| | | | | (_| |
                                                  |_|  |_|\__, | |____/ \___/ \___/|_|\_\_|_| |_|\__, |
                                                           |___/                                  |___/ """)
            page_booked()
        elif choice==3:
            print(r"""                            ____                      _  _____ _      _        _   
                                                 / ___|__ _ _ __   ___ ___ | ||_   _(_) ___| | _____| |_ 
                                                | |   / _` | '_ \ / __/ _ \  |  | | | |/ __| |/ / _ \ __|
                                                | |__| (_| | | | | (_|  __/  |  | | | | (__|   <  __/ |_ 
                                                 \____\__,_|_| |_|\___\___ |_|  |_| |_|\___|_|\_\___|\__|""")
            page_cancel()
        elif choice==4:
            print(r"""
                                                             _    _                 _     _   _     
                                                            / \  | |__   ___  _   _| |_  | | | |___ 
                                                           / _ \ | '_ \ / _ \| | | | __| | | | / __|
                                                          / ___ \| |_) | (_) | |_| | |_  | |_| \__ \
                                                         /_/   \_\_.__/ \___/ \__,_|\__|  \___/|___/


""")
                                                               
        
            page_about()
        elif choice==5:
            print(r"""
                                                              ____            _                   
                                                             |  _ \ _____   _(_) _____      _____ 
                                                             | |_) / _ \ \ / / |/ _ \ \ /\ / / __|
                                                             |  _ <  __/\ V /| |  __/\ V  V /\__ \
                                                             |_| \_\___| \_/ |_|\___| \_/\_/ |___/""")

            reviews()
        elif choice==6:
             print(r"""
                                                                      _   _      _       
                                                                     | | | | ___| |_ __  
                                                                     | |_| |/ _ \ | '_ \ 
                                                                     |  _  |  __/ | |_) |
                                                                     |_| |_|\___|_| .__/ 
                                                                                  |_|    """)
             page_help()
        elif choice==7:
            print(r"""
                                                                      _____      _ _   
                                                                     | ____|_  _(_) |_ 
                                                                     |  _| \ \/ / | __|
                                                                     | |___ >  <| | |_ 
                                                                     |_____/_/\_\_|\__|""")
            page_exit()
            break
    
        else:
            print("Invalid choice")
                   


#BOOKING

def page_book():
    current_datetime = datetime.now().date()
    print("Today's date is",current_datetime.strftime("%d-%m-%Y"))
    while True:
        date_str = input("Please enter the date on which you would like to book your ticket (dd-mm-yyyy): ")
        try:
            booking_date = datetime.strptime(date_str, "%d-%m-%Y").date()
        except ValueError:
            print("⚠️ Invalid format! Please use dd-mm-yyyy.")
            continue
        if booking_date>current_datetime:
            break
        else:
            print("Invalid date")
    
    print("You have chosen:", booking_date.strftime("%A, %d %B %Y"))


    #destination
    start_list=["1.Chennai","2.Bangalore","3.Mysore","4.Rameshwaram","5.Kanyakumari"]
    end_list=["1.Chennai","2.Bangalore","3.Mysore","4.Rameshwaram","5.Kanyakumari"]
    print()
    start=int(input("""
1-Chennai
2-Banglore
3-Mysore
4-Rameshwaram
5-Kanyakumari
Enter your start location option : """))
    while start<0 or start>5:
        print("Invalid input! Try again")
        start=int(input("Enter your start location option : "))
            
    print()
    drop=int(input("""
1-Chennai
2-Banglore
3-Mysore
4-Rameshwaram
5-Kanyakumari
Enter your drop location option : """))
    while drop<0 or drop>5:
        print("Invalid input!,Try again")
        drop=int(input("Enter your drop location option : "))
    df=pd.read_csv(r"C:\Users\Personal\gungun\IP-Project-\busdetail.txt",index_col="Bus_no")
    while True:
        new_df=df[(df["Start"] == start_list[start-1][2:]) & (df["End"] == end_list[drop-1][2:])]
        print()
        print("Start location:",start_list[start-1][2:])
        print("Drop location:",end_list[drop-1][2:])
        print()
        if new_df.empty:
            print("⚠️ No buses available for this route. Please try a different start and drop location.")
            start = int(input("""
1-Chennai
2-Banglore
3-Mysore
4-Rameshwaram
5-Kanyakumari
Enter your start location option : """))
            while start < 1 or start > 5:
                print("Invalid input! Try again.")
                start = int(input("Enter your start location option : "))
            drop = int(input("""
1-Chennai
2-Banglore
3-Mysore
4-Rameshwaram
5-Kanyakumari
Enter your drop location option : """))
            while drop < 1 or drop > 5:
                print("Invalid input! Try again.")
                drop = int(input("Enter your drop location option : "))
        else:
            print(new_df)
            print()
            break
        
    a=input("Enter the bus_no you want to choose : ").upper()
    while a not in new_df.index:
        print("Invalid bus option")
        a=int(input("Enter the bus option you want to choose : "))
    print(new_df.loc[a])
    print()

    
    #Passanger Details
    tickets=int(input("Enter the no. of tickets you want to book : "))
    NAMES=[]
    AGE=[]
    SEX=[]
    PHONE=[]
    CODE=[]
    while tickets>df.loc[a,"Tickets"]:
        print("The requested number of tickets exceeds availability. Kindly choose fewer tickets.")
        tickets=int(input("Enter the no. of tickets you want to book : "))
        print()
    for i in range(1,tickets+1):
        print("Enter passenger",i," Name : ")
        name=input()
        print("Enter passenger",i," Age : ")
        age=int(input())
        print("Enter passenger",i," Sex(M/F): ")
        sex=input().upper()
        while sex!="M" and sex!="F" :
            
            print("Invalid input pls try again!")
            sex=input(f"Enter passenger {i} Sex(M/F):")
            
        print("Enter passanger",i,"Phone no. : ")
        ph=input()
        while len(ph)>10 or len(ph)<10:
            print("Invalid input pls try booking again!")
            print("Enter passanger",i,"Phone no.:")
            ph=input()
            print()
        NAMES.append(name)
        AGE.append(age)
        SEX.append(sex)
        PHONE.append(ph)
    det1=pd.DataFrame({"Name":NAMES,"Age":AGE,"Sex":SEX,"Phone.no":PHONE})
    print(det1)
    print()
    confirm=input("To go ahead with the payment type Y : ")
    if confirm=="Y" or confirm=="y":
        print()
        pass
    else:
        home_page()


    #payment
    total_am=df.loc[a,"Cost"]*tickets
    print("Total amount to be paid:",total_am) 
    print()
    pay=int(input("""
1.UPI
2.Card
Enter which payment method you want to use :  """))
    if pay==1:
        payment_method="upi"
        print("Payment succesful")
        code = random.randint(1000, 9999)
        CODE=[code]*tickets
        print()
        print("Please keep this code safe to check additional information")
        print(code)
        input()
    elif pay==2:
        payment_method="card"
        print("Payment successful")
        code =random.randint(1000, 9999)
        CODE=[code]*tickets
        print()
        print("Please keep this code safe to check additional information.")
        print(code)
        print()
        input()
    else:
        print("Invalid option, payment failed, try booking again")
        return
    
    det=pd.DataFrame({"Name":NAMES,"Age":AGE,"Sex":SEX,"Phone.no":PHONE,"Code":CODE})
    det["From"]=start_list[start-1][2:]
    det["To"]=end_list[drop-1][2:]
    det["Bus_No."]=a
    det["Payment_Method"]="UPI" if pay==1 else "Card"
    det=det.set_index("Code")
    det.to_csv(r"C:\Users\Personal\gungun\IP-Project-\booking.txt",mode="a",header=False)
    print("Ticket details are as follows:")
    print()
    print(det.to_string())
    input()
    print("total amount payed is",total_am)
    print("Thank you! We wish you a comfortable and happy journey.")
    input()
    





#MYBOOKING/HISTORY
def page_booked():
    num=int(input("Enter code : "))
    print()
    details=pd.read_csv(r"C:\Users\stell\OneDrive\Desktop\IP\booking.txt",index_col="code")           
    if num not in details.index:
        print("⚠️ No booking found with this code.")
        input()
        return
    booking=details.loc[[num]]
    print("Booking details")
    print()  
    for _, row in booking.iterrows():
        print("\n/==================== BUS TICKET ====================\\")
        print(f"| Booking Code : {num:<35} |")
        print(f"| Passenger    : {row['name']:<35} |")
        print(f"| Age / Sex    : {row['age']} / {row['sex']:<30} |")
        print(f"| Phone No.    : {row['phone.no']:<35} |")
        print(f"| From → To    : {row['from']} → {row['to']:<27} |")
        print(f"| Bus No.      : {row['bus_no']:<35} |")
        print(f"| Payment      : {row['payment_method']:<35} |")
        print("\\====================================================/\n")
        print()
    print("Press enter to return to homepage")
    input()
    
    





#CANCEL
def page_cancel():
    num=int(input("Enter code : "))
    print()
    details=pd.read_csv(r"C:\Users\stell\OneDrive\Desktop\IP\booking.txt",index_col="code")           
    if num not in details.index:
        print("⚠️ No booking found with this code.")
        return
    booking=details.loc[[num]]
    no_of_tickets=int(input("Enter how many tickets you would like to cancel : "))
    while no_of_tickets>booking.shape[0]:
        print("⚠️ Only", booking.shape[0] ,"ticket(s) exist for this booking. Please try again.")
        no_of_tickets=int(input("Enter how many tickets you would like to cancel : "))
    if no_of_tickets==booking.shape[0]:
        print("Tickets")
        print()  
        for _, row in booking.iterrows():
            print("\n/==================== BUS TICKET ====================\\")
            print(f"| Booking Code : {num:<35} |")
            print(f"| Passenger    : {row['name']:<35} |")
            print(f"| Age / Sex    : {row['age']} / {row['sex']:<30} |")
            print(f"| Phone No.    : {row['phone.no']:<35} |")
            print(f"| From → To    : {row['from']} → {row['to']:<27} |")
            print(f"| Bus No.      : {row['bus_no']:<35} |")
            print(f"| Payment      : {row['payment_method']:<35} |")
            print("\\====================================================/\n")
            print()
        confirm=input("Press Y to confirm cancellation or press any key to abort : ")
        if confirm=="Y" or confirm=="y":
            details=details.drop(num)
            details.to_csv(r"C:\Users\stell\OneDrive\Desktop\IP\booking.txt")
            print()
            print("✅ Your ticket(s) have been successfully cancelled. Thank you for using BlueBus! Refund will be processed shortly.")
            input("Press enter to return to homepage")
        else:
            return
    else:
        print("Tickets")
        print()  
        for _, row in booking.iterrows():
            print("\n/==================== BUS TICKET ====================\\")
            print(f"| Booking Code : {num:<35} |")
            print(f"| Passenger    : {row['name']:<35} |")
            print(f"| Age / Sex    : {row['age']} / {row['sex']:<30} |")
            print(f"| Phone No.    : {row['phone.no']:<35} |")
            print(f"| From → To    : {row['from']} → {row['to']:<27} |")
            print(f"| Bus No.      : {row['bus_no']:<35} |")
            print(f"| Payment      : {row['payment_method']:<35} |")
            print("\\====================================================/\n")
            print()
        for i in range(no_of_tickets):
            while True:
                name=input(f"Enter name of passenger #{i+1} to cancel : ")
                if name not in booking['name'].values:
                    print("⚠️ Name not found in this booking. Try again.")
                else:
                    details = details.drop(details[details['name'] == name].index)
                    break
        details.to_csv(r"C:\Users\stell\OneDrive\Desktop\IP\booking.txt")
        print()
        print("✅ Your ticket(s) have been successfully cancelled. Thank you for using BlueBus! Refund will be processed shortly.")
        input("Press enter to return to homepage")

        
        
        
    
    





# ABOUT US
def page_about():
    print("""Welcome to BlueBus, your trusted companion for seamless and affordable bus travel.

We’re a student-led initiative created with a passion for technology and a commitment to solving real-world problems. Inspired by platforms like RedBus, BlueBus aims to simplify the bus ticket booking experience — making it faster, cleaner, and smarter.

Whether you're commuting between cities, planning a trip, or just heading home, BlueBus helps you:

📅 Book tickets in seconds

📂 Access your bookings and travel history

❌ Cancel with zero stress

🧾 Get clean, clutter-free receipts

🙋 Reach support anytime

This project is a part of our learning journey in software development — combining Python, MySQL, and a love for solving practical problems.

We believe smart travel should be for everyone — and BlueBus is our step in that direction.""")
    print()
    input("Press enter to return to homepage")






#REVIEWS
def reviews():
    while True:
        print("""
    1)Give a review
    2)Read reviews
    3)Return to homepage
    """)
        print("______________________________________________________________________________________________________________________________________________________")
        choice2=int(input("Enter your choice : "))
        if choice2==1:
            give_review()
            break
        elif choice2==2:
            read_reviews()
            break
        elif choice2==3:
            break
        else:
            print("Invalid choice")
            reviews()
#Give reviews
def give_review():
    while True:
        num=int(input("Enter code : "))
        details=pd.read_csv(r"C:\Users\stell\OneDrive\Desktop\IP\booking.txt",index_col="code") 
        if num not in details.index:
            print("⚠️ You cannot give a review because no booking was found with this code.")
            choice= int(input("Enter 1 to try again else enter any other number : "))
            if choice!=1:
                return
            else:
                continue
        else:
            break
    name=input("Enter your name : ")
    while True:
        rate=int(input("Rate your experience (1-5): "))
        if 1<=rate<=5:
            rate="⭐"*rate
            break
        else:
            print("Please enter a rating between 1 and 5.")
    description=input("Enter your review :")
    print()
    print("Rating : ",rate)
    print("Name : ",name)
    print("Review : ",description)
    print()
    confirm(rate,name,description)
def confirm(rate,name,description):
        choice3=input("Confirm details ? Y/N : ")
        if choice3=="Y" or choice3=="y":
            d={"Rating":[rate],"Name":[name],"Review":[description]}
            df=pd.DataFrame(d)
            df.to_csv(r"C:\Users\stell\OneDrive\Desktop\IP\review.csv",header=False,mode="a",index=False)
            print()
            print("Thanks for sharing your thoughts with BlueBus! Safe travels!")
            print()
            input("Press enter to return to homepage")
            print()
        elif choice3=="N" or choice3=="n":
            print("Press enter to return to homepage")
            input()
            return 
        else:
            print("Invalid choice")
            print()
            return confirm(rate,name,description)

#Read reviews
def read_reviews():
    df1=pd.read_csv(r"C:\Users\stell\OneDrive\Desktop\IP\review.csv",header=None,names=["Rating","Name","Review"])
    for index,row in df1.iterrows():
        print("REVIEW",index+1)
        print("──────────────")
        print("Rating :", row['Rating'])
        print("Name   :", row['Name'])
        print("Review :", row['Review'])
        print("\n" + "-"*60 + "\n")
    print()
    input("Press enter to return to homepage")






#HELP
def page_help():
    print()
    print("""
Need assistance?

📞 Customer Care: +91-987654
🕒 Available: 8:00 AM – 10:00 PM, All Days

For any queries related to booking, cancellation, or payments, feel free to call us!

Press enter to return to the homepage.
""")
    input()





#Exit    
def page_exit():
    print("""
             __   __                _                                          _      _                    __                           _  
             \ \ / /__ _  _ _ _    (_)___ _  _ _ _ _ _  ___ _  _   ___ _ _  __| |___ | |_  ___ _ _ ___    / _|___ _ _   _ _  _____ __ _| | 
              \ V / _ \ || | '_|   | / _ \ || | '_| ' \/ -_) || | / -_) ' \/ _` (_-< | ' \/ -_) '_/ -_)  |  _/ _ \ '_| | ' \/ _ \ V  V /_| 
               |_|\___/\_,_|_|    _/ \___/\_,_|_| |_||_\___|\_, | \___|_||_\__,_/__/ |_||_\___|_| \___|  |_| \___/_|   |_||_\___/\_/\_/(_)
                                 |__/                       |__/                                 """)
def admin():
    adm_phone=9535044904
    adm_password="bluebuzz08"
    mob=int(input("enter your mobile number: "))
    password=input("enter your admin login password: ")
    if mob!=adm_phone or password!=adm_password:
         print("""invalid input
         please verify your data again""")
         start()
    else:
        e=pd.read_csv(r"C:\Users\Personal\gungun\IP-Project-\busdetail.txt",index_col="Bus_no")
        start_list=["chennai","bangalore","mysore","rameshwaram","kanyakumari"]
        end_list=["chennai","bangalore","mysore","rameshwaram","kanyakumari"]
        while True:
            print("""options:
            1.adding buses
            2.deleting buses
            3.modifying the number of tickets 
            4.view
            5.exit""")
            op=int(input("enter your option:"))
            if op==4:
                print(e)
            elif op==1:
                z=input("enter the bus_no: ")
                z=z.upper()
                while z in e.index:
                    print("invalid input")
                    z=input("enter the bus_no: ")
                    z=z.upper()
                l=[]
                
                f=input("enter start location: ").lower()
                while f not in start_list:
                    print("start location does not belong in original data set")
                    f=input("enter start location: ")
                l.append(f)
                
                d=input("enter drop location: ").lower()
                while d not in end_list:
                    print("drop location does not belong in original data set")
                    d=input("enter drop location: ")
                l.append(d)
                 
                n=input("enter agency name: ")
                l.append(n)
                
                t=input("enter time(hh:mm(am/pm)): ")
                l.append(t)
                
                c=int(input("enter cost of one ticket: "))
                l.append(c)
                
                day=input("enter the day of boarding: ")
                l.append(day)
                
                tick=int(input("enter the total no. of tickets available in the bus: "))
                l.append(tick)
               
                
                e.loc[z,:]=l
                print()
                print(e)
                
            elif op==2:
                d=input("enter the bus_no you want to delete:")
                d=d.upper()
                while d not in e.index:
                    print("invalid input")
                    d=input("enter the bus_no you want to delete:")
                    d=d.upper()
                e.drop([d],inplace=True)
                print()
                print(e)
                
                
            elif op==3:
                z=input("enter the bus_no: ")
                z=z.upper()
                n=int(input("enter what you want to change the no of tickects to: "))
                while z not in e.index:
                    print("invalid input")
                    z=input("enter the bus_no: ")
                    z=z.upper()
                e.loc[z,"Tickets"]=n
                print()
                print(e)

                
            elif op==5:
                
                choice=input("do you want to save the changes?(y/n)").lower()
                if choice == "y":
                    e.to_csv(r"C:\Users\Personal\gungun\IP-Project-\busdetail.txt")
                break
            else:
                print("invalid input")
                print("""options:
                1.adding buses
                2.deleting buses
                3.modifying the number of tickets 
                4.view""")
                op=int(input("enter your option: "))
                
                
            
            
            
     
 
 
 
 
 
 
 
 
 
 
 
def start():
    print("""how would you like to explore today:
        1.admin
        2.user""")
    print()
    ch=int(input("enter your choice: "))
    if ch==1:
        admin()
            
    elif ch==2:
        home_page()
    else:
        print("invalid input")
        start()
start()

