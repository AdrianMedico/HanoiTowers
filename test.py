from hanoi.tower import Tower
from hanoi.state import State
from hanoi.hanoi import HanoiGame

if __name__ == '__main__':
    """
    towers = [Tower(), Tower(), Tower()]

    towers[0].discs.append(4)

    n_discs = 4

    state1 = State(1,1,1,2,3,towers, n_discs)
    state1.towers = towers
    result = state1.__str__()
    """

    hanoi = HanoiGame(3)
    hanoi.print_optimal_solution()
    #print(hanoi.__str__())
