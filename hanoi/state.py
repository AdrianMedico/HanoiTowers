

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

        self.towers = towers


        # How the towers will be stored? Directly? Is that a good idea?
        #raise NotImplementedError()

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
        rep = str(self.n_discs), self.towers.__str__(), str(self.depth), str(self.move_id), str(self.source), str(self.target)

        return rep

    def __str__(self):
        """
        Returns a string with the representation of the state in the requested format.

        :return: A string with the representation of the state in the requested format

        """

        self.state_repr = ""

        for i in range(self.n_discs - 1, -1, -1):  # for each row
            for tower in self.towers:  # for each tower
                if i >= len(tower.discs):
                    self.state_repr += tower.fill_row(self.n_discs, 0)
                    self.state_repr += " "
                else:
                    self.state_repr += tower.fill_row(self.n_discs, tower.discs[i])
                    self.state_repr += " "

            self.state_repr += '\n'

        return self.state_repr
