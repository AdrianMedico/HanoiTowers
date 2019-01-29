#from .hanoi_exception import HanoiException


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
        return self.discs.pop()

    '''
        Inserta un disco encima de la torre.
    '''
    def push_disc(self, disc):
        """
        Adds a dis to the top of the tower.
        Raises an HanoiException if the disc is bigger that the disc at the top of the tower.

        :param disc: The disc to be added to the top of the tower.
        """
        if self.discs[len(self.discs)] < disc:
            raise HanoiException("The disc is bigger than the current top disc")
        else:
            self.discs.append(disc)

    def as_list(self):
        """
        Returns the discs of the tower as a new list (it means that if the internal representation of the tower is a
        list, it should return a copy of it).

        :return: A list containing the discs of the tower.
        """
        return self.discs

    def __repr__(self):
        """
        Returns a string with the internal representation of the tower. This method can be used to represent the tower
        information in a different format than the requested.

        :return: A string with the internal representation of the state.
        """

        tower_representation = ""
        for item in self.discs:
            tower_representation += self.disc_as_string(item)
        return tower_representation

    def __str__(self):
        """
        Returns a string with the representation of the state in the requested format.

        :return: A string with the representation of the state in the requested format
        """
        relleno_puntos = 1
        duplicar_almohadillas = 2
        torre_prn = ""
        print(T1)
        puntos = (int(n_discs) * duplicar_almohadillas) + relleno_puntos  #
        for torre in range(n_discs):  # Recorremos la tabla T1

            linea_prn = ""  # Inicializamos la variable liena de impresión
            for T in T1:  # Bucle para dibujar las torres
                almohadilla = (int(T[torre]) * duplicar_almohadillas) + 1  #
                dibuja_disco = "|".center(almohadilla, "#").center(puntos, ".")  # Dibuja la torre con o sin discos
                linea_prn = linea_prn + "  " + dibuja_disco + "  "  # Concatena una linea de cada torre para ser impresa en pantalla
                print(linea_prn)

            for i in range(3):
                torre_prn = torre_prn + "  " + ("Torre" + str(i + 1)).center(puntos) + "  "
            print(torre_prn)

               
        return str(self.discs)

    def disc_as_string(self, size):
        disc = ''
        if size > 0:
            for j in range(size) * 2:
                disc += '#'
                if j == size:
                    disc += '|'
            disc += '\n'
        else:
            disc = "...|...\n"

