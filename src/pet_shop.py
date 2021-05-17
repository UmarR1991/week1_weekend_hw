from os import X_OK


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, nopetssold):
    pet_shop["admin"]["pets_sold"] += nopetssold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets = []
    for x in pet_shop["pets"]:
        if x["breed"] == breed:
            pets.append(x)
    return (pets)
            
def find_pet_by_name(pet_shop, pet_name):
    for x in pet_shop["pets"]:
        if x["name"] == pet_name:
            return (x)
            
def remove_pet_by_name(pet_shop, pet_name):
    i = -1
    for x in pet_shop["pets"]:
        i = i+1
        if x["name"] == pet_name:
            pet_shop["pets"].pop(i)
    return(x)

def add_pet_to_stock(pet_shop, new_pet):
   pet_shop["pets"].append(new_pet)
   return len(pet_shop["pets"])

def get_customer_cash(customers):
   x = customers["cash"]
   return(x)

def remove_customer_cash(customer, amount):
    customer["cash"] = customer["cash"] - amount
    return(customer["cash"])

def get_customer_pet_count(customer):
    x = len(customer["pets"])
    return(x)

def add_pet_to_customer(customer, new_pet):
    x = customer["pets"]
    x.insert(0, new_pet)
    return(x)

def  customer_can_afford_pet(customer, new_pet):
    if (customer["cash"] >= new_pet["price"]):
       return(True)
    else:
        return(False)
   
def sell_pet_to_customer(pet_shop, new_pet, customer):
   
    if new_pet is not None: 
        
        if (customer_can_afford_pet(customer, new_pet) == True):
            # adds pet to the customer in pameter
            add_pet_to_customer(customer, new_pet)
            # using pet shop pass 1 to icrease the value in the pet shop sold item
            increase_pets_sold(pet_shop, 1)
            remove_customer_cash(customer, new_pet["price"])
            add_or_remove_cash(pet_shop, new_pet["price"])

