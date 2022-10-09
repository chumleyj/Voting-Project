"""
Class: Lane
Description: This class contains a lane, including a lane name and probabilities
    reflecting the likely ranking for a vote from this lane
Class Variables:
    name - the name of the lane
"""
class Lane():

    """
    Function: init
    Description: initializes the object and member variables.
    Parameters:
        name - a string with the lane's name
    """
    def __init__(self, name):
        
        self.name = name
        self.probabilities = None

    """
    Function: set_probabilities
    Description: sets probabilities for each candidate for use when generating votes
        from voters in this lane
    Parameters:
        candidate_list - a list of candidate names
    """
    def set_probabilities(self, candidate_list):
        
        self.probabilities = []

        for candidate in candidate_list:
            
            print(f"What {candidate}")



"""
    Function: set_lanes
    Description: prompts the user for the number of lanes in the election
        and returns that number
"""
def set_lanes():

    num_lanes = None
    lane_names = []

    while num_lanes == None:

        # continue prompting until valid number input         
        num_lanes = input("How many lanes are there?: ")
        num_lanes = try_parse_int(num_lanes)
    
    # prompt for a name for each lane
    for i in range(0, num_lanes):

        lane_names.append(input(f"What is the name of lane {i + 1}?: "))

    return (num_lanes, lane_names)

"""
    Function: try_parse_int
    Description: checks that s is an integer and returns it if it is.
        Otherwise returns None
    Parameters:
        s - value to check whether is an integer
        base - base value for the integer (defaults to 10)
        val - value returned (None) if s is not an integer
"""
def try_parse_int(s, base=10, val=None):
    try:
        return int(s, base)
    except ValueError:
        print("Input is not a valid number.")
        return val