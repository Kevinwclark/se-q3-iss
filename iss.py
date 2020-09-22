#!/usr/bin/env python

__author__ = 'Kevin Clark'

import requests


def obtain_astronauts():
    """obtains a list of astronauts, prints full names,
    the spacecraft they are aboard, and the total number
    of astronauts in space
    """
    r = requests.get('http://api.open-notify.org/astros.json')
    astros = r.text
    print(astros)
    return astros


def current_coord():
    """obtains geographic coordinates of ISS along with
    timestamp
    """
    r = requests.get('http://api.open-notify.org/iss-now.json')
    coords = r.text
    print(coords)
    return coords


def graphic_display():
    """creates a graphic screen with the world map,
    registers an icon for the ISS and moves the ISS to
    its current lat/lon on the map"""
    pass


def main():
    obtain_astronauts()
    current_coord()


if __name__ == '__main__':
    main()
