""" This program computes the soccer league log table
"""
import sys
import pytest

class Team:
    """
    This is the class that will be used to create soccer team objects
    Instance Attributes:
        team_name (str) : The name of the football team
        total_points (int) : The amount of points team has
    """
    def __init__(self, team_name):
        """
        The constructor for the team class.
        Parameters:
        team_name (str): The name of the football team
        """
        self.team_name = team_name
        self.total_points = 0
        
    def team_win(self):
        """This functions computes the win scored
        """
        self.total_points = self.total_points +3
        
    def team_draw(self):
        """This functions computes the draw scored
        """
        self.total_points = self.total_points +1
 
def string_extraction(new_games):
    """This functions extracts the team names and scores from textfile
    """
    team_two_score = int(new_games[new_games.rfind(" ")+1:len(new_games)])
    team_two = new_games[new_games.rfind(",")+1: new_games.rfind(" ")].strip()
        
    new_games = new_games[0:new_games.rfind(",")]
        
    team_one_score = int(new_games[new_games.rfind(" ")+1:len(new_games)])
    team_one = new_games[0: new_games.rfind(" ")].strip()
    
    return team_one, team_one_score, team_two, team_two_score

def print_score(team_objects):
    """This functions returns the correct league board
    """
    rank1=1
    rank2=1
    current_points=-3
    league_output = ""
    
    for obj in team_objects:
        
        if obj.total_points == 1:
            ending_text = "pt"
        else:
            ending_text = "pts"
            
        if current_points != obj.total_points:
            rank2= rank1
            league_output = league_output+str(rank1)+". "+obj.team_name+", "+str(obj.total_points)+" "+ending_text+'\n'
        else:
            league_output = league_output+str(rank2)+". "+obj.team_name+", "+str(obj.total_points)+" "+ending_text+'\n'
            
        rank1+=1   
        current_points = obj.total_points
        
    print(league_output) #for running normally to see output
    return league_output # For the automated tests
 
def read_file(input_file):
    """This functions creates the list of teams and
     computes their total points
    """
    info = input_file.readlines()
    team_objects = []
    team_names = []
    
    for line in info:
        new_games = line.strip()
        team_one, team_one_score, team_two, team_two_score = string_extraction(new_games)
            
        if team_one not in team_names:
            team_objects.append(Team(team_one))
            team_names.append(team_one)
        if team_two not in team_names:
            team_objects.append(Team(team_two))
            team_names.append(team_two)
    
        if team_one_score == team_two_score:
            for obj in team_objects:
                if (obj.team_name == team_one or obj.team_name == team_two):
                    obj.team_draw()
        
        elif team_one_score > team_two_score:
            for obj in team_objects:
                if obj.team_name == team_one:
                    obj.team_win()
                    break       
        else:
            for obj in team_objects:
                if obj.team_name == team_two:
                    obj.team_win()
                    break

    team_objects.sort(key=lambda obj: (-obj.total_points, obj.team_name), reverse=False)
    return print_score(team_objects)
    
def main():
    """The main function that executes when running
    """
    try:
        user_input = sys.argv[1]
        with open(user_input) as input_file:
            read_file(input_file)
    except IndexError:
        pytest.main()
      
if __name__ == "__main__":
    main()
