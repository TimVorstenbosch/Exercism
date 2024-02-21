"""Functions which helps the locomotive engineer to keep track of the train."""

from itertools import chain

def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    return [each_wagons_id[2]] + missing_wagons + each_wagons_id[3:] + each_wagons_id[:2]


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route["stops"] = [value for value in kwargs.values()]
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return route | more_route_information


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    switched_wagons = wagons_rows.copy()

    switched_wagons[1][0], switched_wagons[0][1] = wagons_rows[0][1], wagons_rows[1][0]

    switched_wagons[2][0] , switched_wagons[0][2] = wagons_rows[0][2] ,wagons_rows[2][0]

    switched_wagons[1][2] , switched_wagons[2][1] = wagons_rows[2][1] , wagons_rows[1][2]

    return switched_wagons 

