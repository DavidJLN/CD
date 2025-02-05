import pytest
import src.minesweeper as minesweeper

def test_module_exists():
    assert minesweeper
    
def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    assert len(game.mines) == 2
    
def test_reveal():
    import random 
    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    game.reveal(2, 2)
    assert game.revealed == {(2, 2)}
    
def test_get_board():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    game.reveal(2, 2)
    assert game.get_board() == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', 4]]
    
def test_is_winner():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    assert game.is_winner() == False
    
def test_restart():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    game.reveal(0, 0)
    game.restart()
    assert game.revealed == set()
    
"""def test_fail():
    assert False"""