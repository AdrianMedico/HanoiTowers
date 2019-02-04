import logging

from .hanoi_exception import HanoiException
from .state import State
from .tower import Tower

logging.basicConfig(level=logging.INFO, format='%(levelname)-10s  %(message)s')


class HanoiGame:
    """
    Main class for management of the data structures and moves of the game.
    """

    def __init__(self, n_discs, n_towers=3):
        """
        Initializes the game with n_discs and n_towers, which defaults to 3.
        At this step, the game can be solved and stored to consult.

        Raises a HanoiException if n_discs is negative or n_towers is less than 3.

        :param n_discs: Number of disks for this game.
        :param n_towers: Number of towers for this game. Default: 3
        """
        self.min_discs = 0
        self.min_towers = 3
        self.current_discs = n_discs

        # Steps:
        # 1.- Check the parameters (Add the code after this comment)
        if n_discs < self.min_discs:
            raise HanoiException("The number of discs must be positive")
        elif n_towers < self.min_towers:
            raise HanoiException("The number of towers should be at least 3")

        # 2.- Initialize the structure attributes (Add the code after this comment)
        self.states = []  # Initialize the states list

        # 3.- Initialize the towers (Add the code after this comment)
        self.towers = [Tower(), Tower(), Tower()]
        self.fill_origin_tower(n_discs)

        # 4.- Solve and store the optimal solution
        self._solve()

    def get_state(self, step):
        """
        Returns the state at the requested step in the optimal solution.
        Raises a HanoiException if the step index is negative or bigger than the total of states in the optimal
        solution.

        :param step: The step index in the optimal solution.
        :return: The state at the requested step in the optimal solution.
        """
        length = len(self.steps)
        if step > length or step < 0:
            raise HanoiException("The introduced step should be between 0 and " + length)
        """
        En esta función falta que devuelva algo, solo tenemos  un condicional y una exception pero sin devolver nada.
        """

    def get_n_discs(self):
        """
        Returns the number of disks of this game.

        :return: The number of disks of this game.
        """
        return self.current_discs

    def get_n_towers(self):
        """
        Returns the number of towers of this game.

        :return: The number of towers of this game.
        """
        return len(self.towers)

    def get_n_states(self):
        """
        Returns the number of states of the optimal solution. Ideally, it should be the size of the structure used to
        store the optimal solution states.

        :return: The number of states of the optimal solution.
        """

        return len(self.states)

    def move(self, source, target, move_id=None, depth=None):
        """
        Moves a disk from source tower to target tower.
        Raises a HanoiException if source and target are the same or if the move is invalid (the disk moved is bigger
        than the last disk in the target tower, the source tower is empty...)

        :param source: Tower from which a disk is going to be moved.
        :param target: Tower to which a disk is going to be moved.
        :param move_id: Identifier of the movement. Useful as information for the optimal state.
        :param depth: Depth of the recursion call. Useful as information for the optimal state.
        :return: The new state generated by the move.
        """
        if source == target:
            raise HanoiException("Source and origin should be different")

        elif self.towers[source].size == 0:
            return HanoiException("The origin is empty")

        #  if not self.towers[target].is_empty() and len(self.towers[source].discs) > len(self.towers[target].discs):
        #    raise HanoiException("The disc should be ")
        moved_disc = self.towers[source].pop_disc()
        self.towers[target].push_disc(moved_disc)

        current_state = State(move_id, depth, moved_disc, source, target, self.towers, self.current_discs)

        return current_state

    def _solve(self):
        """
        Generates and stores the optimal solution, reinitializing the towers afterwards.
        """

        self._solve_rec(self.current_discs, 0, 2, 1, 0)

        # Finally reinitialize the towers
        self.towers = [Tower(), Tower(), Tower()]

    def _solve_rec(self, n_discs, source, target, aux, depth=0):
        """
        Recursive call to solve the hanoi game optimally.

        :param n_discs: Number of disks to be moved.
        :param source: Tower from which a disk is going to be moved.
        :param target: Tower to which a disk is going to be moved.
        :param aux: Tower to be used as auxiliary.
        :param depth: Depth of the recursion call. Useful as information for the optimal state.
        """

        if n_discs == 0:
            return 0
            #self.states.append(self.move(source, target, len(self.states) + 1, depth))

        else:
            self._solve_rec(n_discs - 1, source, aux, target, depth + 1)
            self.states.append(self.move(source, target, len(self.states) + 1, depth))
            self._solve_rec(n_discs - 1, aux, target, source, depth + 1)

    def print_optimal_state(self, step):
        """
        Prints the optimal state at the selected step in the required format.

        :param step: Step index of the optimal solution.
        """

        return self.states[step]

    def print_optimal_solution(self):
        """
        Prints all the states of the optimal solution in the required format.
        """
        for state in self.states:
            print(state.__str__())

    def is_finished(self):
        """
        Checks if the interactive game is finished, returns True if is finished, False otherwise.

        :return: True if the game is finished, False otherwise.
        """

        """
        No se como escribirlo en código, pero la idea que tengo es usar un if/else donde el if compruebe si la función 
        finaliza donde debe finalizar haga un return True y de la misma con el else, si la función no acaba como debería
        hacer un return False
        """

    def get_current_state(self):
        """
        Returns the current state of the game.

        :return: The current state of the game.
        """
        return self.states[len(self.states)]

    def __repr__(self):
        """
        Returns a string with the internal representation of the game. This method can be used to represent the game
        information in a different format than the requested.

        :return: A string with the internal representation of the game.
        """

        #raise NotImplementedError()

    def __str__(self):
        """
        Returns a string with the representation of the current state of the game in the requested format.

        :return: A string with the representation of the current state of the game in the requested format
        """

        return self.states[len(self.states)-1]

    def fill_origin_tower(self, n_discs):
        """
        internal function that fill the origin tower with the number of discs that the user request
        :param tower: the object tower
        :param n_discs: the number of discs
        :return: the tower filled with discs
        """
        for i in range(n_discs, 0, -1):
            self.towers[0].push_disc(i)
            print()


