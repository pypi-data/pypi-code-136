def game():
    while True:
        try:
            RESPONSE = int(input("When were you born? e.g 'year' : "))
            if RESPONSE >= 2000 and RESPONSE <= 2022:
                print("You were born in 21st century")
            elif RESPONSE >= 1900 and RESPONSE <= 1999:
                print("You were born in 20th century")
            elif RESPONSE == 1899 or RESPONSE <= 1898:
                print("You should not be running this.")
            else:
                print("Something went wrong")
            break
        except TypeError:
            print("Error: did you provide digit e.g 1")
        except ValueError:
                print("Did you enter the right value? ")
        except TypeError:
            print("Error: did you provide digit e.g 1")
        except ValueError:
                print("Did you enter the right value? ")
