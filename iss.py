#!/usr/bin/env python

__author__ = 'Kevin Clark with help from Joseph Hafed'

import requests
import turtle 


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
    wn = turtle.Screen()
    wn.bgpic('map.gif')
    wn.setup(width=650, height=370)

    wn.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.goto(-10, 0)

    indi = turtle.Turtle()
    indi.penup()
    indi.goto(-190, 86)
    indi.shape('circle')
    indi.color('yellow')
    indi.turtlesize(0.3)

    wn.mainloop()
    # wn.exitonclick()


def overhead_indi():
    """Finds next time ISS will be over Indianapolis,
    Indiana."""
    pass


def main():
    obtain_astronauts()
    current_coord()
    graphic_display()
    overhead_indi()


if __name__ == '__main__':
    main()
