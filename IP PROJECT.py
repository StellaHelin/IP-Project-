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
            print("""
                                                  ____              _              _____ _      _        _   
                                                 | __ )  ___   ___ | | __   __ _  |_   _(_) ___| | _____| |_ 
                                                 |  _ \ / _ \ / _ \| |/ /  / _` |   | | | |/ __| |/ / _ \ __|
                                                 | |_) | (_) | (_) |   <  | (_| |   | | | | (__|   <  __/ |_ 
                                                 |____/ \___/ \___/|_|\_\  \__,_|   |_| |_|\___|_|\_\___|\__|""")
                                                                 
            page_book()
        elif choice==2:
            print("""  
                                                   __  __         ____              _    _             
                                                  |  \/  |_   _  | __ )  ___   ___ | | _(_)_ __   __ _ 
                                                  | |\/| | | | | |  _ \ / _ \ / _ \| |/ / | '_ \ / _` |
                                                  | |  | | |_| | | |_) | (_) | (_) |   <| | | | | (_| |
                                                  |_|  |_|\__, | |____/ \___/ \___/|_|\_\_|_| |_|\__, |
                                                           |___/                                  |___/ """)
            page_booked()
        elif choice==3:
            print("""                             ____                      _  _____ _      _        _   
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
          print("""   ____            _                   
                     |  _ \ _____   _(_) _____      _____ 
                     | |_) / _ \ \ / / |/ _ \ \ /\ / / __|
                     |  _ <  __/\ V /| |  __/\ V  V /\__ \
                     |_| \_\___| \_/ |_|\___| \_/\_/ |___/""")
                                      
        
              
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
home_page()
