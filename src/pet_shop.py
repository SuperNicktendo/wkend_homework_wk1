# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(sum):
    return sum["admin"]["total_cash"]

def add_or_remove_cash(cash, amount):
    cash["admin"]["total_cash"] += amount

def get_pets_sold(sold):
    return sold["admin"]["pets_sold"]

def increase_pets_sold(sold, amount):
    sold["admin"]["pets_sold"] += amount

def get_stock_count(stock_count):
    return len(stock_count["pets"])

def get_pets_by_breed(pets, breed):
    breed_total = []
    for pet in pets["pets"]:
        if pet["breed"] == breed:
            breed_total.append(pet["breed"])
    return breed_total

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer_cash):
    return customer_cash["cash"]

def remove_customer_cash(customer_cash, amount):
    customer_cash["cash"] -= amount

def get_customer_pet_count(pets):
    return len(pets["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

###### OPTIONAL ########

def customer_can_afford_pet(customer_cash, pet_cost):
    if customer_cash["cash"] >= pet_cost["price"]:
        return True
    else:
        return False
