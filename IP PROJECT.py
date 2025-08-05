import pandas as pd
import numpy as np

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
        2)My booking/history
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
            print(r"""                             ____                      _  _____ _      _        _   
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
                   


def page_about():
    print("""Welcome to BlueBus, your trusted companion for seamless and affordable bus travel.

We’re a student-led initiative created with a passion for technology and a commitment to solving real-world problems. Inspired by platforms like RedBus, BlueBus aims to simplify the bus ticket booking experience — making it faster, cleaner, and smarter.

Whether you're commuting between cities, planning a trip, or just heading home, BlueBus helps you:

📅 Book tickets in seconds

📂 Access your bookings and travel history

❌ Cancel with zero stress

🧾 Get clean, clutter-free receipts

🙋 Reach support anytime

All from one simple console-based app.

This project is a part of our learning journey in software development — combining Python, MySQL, and a love for solving practical problems.

We believe smart travel should be for everyone — and BlueBus is our step in that direction.""")
    print()
    input("Please press enter to go back")


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
        elif choice2==2:
            read_review()
        elif choice2==3:
            home_page()
        else:
            print("Invalid choice")
            reviews()
def give_review():
    name=input("Enter yout name : ")
    rate=int(input("Rate your experience (1-5): "))
    if 1<=rate<=5:
        rate="⭐"*rate
    else:
        print("Please enter a rating between 1 and 5.")
        return give_review()
    description=input("Enter your review :")
    print("Rating : ",rate)
    print("Name : ",name)
    print("Review : ",description)
    print()
    confirm(rate,name,description)
def confirm(rate,name,description):
        choice3=input("Confirm details ? Y/N : ")
        if choice3=="Y":
            d={"Rating":[rate],"Name":[name],"Review":[description]}
            df=pd.DataFrame(d)
            df.to_csv(r"C:\Users\stell\OneDrive\Desktop\IP\review.csv",header=False,mode="a",index=False)
            print()
            print("Thanks for sharing your thoughts with BlueBus! Safe travels!")
            print()
            input("Press enter to back")
            print()
            home_page()
        elif choice3=="N":
            return give_review()
        else:
            print("Invalid choice")
            print()
            return confirm(rate,name,description)
                       
    
def page_exit():
    print("""
             __   __                _                                          _      _                    __                           _  
             \ \ / /__ _  _ _ _    (_)___ _  _ _ _ _ _  ___ _  _   ___ _ _  __| |___ | |_  ___ _ _ ___    / _|___ _ _   _ _  _____ __ _| | 
              \ V / _ \ || | '_|   | / _ \ || | '_| ' \/ -_) || | / -_) ' \/ _` (_-< | ' \/ -_) '_/ -_)  |  _/ _ \ '_| | ' \/ _ \ V  V /_| 
               |_|\___/\_,_|_|    _/ \___/\_,_|_| |_||_\___|\_, | \___|_||_\__,_/__/ |_||_\___|_| \___|  |_| \___/_|   |_||_\___/\_/\_/(_)
                                 |__/                       |__/                                 """)
home_page()
print("hi")

