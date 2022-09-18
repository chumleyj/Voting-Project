"""
Class: Vote
Description: This class contains an individual vote of ranked candidates, including what the most
    resent candidate returned is and their ranking in this individual vote.
Class Variables:
    lane_name: the name of the lane associated with the vote
    candidate_preference: a tuple of strings representing the names of candidates
        in order of the voters preference.
    last_voted: stores the last candidate that was returned by the get_vote function
    last_voted_rank: stores this vote's ranking of the last candidate returned by the get_vote function
"""
class Vote():

    """
    Function: init
    Description: initializes the object and member variables.
    Parameters:
        lane - default is None. If enetered, is passed to add_lane to store the lane name of the vote
        ranked_candidates - default is None. If entered, is passed to add_ranked_candidates to store
            as the candidate_preference
    """
    def __init__(self, *, lane=None, ranked_candidates=None):
        
        self.lane_name = None
        self.candidate_preference = None
        self.last_voted = ""
        self.last_voted_rank = None
        self.is_counted = None

        self.add_lane(lane)
        self.add_ranked_candidates(ranked_candidates)

    """
    Function: add_ranked_candidates
    Description: stores ranked_list as the candidate_preference if ranked_list is a list
    Parameters: 
        ranked_list - a list of candidates in order of preference for this individual vote
    """
    def add_ranked_candidates(self, ranked_list):

        if isinstance(ranked_list, list):
            self.candidate_preference = tuple(ranked_list)
        else:
            self.candidate_preference = []

    """
    Function: add_lane
    Description: adds a lane name to the vote
    Parameters: 
        lane_name - a string that is saved as the lane_name
    """
    def add_lane(self, lane_name):
        
        if isinstance(lane_name, str):
            self.lane_name = lane_name
        else:
            self.lane_name = "Unknown lane"

    """
    Function: get_vote
    Description: returns a dictionary with the first candidate from candidate preferences that is not in the
        excluded_candidates list and the ranking for that candidate 
    Parameters:
        excluded_candidates - a list of candidates that have been eliminated and cannot be voted for
    """
    def get_vote(self, excluded_candidates):

        vote = {"candidate": "No vote", "rank": 0}
        self.is_counted = False

        # Loop through candidate preference and get first candidate not in excluded candidate list
        for i in range(0, len(self.candidate_preference)):
            if self.candidate_preference[i] not in excluded_candidates:
                
                vote["candidate"] = self.candidate_preference[i]
                self.last_voted = self.candidate_preference[i]
                
                vote["rank"] = i + 1
                self.last_voted_rank = i + 1

                self.is_counted = True
                break
        
        return vote
    
    """
    Function: reset
    Description: resets all member variables to default state
    Parameters: N/A
    """
    def reset(self):
        self.lane_name = "Unknown lane"
        self.candidate_preference = []
        self.last_voted = ""
        self.last_voted_rank = None
    
    """
    Function: clear_last_vote
    Description: resets last_voted and last_voted_rank variables, but keeps lane_name and candidate_preference
    Parameters: N/A
    """
    def clear_last_vote(self):
        self.last_voted = ""
        self.last_voted_rank = None