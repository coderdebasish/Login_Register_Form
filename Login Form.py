# Programmed By Debasish Mohanty
# Project Name = Login Register Form
# Importing modules
import os


# Functions
def capitalize(z):
    return z.title()


def gender_full_name(g):
    if g == "m" or g == "M":
        g = "Male"
    elif g == "f" or g == "F":
        g = "Female"
    elif g == "r" or g == "R":
        g = "Rather Not To Say"
    return g


# Global Variables

# Main Programme
while True:
    print("Welcome To Register/Login Form Programme")
    a = 0
    while a != "1" or a != "2" or a != "3":
        print("Press 1 for Register/Sign Up\nPress 2 for Login\nPress 3 for Password Recovery")
        a = input("Enter your choice : ")
        if a == "1" or a == "2" or a == "3":
            break
        else:
            print("Invalid Input! Try Again!")

# ***************************************************** if a = 1 ******************************************************
    if a == "1":
        while True:
            Username = input("Enter your username : ")
            if os.path.exists(f"Users\\{Username}.txt"):
                print("The user name has already taken ")
            else:
                print("This is a new username. Let's continue.")
                break
        Name = input("Enter your Name : ")
        Name = capitalize(Name)
        print("Enter your Date Of Birth Details")
        while True:
            date = input("Date : ")
            if date.isnumeric():
                if 0 < int(date) <= 31:
                    break
                else:
                    print("Invalid Date Input!")
                    pass
            else:
                print("Invalid Date Input!")
                pass
        while True:
            Month = input("Month in No. : ")
            if Month.isnumeric():
                if 0 < int(Month) <= 12:
                    break
                else:
                    print("Invalid Month Input!")
                    pass
            else:
                print("Invalid Month Input!")
                pass
        while True:
            Year = input("Year : ")
            if Year.isnumeric():
                if 1900 < int(Year) <= 2020:
                    break
                else:
                    print("Invalid Year Input!")
                    pass
            else:
                print("Invalid Year Input!")
                pass
        while True:
            gender = input("Enter your Gender(M For Male / F For Female / R for Rather Not To Say) : ")
            if gender == "M" or gender == "m" or gender == "F" or gender == "f" or gender == "R" or gender == "r":
                gender = gender_full_name(gender)
                break
            else:
                print("Invalid Input!")
                pass

        print("Enter Your Address Details")
        City = input("City : ")
        City = capitalize(City)
        while True:
            Pin = input("Pin : ")
            if Pin.isnumeric():
                break
            else:
                print("Invalid Input!")
        State = input("State : ")
        State = capitalize(State)
        Country = input("Country : ")
        Country = capitalize(Country)
        while True:
            Phone = input("Enter your Mobile No. : ")
            if Phone.isnumeric():
                break
            else:
                print("Invalid Mobile no!")
        Email = input("Enter your Email : ")
        password = input("Enter a Password and remember it : ")
        while True:
            re_password = input("Re Enter Your Password : ")
            if re_password == password:
                break
            else:
                print("Enter Same password!")
                pass
        while True:
            print("********Check The Preview********")
            print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(password) * "x")
# Editing Details
            edit = ""
            while edit != "Y" or edit != "y" or edit != "N" or edit != "n":
                edit = input("\nDo you want to edit something? (y/n) : ")
                if edit == "n" or edit == "N":
                    break
                elif edit == "Y" or edit == "y":
                    print("Which thing you want to edit? Choose any one of them.")
                    print("Press 1 For Changing Your Username")
                    print("Press 2 For Changing Your Name")
                    print("Press 3 For Changing Your DOB's Date")
                    print("Press 4 For Changing Your DOB's Month")
                    print("Press 5 For Changing Your DOB's Year")
                    print("Press 6 For Changing Your Gender")
                    print("Press 7 For Changing Your City")
                    print("Press 8 For Changing Your Pin")
                    print("Press 9 For Changing Your State")
                    print("Press 10 For Changing Your Country")
                    print("Press 11 For Changing Your Mobile No.")
                    print("Press 12 For Changing Your Email")
                    while True:
                        to_be_edit = input("Enter your Choice : ")
                        if to_be_edit.isnumeric():
                            if 0 < int(to_be_edit) <= 12:
                                break
                            else:
                                print("Invalid Input!")
                        else:
                            print("Invalid Input!")
                            pass

                    if to_be_edit == "1":
                        while True:
                            Username = input("Enter Your New Username : ")
                            if os.path.exists(f"Users\\{Username}.txt"):
                                print("The user name has already taken ")
                            else:
                                print("This is a new username.")
                                break
                        print("********Check The Preview********")
                        print(f"Username* = {Username}\nName = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(password) * "x")
                    elif to_be_edit == "2":
                        Name = input("Enter Your New Name : ")
                        Name = capitalize(Name)
                        print("********Check The Preview********")
                        print(f"Name* = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(password) * "x")
                    elif to_be_edit == "3":
                        while True:
                            date = input("Enter Your New DOB's  Date : ")
                            if date.isnumeric():
                                if 0 < int(date) <= 31:
                                    break
                                else:
                                    print("Invalid Date Input!")
                                    pass
                            else:
                                print("Invalid Date Input!")
                                pass

                        print("********Check The Preview********")
                        print(f"Name = {Name}\nDate of Birth* = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(password) * "x")
                    elif to_be_edit == "4":
                        while True:
                            Month = input("Enter Your New DOB's  Month : ")
                            if Month.isnumeric():
                                if 0 < int(Month) <= 12:
                                    break
                                else:
                                    print("Invalid Month Input!")
                                    pass
                            else:
                                print("Invalid Input!")
                                pass

                        print("********Check The Preview********")
                        print(f"Name = {Name}\nDate of Birth* = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(password) * "x")
                    elif to_be_edit == "5":
                        while True:
                            Year = input("Enter Your New DOB's  Year : ")
                            if Year.isnumeric():
                                if 1900 < int(Year) <= 2020:
                                    break
                                else:
                                    print("Invalid Year Input!")
                                    pass
                            else:
                                print("Invalid Year Input!")
                                pass

                        print("********Check The Preview********")
                        print(f"Name = {Name}\nDate of Birth* = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(password) * "x")
                    elif to_be_edit == "6":
                        while True:
                            gender = input("Enter your Gender(M For Male / F For Female / R for Rather Not To Say) : ")
                            if gender == "M" or gender == "m" or gender == "F" or gender == "f" or gender == "R" or gender == "r":
                                gender = gender_full_name(gender)
                                break
                            else:
                                print("Invalid Input!")
                                pass
                        print("********Check The Preview********")
                        print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender* = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(password) * "x")
                    elif to_be_edit == "7":
                        City = input("New City : ")
                        City = capitalize(City)
                        print("********Check The Preview********")
                        print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity* = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(password) * "x")
                    elif to_be_edit == "8":
                        while True:
                            Pin = input("New Pin : ")
                            if Pin.isnumeric():
                                break
                            else:
                                print("Invalid Input! The Pin should only be numeric.")
                        print("********Check The Preview********")
                        print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin* = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(password) * "x")
                    elif to_be_edit == "9":
                        State = input("New State : ")
                        State = capitalize(State)
                        print("********Check The Preview********")
                        print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState* = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(password) * "x")
                    elif to_be_edit == "10":
                        Country = input("New Country : ")
                        Country = capitalize(Country)
                        print("********Check The Preview********")
                        print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry* = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(password) * "x")
                    elif to_be_edit == "11":
                        while True:
                            Phone = input("New Mobile No. : ")
                            if Phone.isnumeric():
                                print("********Check The Preview********")
                                print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No.* = {Phone}\nEmail = {Email}\nPassword =" + len(password) * "x")
                                break
                            else:
                                print("Invalid Mobile Number!")
                                pass
                    elif to_be_edit == "12":
                        Email = input("New Email : ")
                        print("********Check The Preview********")
                        print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail* = {Email}\nPassword =" + len(password) * "x")

                    else:
                        print("Invalid Input!")
                        break
            if edit == "n" or edit == "N":
                break
            else:
                pass
        f = open(f"Users\\{Username}.txt", "w")
        f.write(f"{password}\n{Name}\n{date}\n{Month}\n{Year}\n{gender}\n{City}\n{Pin}\n{State}\n{Country}\n{Phone}\n{Email}")
        f.close()
        print("You are registered as a user. Now you can Login with your Username and Password.")

# ***************************************************** if a = 2 ******************************************************
    elif a == "2":
        while True:
            Username = input("Enter your username : ")
            if os.path.exists(f"Users\\{Username}.txt"):
                break
            else:
                print("No user with this username exists")
                print("Try Again!")
        with open(f"Users\\{Username}.txt") as x:
            pass_word = x.readline()
            Name = x.readline()
            date = x.readline()
            Month = x.readline()
            Year = x.readline()
            gender = x.readline()
            City = x.readline()
            Pin = x.readline()
            State = x.readline()
            Country = x.readline()
            Phone = x.readline()
            Email = x.readline()
            # Removing \n
            pass_word = pass_word.strip()
            Name = Name.strip()
            date = date.strip()
            Month = Month.strip()
            Year = Year.strip()
            gender = gender.strip()
            City = City.strip()
            State = State.strip()
            Pin = Pin.strip()
            Country = Country.strip()
            Phone = Phone.strip()
            Email = Email.strip()
        Password = ""
        count = 0
        while Password != pass_word:
            Password = input("Enter your Password : ")
            if Password == pass_word:
                while True:
                    print("\n*************** Your Details Below ***************\n")
                    # print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nPhone = {Phone}\nEmail = {Email}")
                    while True:

                        print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(pass_word) * "x")
# Editing Profiles
                        edit = ""
                        while edit != "Y" or edit != "y" or edit != "N" or edit != "n":
                            edit = input("\nDo you want to edit Your Profile? (y/n) : ")
                            if edit == "n" or edit == "N":
                                break
                            elif edit == "Y" or edit == "y":
                                print("Which thing you want to edit? Choose any one of them.")
                                # print("Press 1 For Changing Your Username")
                                print("Press 1 For Changing Your Name")
                                print("Press 2 For Changing Your DOB's Date")
                                print("Press 3 For Changing Your DOB's Month")
                                print("Press 4 For Changing Your DOB's Year")
                                print("Press 5 For Changing Your Gender")
                                print("Press 6 For Changing Your City")
                                print("Press 7 For Changing Your Pin")
                                print("Press 8 For Changing Your State")
                                print("Press 9 For Changing Your Country")
                                print("Press 10 For Changing Your Mobile No.")
                                print("Press 11For Changing Your Email")
                                while True:
                                    to_be_edit = input("Enter your Choice : ")
                                    if to_be_edit.isnumeric():
                                        if 0 < int(to_be_edit) <= 11:
                                            break
                                        else:
                                            print("Invalid Input!")
                                    else:
                                        print("Invalid Input!")
                                        pass

                                # if to_be_edit == "1":
                                #     while True:
                                #         Username = input("Enter Your New Username : ")
                                #         if os.path.exists(f"Users\\{Username}.txt"):
                                #             print("The user name has already taken ")
                                #         else:
                                #             print("This is a new username.")
                                #             break
                                #     print("********Check The Preview********")
                                #     print(f"Username* = {Username}\nName = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(pass_word) * "x")

                                if to_be_edit == "1":
                                    Name = input("Enter Your New Name : ")
                                    Name = capitalize(Name)
                                    print("********Check The Preview********")
                                    print(f"Name* = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(pass_word) * "x")
                                elif to_be_edit == "2":
                                    while True:
                                        date = input("Enter Your New DOB's  Date : ")
                                        if date.isnumeric():
                                            if 0 < int(date) <= 31:
                                                break
                                            else:
                                                print("Invalid Date Input!")
                                                pass
                                        else:
                                            print("Invalid Date Input!")
                                            pass

                                    print("********Check The Preview********")
                                    print(f"Name = {Name}\nDate of Birth* = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(pass_word) * "x")
                                elif to_be_edit == "3":
                                    while True:
                                        Month = input("Enter Your New DOB's  Month : ")
                                        if Month.isnumeric():
                                            if 0 < int(Month) <= 12:
                                                break
                                            else:
                                                print("Invalid Month Input!")
                                                pass
                                        else:
                                            print("Invalid Input!")
                                            pass

                                    print("********Check The Preview********")
                                    print(f"Name = {Name}\nDate of Birth* = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(pass_word) * "x")
                                elif to_be_edit == "4":
                                    while True:
                                        Year = input("Enter Your New DOB's  Year : ")
                                        if Year.isnumeric():
                                            if 1900 < int(Year) <= 2020:
                                                break
                                            else:
                                                print("Invalid Year Input!")
                                                pass
                                        else:
                                            print("Invalid Year Input!")
                                            pass

                                    print("********Check The Preview********")
                                    print(f"Name = {Name}\nDate of Birth* = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(pass_word) * "x")
                                elif to_be_edit == "5":
                                    while True:
                                        gender = input(
                                            "Enter your Gender(M For Male / F For Female / R for Rather Not To Say) : ")
                                        if gender == "M" or gender == "m" or gender == "F" or gender == "f" or gender == "R" or gender == "r":
                                            gender = gender_full_name(gender)
                                            break
                                        else:
                                            print("Invalid Input!")
                                            pass
                                    print("********Check The Preview********")
                                    print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender* = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(pass_word) * "x")
                                elif to_be_edit == "6":
                                    City = input("New City : ")
                                    City = capitalize(City)
                                    print("********Check The Preview********")
                                    print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity* = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(pass_word) * "x")
                                elif to_be_edit == "7":
                                    while True:
                                        Pin = input("New Pin : ")
                                        if Pin.isnumeric():
                                            break
                                        else:
                                            print("Invalid Input! The Pin should only be numeric.")
                                    print("********Check The Preview********")
                                    print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin* = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(pass_word) * "x")
                                elif to_be_edit == "8":
                                    State = input("New State : ")
                                    State = capitalize(State)
                                    print("********Check The Preview********")
                                    print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState* = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(pass_word) * "x")
                                elif to_be_edit == "9":
                                    Country = input("New Country : ")
                                    Country = capitalize(Country)
                                    print("********Check The Preview********")
                                    print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry* = {Country}\nMobile No. = {Phone}\nEmail = {Email}\nPassword =" + len(pass_word) * "x")
                                elif to_be_edit == "10":
                                    while True:
                                        Phone = input("New Mobile No. : ")
                                        if Phone.isnumeric():
                                            print("********Check The Preview********")
                                            print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No.* = {Phone}\nEmail = {Email}\nPassword =" + len(pass_word) * "x")
                                            break
                                        else:
                                            print("Invalid Mobile Number!")
                                            pass
                                elif to_be_edit == "11":
                                    Email = input("New Email : ")
                                    print("********Check The Preview********")
                                    print(f"Name = {Name}\nDate of Birth = {date}/{Month}/{Year}\nGender = {gender}\nCity = {City}\nPin = {Pin}\nState = {State}\nCountry = {Country}\nMobile No. = {Phone}\nEmail* = {Email}\nPassword =" + len(pass_word) * "x")

                                else:
                                    print("Invalid Input!")
                                    break
                        if edit == "n" or edit == "N":
                            break
                        else:
                            pass
                    f = open(f"Users\\{Username}.txt", "w")
                    f.write(f"{pass_word}\n{Name}\n{date}\n{Month}\n{Year}\n{gender}\n{City}\n{Pin}\n{State}\n{Country}\n{Phone}\n{Email}")
                    f.close()
                    print("Your Profile is updated.")
                    break
                break
            else:
                print("Invalid Input! Try Again!")
                count = count + 1
            if count == 1:
                print("You have Two attempts Left")
            elif count == 2:
                print("You have one attempts left")
            elif count == 3:
                print("You have zero attempts left. You have entered wrong password 3 times.")
                print("***** If you forget your Password You should go to Password Reset section in the Home Menu *****")
                break
# ***************************************************** if a = 3 ******************************************************
    elif a == "3":
        while True:
            Username = input("Enter your username : ")
            if os.path.exists(f"Users\\{Username}.txt"):
                break
            else:
                print("No user with this username exists")
                print("Try Again!")
        with open(f"Users\\{Username}.txt") as x:
            pass_word = x.readline()
            Name = x.readline()
            date = x.readline()
            Month = x.readline()
            Year = x.readline()
            gender = x.readline()
            City = x.readline()
            Pin = x.readline()
            State = x.readline()
            Country = x.readline()
            Phone = x.readline()
            Email = x.readline()
            # Removing \n
            pass_word = pass_word.strip()
            Name = Name.strip()
            date = date.strip()
            Month = Month.strip()
            Year = Year.strip()
            gender = gender.strip()
            City = City.strip()
            State = State.strip()
            Pin = Pin.strip()
            Country = Country.strip()
            Phone = Phone.strip()
            Email = Email.strip()
        count = 0
        print("Enter Your Date of Birth Details To Reset Password")
        # while True:
        while True:
            recover_date = input("Date : ")
            if recover_date.isnumeric():
                if 0 < int(recover_date) <= 31:
                    break
                else:
                    print("Invalid Date Input!")
                    pass
            else:
                print("Invalid Date Input!")
                pass
        while True:
            recover_month = input("Month in No. : ")
            if recover_month.isnumeric():
                if 0 < int(recover_month) <= 12:
                    break
                else:
                    print("Invalid Month Input!")
                    pass
            else:
                print("Invalid Month Input!")
                pass
        while True:
            recover_year = input("Year : ")
            if recover_year.isnumeric():
                if 1900 < int(recover_year) <= 2020:
                    break
                else:
                    print("Invalid Year Input!")
                    pass
            else:
                print("Invalid Year Input!")
                pass
        if recover_date == date and recover_month == Month and recover_year == Year:
            new_password = input("Enter Your New Password : ")
            while True:
                re_new_password = input("Re Enter Your Password : ")
                if re_new_password == new_password:
                    f = open(f"Users\\{Username}.txt", "w")
                    f.write(f"{new_password}\n{Name}\n{date}\n{Month}\n{Year}\n{gender}\n{City}\n{Pin}\n{State}\n{Country}\n{Phone}\n{Email}")
                    f.close()
                    print("Your Password changed. Now you can Login with your Username and Password.")
                    break
                else:
                    print("Enter same Password.")
                    pass
        else:
            print("Invalid Input! Try Again!")
            count = count + 1
        if count == 1:
            print("You have Two attempts Left")
        elif count == 2:
            print("You have one attempts left")
        elif count == 3:
            print("You have zero attempts left. You have entered wrong Date Of Birth Details 3 times. Try again!")
            break

    again = ""
    while again != "Y" or again != "y" or again != "N" or again != "n":
        again = input("\nDo you want to return to the home menu? (y/n) : ")
        if again == "Y" or again == "y":
            os.system("cls")
            break
        elif again == "n" or again == "N":
            print("***** Thanks For Using My Programme *****")
            exit()