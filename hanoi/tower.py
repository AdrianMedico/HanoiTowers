from .hanoi_exception import HanoiException


class Tower:
    """
    Class for storing and managing Hanoi game towers.
    """

    def __init__(self):
        """
        Initializes the tower.
        """
        self.discs = []

    def is_empty(self):
        """
        Returns if a tower is empty or not, it is, if the tower has no discs.

        :return: True if is empty, it is, if the tower has no discs, False otherwise
        """
        if len(self.discs) == 0:
            return True
        else:
            return False

    def size(self):
        """
        Returns the size (number of discs) of the tower.

        :return: The size (number of discs) of the tower.
        """
        return len(self.discs)

    def pop_disc(self):
        """
        Removes a disc from the top of the tower and returns it.
        Raises an HanoiException if the tower is empty.

        :return: The disc removed from the top of the tower.
        """
        if self.is_empty():
            raise HanoiException("Empty tower")
        else:
            return self.discs.pop()

    def push_disc(self, disc):
        """
        Adds a disc to the top of the tower.
        Raises an HanoiException if the disc is bigger that the disc at the top of the tower.

        :param disc: The disc to be added to the top of the tower.
        """
        length = len(self.discs)
        if length != 0:
            if self.discs[length-1] < disc:
                raise HanoiException("The disc is bigger than the current top disc")

        self.discs.append(disc)

    def as_list(self):
        """
        Returns the discs of the tower as a new list (it means that if the internal representation of the tower is a
        list, it should return a copy of it).

        :return: A list containing the discs of the tower.
        """
        return self.discs.copy()

    def __repr__(self):
        """
        Returns a string with the internal representation of the tower. This method can be used to represent the tower
        information in a different format than the requested.

        :return: A string with the internal representation of the state.
        """
        pass

    def __str__(self, n_discs):
        """
        Returns a string with the representation of the tower in the requested format.

        :return: A string with the representation of the tower in the requested format
        """

        self.tower_representation = ""

        for i in range(n_discs - 1, -1, -1):  # Descending order to start with top tower. i.e n_discs = 5. The loop works in the order: 4, 3, 2, 1, 0.
            if i >= len(self.discs):
                self.tower_representation += self.fill_row(n_discs, 0)  # If the iteration is higher than the tower length means that is a void row, then we pass trough a zero value as the number
            else:
                self.tower_representation += self.fill_row(n_discs, self.discs[i])

        return self.tower_representation

    def fill_row(self, n_discs, disc_value):
        """ le añado las almohadillas segun el input, entonces se le añade la pipe
        y se le añaden las almohadillas de la derecha,
        seguidamente utilizamos el metodo .center() que genera un padding teniendo en cuenta
        el numero total de caracteres que debe tener la string.

        :param n_discs: the total amount of discs
        :param disc_value: the current value for the row
        :return: a row with the specifications
        """

        self.string_pads = ""
        self.number_of_pipes = 1
        self.double_val = 2

        for i in range(disc_value):
            self.string_pads += "#"

        self.row = self.string_pads + "|"

        self.row += self.string_pads

        self.row = self.row.center((n_discs * self.double_val) + self.number_of_pipes, ".")

        return self.row

