"""from datetime import datetime
import numpy as np
current_datetime = datetime.now().date()
date_str = input("Please enter the date on which you would like to book your ticket (dd-mm-yyyy): ")
        try:
            booking_date = datetime.strptime(date_str, "%d-%m-%Y").date()
month=int(current_datetime.strftime("%m"))
year=int(current_datetime.strftime("%y"))"""
  

current_datetime = datetime.now().date()
month=int(current_datetime.strftime("%m"))
m=month+3
if m>month
