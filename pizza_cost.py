#!/usr/bin/env python3
# Created by: Alexander Matheson
# Created on: Dec 1, 2021
# This program asks the user for the diameter of a pizza.
# It then calculates and displays the total cost of the pizza with tax.
import constants


def main():
    # input
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # process
    subtotal = constants.LABOUR + constants.RENTAL + constants.INGR * diameter
    tax = constants.TAX * subtotal
    total = subtotal + tax

    # output
    print("")
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
