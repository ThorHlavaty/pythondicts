hotel = [ {
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {},
}, {
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {}, }, {
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {}, }] 

def checkout():
    checking_out = []
    y = "y"
    while y == 'y':
        takes_a_key = input("What room number is checking out? ")
        if takes_a_key in hotel:
            checking_out.append(hotel[takes_a_key])
            hotel[takes_a_key] = {}
            print(f"Our current roster is\n\n{hotel}\n\nGuests currently checking out are \n\n{checking_out}\n")
            y = input("Is someone else checking out? [y/n]: ")
        else:
            print("I didn't catch that.")
    return checking_out
print(checkout())
print(hotel)
        

def open():
    open_again = "y"
    while open_again == "y":
        with open(input("What would you like to read? ") as hotel_file:
        hotel_json = json.load(hotel_file)
        print(hotel_json)
        open_again = input("Would you like to look at a new file? [y/n]: ")