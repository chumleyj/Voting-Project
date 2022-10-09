"""
Class: Candidate
Description: This class contains an individual candidate, including data on votes for them and 
    associated methods
Class Variables:
    candidate_name - the name of the candidate
    lane_name - the name of the candidate's lane
    total_votes - the total number of votes the candidate received in an election
    votes_by_round - the number of votes the candidate received in each round of an
        instant runoff.
"""
class Candidate():
    
    """
    Function: init
    Description: initializes the object and member variables.
    Parameters:
        name - a string with the candidates name
        lane - the name of the candidates lane
    """
    def __init__(self, name, *, lane=None):

        self.candidate_name = None
        self.lane_name = None
        self.total_votes = 0
        self.votes_by_round = {}

        self.set_lane(lane)

        # set the candidates name
        if isinstance(name, str):
            self.candidate_name = name
        else:
            self.candidate_name = input("Invalid candidate name. Re-enter: ")
    
    """
    Function: set_lane
    Description: adds a lane_name to the candidate
    Parameters:
        lane_name - a string that is saved as the lane_name
    """
    def set_lane(self, lane_name):

        if isinstance(lane_name, str):
            self.lane_name = lane_name
        else:
            self.lane_name = "Unknown lane"
    
    """
    Function: add_votes
    Description: adds votes to the total_vote tally and the runoff round associated with those votes
    Parameters:
    """
    def add_votes(self, vote_count, vote_round):

        self.total_votes += vote_count
        self.votes_by_round.update({vote_round: vote_count})
    
    """
    Function: clear_votes
    Description: resets the total_votes to 0 and votes_by_rank to an empty dictionary.
    Parameters: N/A
    """
    def clear_votes(self):

        self.total_votes = 0
        self.votes_by_round = {}