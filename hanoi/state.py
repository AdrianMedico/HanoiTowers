from hanoi.tower import Tower

class State:
    """
    Class for storing and managing Hanoi game states.
    """

    DISC_CHAR = '#'
    NON_DISC_CHAR = '.'
    ROD_CHAR = '|'

    def __init__(self, move_id, depth, moved_disc, source, target, towers, n_discs):
        """
        Initializes a state with all the information needed to represent it in the requested format.

        :param move_id: Identifier of the move. Ideally, the step number.
        :param depth: Recursion depth at which this state is generated.
        :param moved_disc: The disc moved to reach this state. Ideally, a disk is defined just by its size.
        :param source: Tower from which the disc is moved.
        :param target: Tower to which the disc is moved.
        :param towers: Towers of the game.
        :param n_discs: Number of discs of the game.
        """

        self.move_id = move_id
        self.depth = depth

        self.moved_disc = moved_disc
        self.source = source
        self.target = target
        self.n_discs = n_discs

        self.towers = []

        # Utilizar solo listas, dejar a parte las torres.!!!!
        for tower in towers:
            self.towers.append(tower.as_list())


        """
        count = 0
        n_towers = 3
        while count < n_towers:
            self.towers[count].discs = towers[count].as_list()
            count += 1
        """

    def get_tower(self, idx):
        """
        Returns the tower corresponding to the idx. Depending on the implementation of the state, this method can be
        invalid. If so, raise an exception and justify it in the report.

        :param idx: Index of the tower.
        :return: The tower corresponding to the idx.
        """
        return self.towers[idx]

    def __repr__(self):
        """
        Returns a string with the internal representation of the state. This method can be used to represent the state
        information in a different format than the requested.

        :return: A string with the internal representation of the state.
        """
        #rep = str(self.n_discs), self.towers.__str__(), str(self.depth), str(self.move_id), str(self.source), str(self.target)
        pass

    def __str__(self):
        """
        Returns a string with the representation of the state in the requested format.

        :return: A string with the representation of the state in the requested format

        """

        self.state_repr = ""

        for i in range(self.n_discs - 1, -1, -1):  # for each row
            for tower in self.towers:  # for each tower
                if i >= len(tower):
                    self.state_repr += self.fill_row(self.n_discs, 0)
                    self.state_repr += " "
                else:
                    self.state_repr += self.fill_row(self.n_discs, tower[i])
                    self.state_repr += " "

            self.state_repr += '\n'

        return self.state_repr

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