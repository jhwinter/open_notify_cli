#!/usr/bin/env python3

import datetime
import sys

import requests


def display_iss_location() -> bool:
    """Display current ISS location over Earth (latitude/longitude)

    :return: function executed correctly
    :rtype: bool
    """

    res = requests.get("http://api.open-notify.org/iss-now.json").json()
    time = datetime.datetime.now()
    latitude: float = res["iss_position"]["latitude"]
    longitude: float = res["iss_position"]["longitude"]
    print(f"The ISS current location at {time} is ({latitude}, {longitude})")

    return True


def display_iss_pass_times(latitude: float, longitude: float) -> bool:
    """Display predictions when the space station will fly over a particular
    location

    :param latitude: latitude of space station
    :type latitude: float
    :param longitude: longitude of space station
    :type longitude: float
    :return: function executed correctly
    :rtype: bool
    """

    res = requests.get(f"http://api.open-notify.org/iss-pass.json?lat={latitude}&lon={longitude}").json()
    for iss_pass in res["response"]:
        time = iss_pass["risetime"]
        duration: int = iss_pass["duration"]
        print(f"The ISS will be overhead {latitude, longitude} at {time} for {duration}")

    return True


def display_people_in_space() -> bool:
    """The number of people in space at this moment. List of names when known.

    :return: function executed correctly
    :rtype: bool
    """

    res = requests.get("http://api.open-notify.org/astros.json").json()
    number: int = res["number"]
    craft: str = res["people"][0]["craft"]
    names: list = [person["name"] for person in res["people"]]
    names_str: str = ", ".join(names)
    print(f"There are {number} people aboard the {craft}. They are {names_str}")

    return True


def main(argv):
    if argv[1] == "loc":
        display_iss_location()
    elif argv[1] == "pass":
        display_iss_pass_times(latitude=argv[2], longitude=argv[3])
    elif argv[1] == "people":
        display_people_in_space()
    else:
        print("Invalid argument.")


if __name__ == "__main__":
    main(sys.argv)
