import pandas as pd
import numpy as np
from datetime import datetime
from tabulate import tabulate
import matplotlib.pyplot as plt
import random
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.colheader_justify", "center")

def home_page():
    #HOME PUT NICELY 
    print(r"""
                                                                 _   _  ___  __  __ _____  
                                                                | | | |/ _ \|  \/  | ____| 
                                                                | |_| | | | | |\/| |  _|   
                                                                |  _  | |_| | |  | | |___  
                                                                |_| |_|\___/|_|  |_|_____| 

                            """)
    while True:
        print()
        print()
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
        choice=input("Enter your choice : ")
          
        if choice=="1":
            print(r"""
                                                  ____              _              _____ _      _        _   
                                                 | __ )  ___   ___ | | __   __ _  |_   _(_) ___| | _____| |_ 
                                                 |  _ \ / _ \ / _ \| |/ /  / _` |   | | | |/ __| |/ / _ \ __|
                                                 | |_) | (_) | (_) |   <  | (_| |   | | | | (__|   <  __/ |_ 
                                                 |____/ \___/ \___/|_|\_\  \__,_|   |_| |_|\___|_|\_\___|\__|""")
                                                                 

            page_book()
        elif choice=="2":
            print(r"""  
                                                   __  __         ____              _    _             
                                                  |  \/  |_   _  | __ )  ___   ___ | | _(_)_ __   __ _ 
                                                  | |\/| | | | | |  _ \ / _ \ / _ \| |/ / | '_ \ / _` |
                                                  | |  | | |_| | | |_) | (_) | (_) |   <| | | | | (_| |
                                                  |_|  |_|\__, | |____/ \___/ \___/|_|\_\_|_| |_|\__, |
                                                           |___/                                  |___/ """)
            page_booked()
        elif choice=="3":
            print(r"""
                                                  ____                      _  _____ _      _        _   
                                                 / ___|__ _ _ __   ___ ___ | ||_   _(_) ___| | _____| |_ 
                                                | |   / _` | '_ \ / __/ _ \  |  | | | |/ __| |/ / _ \ __|
                                                | |__| (_| | | | | (_|  __/  |  | | | | (__|   <  __/ |_ 
                                                 \____\__,_|_| |_|\___\___ |_|  |_| |_|\___|_|\_\___|\__|""")
            page_cancel()
        elif choice=="4":
            print(r"""
                                                             _    _                 _     _   _     
                                                            / \  | |__   ___  _   _| |_  | | | |___ 
                                                           / _ \ | '_ \ / _ \| | | | __| | | | / __|
                                                          / ___ \| |_) | (_) | |_| | |_  | |_| \__ \
                                                         /_/   \_\_.__/ \___/ \__,_|\__|  \___/|___/


""")
                                                               
        
            page_about()
        elif choice=="5":
            print(r"""
                                                              ____            _                   
                                                             |  _ \ _____   _(_) _____      _____ 
                                                             | |_) / _ \ \ / / |/ _ \ \ /\ / / __|
                                                             |  _ <  __/\ V /| |  __/\ V  V /\__ \
                                                             |_| \_\___| \_/ |_|\___| \_/\_/ |___/""")

            reviews()
        elif choice=="6":
             print(r"""
                                                                      _   _      _       
                                                                     | | | | ___| |_ __  
                                                                     | |_| |/ _ \ | '_ \ 
                                                                     |  _  |  __/ | |_) |
                                                                     |_| |_|\___|_| .__/ 
                                                                                  |_|    """)
             page_help()
        elif choice=="7":
            start()
            
    
        else:
            print("Invalid choice")
            choice=input("Enter your choice : ")


#BOOKING

def page_book():
    current_datetime = datetime.now().date()
    print("Today's date is",current_datetime.strftime("%d-%m-%Y"))
    while True:
        date_str = input("Please enter the date on which you would like to book your ticket (dd-mm-yyyy): ")
        try:
            booking_date = datetime.strptime(date_str, "%d-%m-%Y").date()
            #cur_month=int(current_datetime.strftime("%m"))
            #m=cur_month+3
            #book_month=int(datetime.strptime(date_str,"%m"))
            
            
            
        except ValueError:
            print(" Invalid format! Please use dd-mm-yyyy.")
            continue
        if booking_date>current_datetime:
            break
       
        #if book_month>m:
            #print("invalid booking,booking possible")
        
            
            
                
        
    
    print("You have chosen:", booking_date.strftime("%A, %d %B %Y"))


    #destination
    start_list=["CHENNAI","BANGALORE","MYSORE","RAMESHWARAM","KANYAKUMARI"]
    end_list=["CHENNAI","BANGALORE","MYSORE","RAMESHWARAM","KANYAKUMARI"]
    print()
    for i in range(len(start_list)):
        print(i+1, start_list[i])
    start=int(input("""Enter your start location option(number) : """))
    while start<1 or start>5:
        print("Invalid input! Try again")
        start=int(input("Enter your start location option(number) : "))
            
    print()
    
    for i in range(len(start_list)):
        print(i+1, start_list[i])
    drop=int(input("""Enter your drop location option(number) : """))
    while drop<1 or drop>5:
        print("Invalid input!,Try again")
        drop=int(input("Enter your drop location option(number) : "))
    df=pd.read_csv(r"E:\AnushkaProjecy\IP-Project-\busdetail.txt",index_col="BUS_NO")
    while True:
        new_df=df[(df["START"] == start_list[start-1]) & (df["END"] == end_list[drop-1])]
        print()
        print("Start location:",start_list[start-1])
        print("Drop location:",end_list[drop-1])
        print()
        if new_df.empty:
            print(" No buses available for this route. Please try a different start and drop location.")
            for i in range(len(start_list)):
                print(i+1, start_list[i])
            start=int(input("""Enter your start location option(number) : """))
            while start < 1 or start > 5:
                print("Invalid input! Try again.")
                start = int(input("Enter your start location option : "))
            for i in range(len(start_list)):
                print(i+1, start_list[i])
            drop=int(input("""Enter your start location option(number) : """))
            while drop < 1 or drop > 5:
                print("Invalid input! Try again.")
                drop = int(input("Enter your drop location option : "))
        else:
            #print(new_df)
            print(tabulate(new_df, headers='keys', tablefmt='psql'))

            print()
            break
        
    a=input("Enter the bus_no you want to choose : ").upper()
    while a not in new_df.index:
        print("Invalid bus option")
        a=input("Enter the bus option you want to choose : ").upper()
    #print(new_df.loc[a])
    print(tabulate(new_df.loc[[a]], headers='keys', tablefmt='psql'))
    print()

    
    #Passanger Details
    #if errror occurs it shud give message and not stop the code for everything 
    tickets=int(input("Enter the no. of tickets you want to book : "))
    NAMES=[]
    AGE=[]
    SEX=[]
    PHONE=[]
    CODE=[]
    while tickets>df.loc[a,"TICKETS"]:
        print("The requested number of tickets exceeds availability. Kindly choose fewer tickets.")
        tickets=int(input("Enter the no. of tickets you want to book : "))
        print()
    for i in range(1,tickets+1):
        print("Enter passenger",i," Name : ")
        name=input()
        while len(name)==0:
            print("Enter valid name ")
            name=input()
        print("Enter passenger",i," Age : ")
        age = input("Enter age: ")
        while not age.isdigit() or len(age)==0:
            print("Enter valid age")
            age = input("Enter age: ")

        age = int(age)
        print("Enter passenger",i," Sex(M/F): ")
        sex=input().upper()
        while sex!="M" and sex!="F" :
            
            print("Invalid input pls try again!")
            sex=input(f"Enter passenger {i} Sex(M/F):")
            
        print("Enter passanger",i,"Phone no. : ")
        ph=input()
        while not ph.isdigit():
            print("please enter a valid 10 digit number...")
            ph=input()
            print()
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
    #print(det1)
    print(tabulate(det1, headers='keys', tablefmt='psql'))
    print()
    confirm=input("To go ahead with the payment type Y : ")
    if confirm=="Y" or confirm=="y":
        print()
        pass
    else:
        #PAYEMENTPEDNDING
        home_page()


    #payment
    total_am=df.loc[a,"COST"]*tickets
    print("Total amount to be paid:",total_am) 
    print()
    pay=input("""
1.UPI
2.Card
Enter which payment method you want to use :  """)
    if pay=='1':
        payment_method="upi"
        print("Payment succesful")
        code = random.randint(1000, 9999)
        CODE=[code]*tickets
        print()
        print("Please keep this code safe to check additional information")
        print(code)
        input()
    elif pay=='2':
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
    pay=int(pay)
    df.loc[a, "TICKETS"] = df.loc[a, "TICKETS"] - tickets
    df.to_csv(r"E:\AnushkaProjecy\IP-Project-\busdetail.txt")
    det=pd.DataFrame({"Name":NAMES,"Age":AGE,"Sex":SEX,"Phone.no":PHONE,"Code":CODE})
    det["From"]=start_list[start-1]
    det["To"]=end_list[drop-1]
    det["Bus_No."]=a
    det["Payment_Method"]="UPI" if pay==1 else "Card"
    det=det.set_index("Code")
    det.to_csv(r"E:\AnushkaProjecy\IP-Project-\booking.txt",mode="a",header=False)
    print("Ticket details are as follows:")
    print()
    #print(det.to_string())
    print(tabulate(det,headers='rows', tablefmt='psql'))
    input()
    print("Total amount payed is",total_am)
    print("Thank you! We wish you a comfortable and happy journey.")
    input()
    





#MYBOOKING/HISTORY
def page_booked():
    num=int(input("Enter code : "))
    print()
    details=pd.read_csv(r"E:\AnushkaProjecy\IP-Project-\booking.txt",index_col="code")           
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
    details=pd.read_csv(r"E:\AnushkaProjecy\IP-Project-\booking.txt",index_col="code")           
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
            details.to_csv(r"E:\AnushkaProjecy\IP-Project-\booking.txt")
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
                    matching_rows = booking[booking['name'] == name]
                    if matching_rows.empty:
                        print("⚠️ No exact match found in full data (code + name).")
                    else:
                       details_reset = details.reset_index()
                       # 2. Drop only the row that matches code + name
                       details_reset = details_reset[~((details_reset["code"] == num) & (details_reset["name"] == name))]
                       # 3. Set 'code' back as the index
                       details = details_reset.set_index("code")
                    break
        details.to_csv(r"E:\AnushkaProjecy\IP-Project-\booking.txt")
        print()
        print("✅ Your ticket(s) have been successfully cancelled. Thank you for using BlueBus! Refund will be processed shortly.")
        input("Press enter to return to homepage")
    df=pd.read_csv(r"E:\AnushkaProjecy\IP-Project-\busdetail.txt",index_col="BUS_NO")
    bus_no = booking.iloc[0]["bus_no"]
    df.loc[bus_no, "TICKETS"] = df.loc[bus_no, "TICKETS"] + no_of_tickets
    df.to_csv(r"E:\AnushkaProjecy\IP-Project-\busdetail.txt")

        
        
        
    
    





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
        details=pd.read_csv(r"E:\AnushkaProjecy\IP-Project-\booking.txt",index_col="code")
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
    print(r"""
             __   __                _                                          _      _                    __                           _  
             \ \ / /__ _  _ _ _    (_)___ _  _ _ _ _ _  ___ _  _   ___ _ _  __| |___ | |_  ___ _ _ ___    / _|___ _ _   _ _  _____ __ _| | 
              \ V / _ \ || | '_|   | / _ \ || | '_| ' \/ -_) || | / -_) ' \/ _` (_-< | ' \/ -_) '_/ -_)  |  _/ _ \ '_| | ' \/ _ \ V  V /_| 
               |_|\___/\_,_|_|    _/ \___/\_,_|_| |_||_\___|\_, | \___|_||_\__,_/__/ |_||_\___|_| \___|  |_| \___/_|   |_||_\___/\_/\_/(_)
                                 |__/                       |__/                                 """)
    exit(0)
def admin():
    
    adm_phone="9535044904"
    adm_password="BLUEBUZZ08"
    mob=input("Enter your mobile number: ")
    while not mob.isdigit() or len(mob)!=10:
        print("Please enter a valid 10-digit mobile number.\n")
        mob=input("Enter your mobile number: ")

    password=input("Enter your admin login password: ")
    if mob!=adm_phone or password!=adm_password:
        print("\nWrong password or mobile number.")
        print("Please enter your details again.\n")
        admin()
    else:
        
        print()
        e=pd.read_csv(r"E:\AnushkaProjecy\IP-Project-\busdetail.txt",index_col="BUS_NO")
        start_list=["CHENNAI","BANGALORE","MYSORE","RAMESHWARAM","KANYAKUMARI"]
        end_list=["CHENNAI","BANGALORE","MYSORE","RAMESHWARAM","KANYAKUMARI"]
        agency_list=['GREENLINE', 'KSRTC', 'SRS_TRAVELS', 'SKYLINE', 'ROYAL_TRAVELS', 'ORANGE_TOURS', 'JETLINE', 'MODERN_BUS', 'NATIONAL_TRAVELS', 'REDBUS', 'INTERCITY']
        
        while True:
            print(r"""
                                                                     _    ____  __  __ ___ _   _ 
                                                                    / \  |  _ \|  \/  |_ _| \ | |
                                                                   / _ \ | | | | |\/| || ||  \| |
                                                                  / ___ \| |_| | |  | || || |\  |
                                                                 /_/   \_\____/|_|  |_|___|_| \_|
                                                                 """)
            print("\nOptions:")
            print("1. Add Bus")
            print("2. Delete Bus")
            print("3. Modify Number of Tickets")
            print("4. View Buses")
            print("5. Ticket Statistics")
            print("6. Exit")

            op=input("Enter your option: ")
            if op=='4':
                print()
                print(r"""
                                                                 __     _____ _______        __
                                                                 \ \   / /_ _| ____\ \      / /
                                                                  \ \ / / | ||  _|  \ \ /\ / / 
                                                                   \ V /  | || |___  \ V  V /  
                                                                    \_/  |___|_____|  \_/\_/   
                               """)
                print("\nSTART LOCATION FILTER:")
                for i in range(len(start_list)):
                    print(i+1, start_list[i])

                x = input("\n(Comma Separated Numbers or press Enter for ALL) ")
                if x.strip() == "":
                    x = e["START"]
                else:
                    x = x.split(",")
                    s_values = []
                    for v in x:
                        if v.isdigit() and 1 <= int(v) <= len(start_list):
                            s_values.append(start_list[int(v)-1])
                    x = s_values
                    if x == []:
                        x = e["START"]

                if type(x) is list:
                    d = e[e["START"].isin(x)]
                else:
                    d = e[e.loc[:,"START"]==x]

                print("\nEND CITY FILTER:")
                for i in range(len(end_list)):
                    print(i+1, end_list[i])

                y = input("\n(Comma Separated Numbers or press Enter for ALL) ")
                if y.strip() == "":
                    y = d["END"]
                else:
                    y = y.split(",")
                    e_values = []
                    for v in y:
                        if v.isdigit() and 1 <= int(v) <= len(end_list):
                            e_values.append(end_list[int(v)-1])
                    y = e_values
                    if y == []:
                        y = d["END"]

                if type(y) is list:
                    b = d[d.loc[:,"END"].isin(y)]
                else:
                    b = d[d.loc[:,"END"]==y]

                print("\nTRAVEL AGENCY FILTER:")
                for i in range(len(agency_list)):
                    print(i+1, agency_list[i])

                t = input("\n(Comma Separated Numbers or press Enter for ALL) ")
                if t.strip() == "":
                    t = b["NAME"]
                else:
                    t = t.split(",")
                    a_values = []
                    for v in t:
                        if v.isdigit() and 1 <= int(v) <= len(agency_list):
                            a_values.append(agency_list[int(v)-1])
                    t = a_values
                    if t == []:
                        t = b["NAME"]

                if type(t) is list:
                    c = b[b.loc[:,"NAME"].isin(t)]
                else:
                    c = b[b.loc[:,"NAME"]==t]

                z = input("\nDAY FILTER\n (FULL DAY NAME or press Enter for ALL) ").upper()
                if z.strip() == "":
                    z = c["DAY"]
                    r = c
                else:
                    r = c[c.loc[:,"DAY"]==z]

                print("\nBus List:\n")
                print(tabulate(r, headers='keys', tablefmt='psql'))
                input("\nPress Enter to continue...")

            elif op=='1':
                print()
                print(r"""
                                                             _    ____  ____    ____  _   _ ____  _____ ____  
                                                            / \  |  _ \|  _ \  | __ )| | | / ___|| ____/ ___| 
                                                           / _ \ | | | | | | | |  _ \| | | \___ \|  _| \___ \ 
                                                          / ___ \| |_| | |_| | | |_) | |_| |___) | |___ ___) |
                                                         /_/   \_\____/|____/  |____/ \___/|____/|_____|____/
                                                         """)
                z = input("\nEnter Bus Number: ").upper()
                while z in e.index:
                    print("\nBus already exists. Enter a different bus number.")
                    z = input("Enter Bus Number: ").upper()
                l = []

                # Start Location Selection
                for i in range(len(start_list)):
                    print(i+1, start_list[i])
                s = input("\nChoose Start Location (Enter number): ")
                while not s.isdigit() or int(s) < 1 or int(s) > len(start_list):
                    print("Invalid selection. Enter a valid number.")
                    s = input("Choose Start Location (Enter number): ")
                l.append(start_list[int(s)-1])

                # End Location Selection
                for i in range(len(end_list)):
                    print(i+1, end_list[i])
                t = input("\nChoose Drop Location (Enter number): ")
                while not t.isdigit() or int(t) < 1 or int(t) > len(end_list) or t==s:
                    print("Invalid selection. Enter a valid number.")
                    t = input("Choose Drop Location (Enter number): ")
                l.append(end_list[int(t)-1])

                # Agency Selection
                for i in range(len(agency_list)):
                    print(i+1, agency_list[i])
                s = input("\nChoose Travel Agency (Enter number): ")
                while not s.isdigit() or int(s) < 1 or int(s) > len(agency_list):
                    print("Invalid selection. Enter a valid number.")
                    s = input("Choose Travel Agency (Enter number): ")
                l.append(agency_list[int(s)-1])

                t = input("\nEnter Time (hh:mm(am/pm)): ")
                while(len(t)<7):
                    print("Invalid selection. Enter a valid time.")
                    t=input("\nEnter Time (hh:mm(am/pm)): ")
                l.append(t)

                c = input("Enter Ticket Cost: ")
                while not c.isdigit():
                    print("Enter Valid Number")
                    c=input("Enter Ticket Cost: ")
                c=int(c)
                l.append(c)

                day = input("Enter Day of Boarding (Full Name): ").upper()
                l.append(day)

                tick = input("Enter Total Tickets Available: ")
                while not tick.isdigit():
                    print("Enter Valid Number")
                    tick = input("Enter Total Tickets Available: ")
                tick=int(tick)
                l.append(tick)

                e.loc[z, :] = l
                print("\nBus added successfully.\n")
                input("Press Enter to continue...")


            elif op=='2':
                print()
                print(r"""
                                              ____  _____ __  __  _____     _______   ____  _   _ ____  _____ ____  
                                             |  _ \| ____|  \/  |/ _ \ \   / / ____| | __ )| | | / ___|| ____/ ___| 
                                             | |_) |  _| | |\/| | | | \ \ / /|  _|   |  _ \| | | \___ \|  _| \___ \ 
                                             |  _ <| |___| |  | | |_| |\ V / | |___  | |_) | |_| |___) | |___ ___) |
                                             |_| \_\_____|_|  |_|\___/  \_/  |_____| |____/ \___/|____/|_____|____/
                                             """)
                d=input("\nEnter Bus Number to Remove: ").upper()
                while d not in e.index:
                    print("\nBus does not exist.")
                    d=input("Enter Bus Number to Remove: ").upper()

                e.drop([d],inplace=True)
                print("\nBus removed successfully.")
                input("Press Enter to continue...")

            elif op=='3':
                print()
                print(r"""
                                                              __  __  ___  ____ ___ _______   __
                                                             |  \/  |/ _ \|  _ \_ _|  ___\ \ / /
                                                             | |\/| | | | | | | | || |_   \ V / 
                                                             | |  | | |_| | |_| | ||  _|   | |  
                                                             |_|  |_|\___/|____/___|_|     |_|
                                                             """)
                z=input("\nEnter Bus Number: ").upper()
                while z not in e.index:
                    print("\nBus does not exist.")
                    z=input("Enter Bus Number: ").upper()

                n=input("Enter New Number of Tickets: ")
                while not n.isdigit():
                    print("Enter valid number")
                    n=input("Enter New Number of Tickets: ")
                n=int(n)
                e.loc[z,"TICKETS"]=n
                print("\nNumber of tickets updated successfully.")
                input("Press Enter to continue...")
            elif op=="5":
                while True:
                    
                        print()
                        print(r"""
                                                          ____ _____  _  _____ ___ ____ _____ ___ ____ ____  
                                                         / ___|_   _|/ \|_   _|_ _/ ___|_   _|_ _/ ___/ ___| 
                                                         \___ \ | | / _ \ | |  | |\___ \ | |  | | |   \___ \ 
                                                          ___) || |/ ___ \| |  | | ___) || |  | | |___ ___) |
                                                         |____/ |_/_/   \_\_| |___|____/ |_| |___\____|____/
                                                         """)
                                                         
                        print("""1) Tickets sold per destination
2) Remaining tickets per destination
3) Exit""")
                        c=input("Enter your option : ")
                        print()
                        if c=="2":
                            k=pd.read_csv(r"E:\AnushkaProjecy\IP-Project-\busdetail.txt")
                            ch=k[k["END"]=="CHENNAI"]
                            ba=k[k["END"]=="BANGALORE"]
                            ra=k[k["END"]=="RAMESHWARAM"]
                            my=k[k["END"]=="MYSORE"]
                            ka=k[k["END"]=="KANYAKUMARI"]
                            t1=ch["TICKETS"]
                            t2=ba["TICKETS"]
                            t3=ra["TICKETS"]
                            t4=my["TICKETS"]
                            t5=ka["TICKETS"]
                            total1=t1.sum()
                            total2=t2.sum()
                            total3=t3.sum()
                            total4=t4.sum()
                            total5=t5.sum()
                            x=["Chennai","Bangalore","Rameshwaram","Mysore","Kanyakumari"]
                            y=[total1,total2,total3,total4,total5]
                            plt.figure(figsize=(8,5))
                            plt.bar(x,y,color="#4A90E2",edgecolor="black",linewidth=1,width=0.6)
                            plt.title("Remaining tickets per destination",fontsize=16,fontweight="bold")
                            plt.ylabel("Number of tickets remaining",fontsize=12)
                            plt.xlabel("Destination",fontsize=12)
                            plt.grid(axis="y",color="gray",linestyle="--",linewidth=0.5,alpha=0.5)
                            plt.xticks(rotation=20)
                            plt.tight_layout()
                            plt.show()
                            print()
                            input("Press Enter to continue...")
                            continue
                        elif c=="1":
                            k=pd.read_csv(r"E:\AnushkaProjecy\IP-Project-\booking.txt")
                            ch=k[k["to"]=="Chennai"]
                            ba=k[k["to"]=="Bangalore"]
                            ra=k[k["to"]=="Rameshwaram"]
                            my=k[k["to"]=="Mysore"]
                            ka=k[k["to"]=="Kanyakumari"]
                            t1=ch["to"]
                            t2=ba["to"]
                            t3=ra["to"]
                            t4=my["to"]
                            t5=ka["to"]
                            total1=len(t1)
                            total2=len(t2)
                            total3=len(t3)
                            total4=len(t4)
                            total5=len(t5)
                            x=["Chennai","Bangalore","Rameshwaram","Mysore","Kanyakumari"]
                            y=[total1,total2,total3,total4,total5]
                            plt.figure(figsize=(8,5))
                            plt.bar(x,y,color="#4A90E2",edgecolor="black",linewidth=1,width=0.6)
                            plt.title("Remaining tickets per destination",fontsize=16,fontweight="bold")
                            plt.ylabel("Number of tickets remaining",fontsize=12)
                            plt.xlabel("Destination",fontsize=12)
                            plt.grid(axis="y",color="gray",linestyle="--",linewidth=0.5,alpha=0.5)
                            plt.xticks(rotation=20)
                            plt.tight_layout()
                            plt.show()
                            print()
                            input("Press Enter to continue...")
                            continue
                        elif c=="3":
                            break
                        else:
                            print()
                            print("Invalid input")
                            print()
                            continue
                        
                
                
                    
            elif op=='6':
                e.to_csv(r"E:\AnushkaProjecy\IP-Project-\busdetail.txt")
                start()

            else:
                print("\nInvalid option. Please choose from the menu.")

 
 
 
 
 
 
 
 
 
 
def start():
    print(r"""

                    __        __   _                            _           ____  _      _   _  ____  ____  _    _  ____     _
                    \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___    | __ )| |    | | | || ___|| __ )| |  | |/ ___|   | |   
                     \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \   |  _ \| |    | | | || __| |  _ \| |  | |\___ \   | |
                      \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |  | |_) | |___ | |_| || |__ | |_) | |__| | ___) |  |_|
                       \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   |____/|_____| \___/ |____||____/ \____/ |____/   (_)
                     

 
""")
    print("""How would you like to explore today:
        1.Admin
        2.User
        3.Exit""")
    print()
    
    ch=input("Enter your choice: ")
    if ch=='1':
        admin()
            
    elif ch=='2':
        home_page()
    elif ch=='3':
        page_exit()
             

    else:
        print("Invalid input")
        start()
start()

