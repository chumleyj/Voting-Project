"""
Class: Voter
Description: 
Class Variables:
    candidate_preference: a tuple of strings representing the names of candidates
        in order of the voters preference.
"""

class Voter():
    
    """
    Function: init
    Description:
    Parameters:
    """
    def __init__(self, *, lane=None, ranked_candidates=None):
        
        self.lane_name = None
        self.candidate_preference = None

        self.add_lane(lane)
        self.add_ranked_candidates(ranked_candidates)

    """
    Function:
    Description:
    Parameters:
    """
    def add_ranked_candidates(self, ranked_list):

        if isinstance(ranked_list, list):
            self.candidate_preference = ranked_list
            #check every index is string
        else:
            self.candidate_preference = []

    """
    Function:
    Description:
    Parameters:
    """
    def add_lane(self, lane_name):
        
        if isinstance(lane_name, str):
            self.lane_name = lane_name
        else:
            self.lane_name = "Unknown lane"

    """
    Function:
    Description:
    Parameters:
    """
    def is_voting(self):
        if len(self.candidate_preference) > 0:
            return True
        else:
            return False

    """
    Function:
    Description:
    Parameters:
    """
    def get_vote(self, excluded_candidates):
        # return who voting for and their rank in this voter's preference, skip excluded candidates
        pass