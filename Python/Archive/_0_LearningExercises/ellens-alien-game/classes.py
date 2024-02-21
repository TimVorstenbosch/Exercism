"""Solution to Ellen's Alien Game exercise."""

def new_aliens_collection(alien_positions):
    return  [Alien(x_coor,y_coor) for x_coor,y_coor in alien_positions]


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    base_health = 3
    total_aliens_created = 0

    def __init__(self, x_coor, y_coor):
        self.x_coordinate = x_coor
        self.y_coordinate = y_coor
        self.health = self.base_health
        Alien.total_aliens_created += 1

    def hit(self):
        self.health = max(0, self.health - 1)

    def is_alive(self):
        return self.health > 0

    def teleport(self, x_coor, y_coor):
        self.x_coordinate = x_coor
        self.y_coordinate = y_coor

    def collision_detection(self, obj):
        pass
    