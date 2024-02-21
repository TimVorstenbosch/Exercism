"""Functions to automate Conda airlines ticketing system."""

import math

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seat_dict = {0: "A", 1: "B", 2:"C", 3:"D"}
    for i in range(0,number):
        yield seat_dict[i % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    seat_dict = {1: "A", 2: "B", 3:"C", 4:"D"}
    for i in range(0,number):
        row = math.floor( (i+4) / 4)
        row = row if row < 13 else row +1
        yield str( row ) + seat_dict[i % 4 + 1]

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    return {passenger:seat for passenger, seat in zip(passengers, generate_seats( len(passengers) ) ) }

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    length_flight_id = len(flight_id)
    for seat_number in seat_numbers:
        yield seat_number + flight_id + "0" * (12 - len(seat_number) - length_flight_id)


for seat in generate_seats(60):
    print(seat)
