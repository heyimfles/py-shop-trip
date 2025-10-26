from app.customers import customers
from app.shops import shops
from app.fuel import fuel_price


def shop_trip() -> None:
    for customer in customers.values():
        print(f"{customer.name} has {customer.money} dollars")
        trip = customer.calculate_trip_fuel(shops, fuel_price)
        store_we_go_to = next(iter(trip["cheapest trip"]))
        prices = customer.calculate_trip_products(shops)
        sum_of_shopping = customer.calc_sum_price(prices)
        for shop, fuel_cost in trip["fuel prices"].items():
            sum_of_everything = sum_of_shopping[shop] + (fuel_cost * 2)
            print(f"{customer.name}'s trip to the {shop} costs {sum_of_everything:.2f}")

        if customer.money > sum_of_everything:
            print(
                f"{customer.name} rides to "
                f"{store_we_go_to}"
            )
            location_home = customer.location
            customer.location = shops[next(iter(trip["cheapest trip"]))].location

            print()

            customer.receipt(prices, store_we_go_to)

            print()

            print(f"{customer.name} rides home")
            customer.location = location_home

            remaining_money = (
                customer.money
                - (next(iter(trip["cheapest trip"].values())) * 2)
                - sum_of_shopping[store_we_go_to]
            )
            print(f"{customer.name} now has {remaining_money:.2f} dollars")

            print()
        else:
            print(
                f"{customer.name} doesn't have enough "
                "money to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
