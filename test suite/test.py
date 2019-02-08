from hanoi.tower import Tower
from hanoi.state import State
from hanoi.hanoi import HanoiGame
from hanoi.hanoi_exception import HanoiException


def negative_disc_input():

    #       TEST NUMBER 1 -- OK
    try:
        hanoiGame = HanoiGame(-1)
        assert (False)

    except HanoiException:
        pass


def check_wrong_finished_game():
    #       TEST NUMBER 2 -- OK

    hanoi_game = HanoiGame(3)
    hanoi_game.move(0, 2)
    hanoi_game.move(0, 1)
    assert (hanoi_game.is_finished() is False)


def check_wrong_movement():
    #       TEST NUMBER 3 -- OK

    hanoi_game = HanoiGame(3)
    try:
        hanoi_game.move(2, 1)
        assert (False)

    except HanoiException:
        pass


def check_wrong_tower_init():

    #       TEST NUMBER 4 -- OK

    # Something is really wrong if this test is not working
    tower = Tower()
    assert (tower.is_empty() == True)


def check_push_pop_tower():
    #       TEST NUMBER 5 -- OK

    tower = Tower()
    tower.push_disc(2)
    assert (tower.pop_disc() == 2)
    assert (tower.is_empty() == True)


def check_total_states(discs=10):
    #       TEST NUMBER 6 -- OK

    # Initial state plus 2^n - 1 states with moves
    hanoi_game = HanoiGame(discs)
    assert (hanoi_game.get_n_states() == 1024)


def retrieve_tower_from_state():
    #       TEST NUMBER 7 -- OK

    # You need to be able to retrieve the state of a tower in a state, to see the number of elements that are there
    hanoi_game = HanoiGame(3)
    state = hanoi_game.get_state(5)

    assert (sum(1 for element in state.get_tower(1) if element != 0) == 1)
    assert (sum(1 for element in state.get_tower(0) if element != 0) == 1)
    assert (sum(1 for element in state.get_tower(2) if element != 0) == 1)


def check_pop_from_empty_tower():
    #       TEST NUMBER 8 -- OK

    tower = Tower()
    try:
        tower.pop_disc()
        assert (False)

    except HanoiException:
        pass


def check_pushed_discs():
    #       TEST NUMBER 9 -- OK

    tower = Tower()
    tower.push_disc(3)
    assert (tower.pop_disc() == 3)


def check_output():
    #       TEST NUMBER 10 -- OK

    # Note that we are accessing the first state. No moves have been done yet, So no header or last move line needs to be present
    expected = """
....#|#.... .....|..... .....|..... 
...##|##... .....|..... .....|..... 
..###|###.. .....|..... .....|..... 
.####|####. .....|..... .....|..... 
#####|##### .....|..... .....|..... 
  Tower 1     Tower 2     Tower 3   
"""

    hanoi_game = HanoiGame(5)
    state = hanoi_game.get_state(0)
    assert (expected == str(state))


def show_standard_optimal_state():
    #       TEST NUMBER 11

    # Show a standard state from the optimal solution
    expected = """
Move id 7 Rec Depth 3
Last move: 1 Disk, from 1 to 3
...|... ...|... ..#|#.. 
...|... ...|... .##|##. 
...|... ...|... ###|### 
Tower 1 Tower 2 Tower 3 
"""
    hanoi_game = HanoiGame(3)
    state = hanoi_game.get_state(7)
    assert (expected == str(state))


def show_current_playing():
    #       TEST NUMBER 12

    # Show the current state, when playing manually
    hanoi_game = HanoiGame(3)
    hanoi_game.move(0, 2)
    hanoi_game.move(0, 1)

    state = hanoi_game.get_current_state()

    expected = """
...|... ...|... ...|... 
...|... ...|... ...|... 
###|### .##|##. ..#|#.. 
Tower 1 Tower 2 Tower 3 
"""
    assert (expected == str(state))


if __name__ == '__main__':


    negative_disc_input()
    check_wrong_finished_game()
    check_wrong_movement()
    check_wrong_tower_init()
    check_push_pop_tower()
    check_total_states(10)
    retrieve_tower_from_state()
    check_pop_from_empty_tower()
    check_pushed_discs()
    check_output()
    show_standard_optimal_state()
    

    show_current_playing()


