"""This file is the script for the automated tests
"""
import main

def test_case_one():
    """This test checks for cases where each team has same points
    """
    user_input = "test_case_one.txt"
    with open(user_input) as input_file:
        val = main.read_file(input_file)
    
    assert val == '''1. Arsenal, 2 pts
1. Chelsea, 2 pts
1. Man United, 2 pts
'''
def test_case_two():
    """This test checks for cases where team names
        have multiple words and scores have high values
    """
    user_input = "test_case_two.txt"
    with open(user_input) as input_file:
        val = main.read_file(input_file)

    assert val == '''1. Barca, 6 pts
1. Manchester City, 6 pts
3. Bayern Munich Club, 3 pts
4. Dortmund, 0 pts
4. Valencia City, 0 pts
4. West Ham United, 0 pts
'''
def test_case_three():
    """This test checkshas multiple of the same games
    """
    user_input = "test_case_three.txt"
    with open(user_input) as input_file:
        val = main.read_file(input_file)
    
    assert val == '''1. Man United, 10 pts
2. Chelsea, 7 pts
3. Arsenal, 4 pts
'''
def test_case_four():
    """General multiple example test case
    """
    user_input = "test_case_four.txt"
    with open(user_input) as input_file:
        val = main.read_file(input_file)
    
    assert val == '''1. Tarantulas, 18 pts
2. Lions, 15 pts
3. FC Awesome, 3 pts
3. Snakes, 3 pts
5. Grouches, 0 pts
'''
def test_case_five():
    """Checking if the ps/pt is printing correct
    """
    user_input = "test_case_five.txt"
    with open(user_input) as input_file:
        val = main.read_file(input_file)
    
    assert val == '''1. Galectica, 4 pts
2. Bafana Bafana, 3 pts
2. Beets, 3 pts
4. Mexico, 1 pt
5. BattleStar, 0 pts
5. Bears, 0 pts
'''
    