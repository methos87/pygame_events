#!/usr/bin/env python

from tank import Tank


def main():
    tanks = {"a": Tank("Alpha"), "b": Tank("Beta"), "c": Tank("Gamma")}
    alive_tanks = len(tanks)

    while alive_tanks > 1:

        for tank_name in sorted(tanks.keys()):
            print(tank_name, tanks[tank_name])

        first = input("Who fires?: ").lower()
        second = input("For who?: ").lower()
        print(first)

        try:
            first_tank = tanks[first]
            second_tank = tanks[second]
        except KeyError:
            print("No such a tank! {}{}".format(first, second))
            continue

        if not first_tank.alive or not second_tank.alive:
            print("One of the tanks is dead!")
            continue

        print("*" * 30)

        first_tank.fire_at(second_tank)
        if not second_tank.alive:
            alive_tanks -= 1

        print("*" * 30)

    for tank in tanks.values():
        if tank.alive:
            print(tank.name, " is a winner!")
            break

if __name__ == '__main__':
    main()
