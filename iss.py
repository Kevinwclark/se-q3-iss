#!/usr/bin/env python

__author__ = 'Kevin Clark with help from Joseph Hafed'

import requests
import turtle
import time


def obtain_astronauts():
    """Obtains a list of astronauts, prints full names,
    the spacecraft that are aboard, and the total number
    of astronauts in space"""
    r = requests.get('http://api.open-notify.org/astros.json')
    astros = r.json()
    print(f'Total # of astronauts: {astros["number"]}')
    for i in astros["people"]:
        print(f'Currently on board the: {i["craft"]}, name: {i["name"]}')


def current_coord():
    """Obtains geographic coordinates of ISS along with
    timestamp"""
    r = requests.get('http://api.open-notify.org/iss-now.json')
    coords = r.json()
    lng = float(coords["iss_position"]["longitude"])
    lat = float(coords["iss_position"]["latitude"])
    new_coords = [lng, lat]
    return new_coords


def graphic_display():
    """Creates a graphic screen with the world map,
    registers an icon for the ISS and moves the ISS to
    its current lat/lon on the map. Adds yellow dot for
    Indianapolis geolocation"""
    indi_data = overhead_indi()
    coords = current_coord()
    wn = turtle.Screen()
    wn.bgpic('map.gif')
    wn.setup(width=720, height=360)
    wn.setworldcoordinates(-180, -90, 180, 90)

    wn.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.penup()
    iss.goto(coords[0], coords[1])
    iss.shape('iss.gif')

    indi = turtle.Turtle()
    indi.penup()
    indi.goto(-86.158068, 39.768403)
    indi.shape('circle')
    indi.color('yellow')
    indi.turtlesize(0.1)

    indi_text = turtle.Turtle()
    indi_text.penup()
    indi_text.color('white')
    indi_text.goto(-80.158068, 39.768403)
    indi_text.write(f"""
    The next time the ISS will pass over Indianapolis
    is on: {indi_data[0]} for a duration of {indi_data[1]}
    seconds""")

    wn.exitonclick()


def overhead_indi():
    """Finds next time ISS will be over Indianapolis,
    Indiana and prints"""
    r = requests.get(
        """
        http://api.open-notify.org/iss/v1/?lat=40.027435&lon=-86.158068&alt=1650&n=1
        """
        )
    resp = r.json()
    date = resp['response'][0]['risetime']
    seconds = resp['response'][0]['duration']
    overhead_date = time.ctime(date)
    indi_data = [overhead_date, seconds]
    return indi_data


def main():
    obtain_astronauts()
    current_coord()
    overhead_indi()
    graphic_display()


if __name__ == '__main__':
    main()
