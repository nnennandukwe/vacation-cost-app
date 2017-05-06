# VACATION CALCULATION APP

def hotel_cost(nights):
    return nights * 140

print hotel_cost(2)

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    total = days * 40

    if days >= 7:
        return total - 50
    elif days >= 3:
        return total - 20
    return total

def trip_cost(city,days,spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
