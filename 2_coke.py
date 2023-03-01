"""
File name:                   2_coke.py
Description:                 Machine sells Coke for 50 cents and only accepts coins in denominations of 25, 10, 5 cents
                             Once the user inputs atleast 50 cents, output how many cents in change the user is owed.
                             Assume that the user will only input integers, and ignore any integer that isn't an accepted denomination.
Created:                     Faran Bhatti
Edited:                      2023-03-01 by Faran Bhatti (FB)
Last Edited:                 2023-03-01 by Faran Bhatti (FB)
"""
def main():
    # Price of coke is 50 cents passed to the function change_owed
    change_owed(50)

def change_owed(price_coke):
    while (price_coke > 0):
        print(f"Amount Due: {price_coke}")
        coin_inserted = int(input("Insert Coin: "))
        match coin_inserted:
            case 25:
                price_coke -= coin_inserted            
            case 10:
                price_coke -= coin_inserted
            case 5:
                price_coke -= coin_inserted
            case _:
                pass
        if (price_coke <= 0):
            print(f"Change Owed: {abs(price_coke)}")

main()