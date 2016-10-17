def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    if city == "Tampa":
        return 220
    if city == "Pittsburgh":
        return 222
    if city == "Los Angeles":
        return 475


def rental_car_cost(days):
    total = 40 * days
    if days >= 7:
        total -= 50
    elif days >= 3:
        total -= 20
    return total


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days) + spending_money

print (trip_cost("Pittsburgh", 4, 500))
