# Author: Karla Castro
# Student ID: 20745522
# Email: kmcastro
# Date: 2023-11-29
# Description: This file has the DodgeballManager class that handles the main functionalities

from list.array_list import ArrayList
from dodgeball_player import DodgeballPlayer, name_map, score_map


class DodgeballManager:
    """ DodgeballManager
    A class to handle the main functionality of a one-sided Dodgeball game
    """


    def __init__(self, throwers : [str], dodgers : [str]):
        """ Constructor

        throwers: a Python list of thrower names (strings)
        dodgers: a Python list of dodger names (strings)
        """
        self._throwerList = ArrayList()
        self._dodgerList = ArrayList()
        self._benchList = ArrayList()

        # Check if the throwers & dodgers lists are empty
        if throwers == None or dodgers == None:
            # Raise a ValueError if it is
            raise ValueError("throwers and dodgers lists cannot be empty")
        # Check if the throwers & dodgers lists are empty
        if len(throwers) == 0 or len(dodgers) == 0:
            # Raise a ValueError if it is
            raise ValueError("throwers and dodgers lists cannot be empty")

        # Create and append players in respective lists
        for thrower in throwers:
            # Append throwers
            self._throwerList.append(DodgeballPlayer(thrower))
        for dodger in dodgers:
            # Append dodgers
            self._dodgerList.append(DodgeballPlayer(dodger))


	###########################
	#    Boolean Accessors    #
	###########################
    def isThrower(self, name : str) -> bool:
        """ Returns True if a player named name is a thrower. """
        # Returns true if any of the names in throwerList is equal to name
        return any(name_map(self._throwerList.get(player)) == name for player in range(self._throwerList.length()))
    
    def isActiveDodger(self, name : str) -> bool:
        """ Returns True if a player named name is an active dodger. """
        # Returns true if any of the names in dodgerList is equal to name
        return any(name_map(self._dodgerList.get(player)) == name for player in range(self._dodgerList.length()))

    def isBenchedPlayer(self, name : str) -> bool:
        """ Returns True if a player named name is a benched dodger. """
        # Returns true if any of the names in benchList is equal to name
        return any(name_map(self._benchList.get(player)) == name for player in range(self._benchList.length()))


	#########################
	#    Count Accessors    #
	#########################


    def nBenchedPlayers(self) -> int:
        """Returns the number of benched players."""
        # Returns the length of benchList
        return self._benchList.length()

    def nActiveDodgers(self) -> int:
        """Returns the number of active dodgers."""
        # Returns the length of dodgerList
        return self._dodgerList.length()


	####################
	#    Main Logic    #
	####################

    def dodge(self, throwerName : str, dodgerName : str):
        """ dodge
            Conducts the main logic for a dodged throw.

            throwerName: the name of the thrower
            dodgerName: the name of the successful dodger
        """
        # Check if the thrower and dodger names are empty
        if throwerName is None or dodgerName is None:
            # Raise a ValueError if they are
            raise ValueError("throwerName and dodgerName cannot be empty")
        # Check if the throwerName is an active thrower
        if self.isThrower(throwerName):
            # Check if the dodgerName is an active dodger
            if self.isActiveDodger(dodgerName):
               # Find the dodger using the index of the dodgerName
                name_dodger = self._dodgerList.get(self._dodgerList.find_index_byvalue(dodgerName, lambda x : x.get_name()))
                # Increment the score of the dodger
                name_dodger.increment_score()
            else:
                # Raise a ValueError if the dodgerName is not an active dodger
                raise ValueError(f"{dodgerName} is not an active dodger")
        else:
            # Raise a ValueError if the throwerName is not a thrower
            raise ValueError(f"{throwerName} is not an active thrower")
        

    def hit(self, throwerName : str, dodgerName : str):
        """ hit
            Conducts the main logic for a successful throw.

            throwerName: the name of the successful thrower
            dodgerName: the name of the hit dodger
        """
        # Check if the thrower and dodger names are empty
        if throwerName is None or dodgerName is None:
            # Raise a ValueError if they are
            raise ValueError("throwerName and dodgerName cannot be empty")
        # Check if the throwerName is an active thrower
        if self.isThrower(throwerName):
            # Check if the dodgerName is an active dodger
            if self.isActiveDodger(dodgerName):
                # Find the dodger using the index of the dodgerName
                name_dodger = self._dodgerList.get(self._dodgerList.find_index_byvalue(dodgerName, lambda x : x.get_name()))
                # Find the thrower using the index of the throwerName
                name_thrower = self._throwerList.get(self._throwerList.find_index_byvalue(throwerName, lambda x : x.get_name()))
                # Increment the score of the thrower
                name_thrower.increment_score()
                # Remove the dodger from the dodgerList
                self._dodgerList.remove(self._dodgerList.find_index_byvalue(name_dodger))
                # Append the dodger to the benchList
                self._benchList.append(name_dodger)
            else:
                raise ValueError(f"{dodgerName} is not an active dodger")
        else:
            raise ValueError(f"{throwerName} is not an active thrower")

    def catchBall(self, throwerName : str, dodgerName : str, benchBackName : str = None):
        """ catchBall
            Conducts the main logic for a caught ball,
            which brings a player back from the bench.

            throwerName: the name of the thrower
            dodgerName: the name of the dodger who caught the ball
            benchBackName: the optional name of the dodger who caught the ball
        """
        # Check if the names are empty
        if throwerName is None or dodgerName is None:
            # Raise a ValueError if they are
            raise ValueError("throwerName and dodgerName cannot be empty")
        
        # Check if the thrower is a thrower
        if self.isThrower(throwerName):
            # Check if the dodger is an active dodger
            if self.isActiveDodger(dodgerName):
                # Check if the there is any other player in the bench
                if benchBackName is None:
                    # Find the dodger using the index of the dodgerName
                    name_dodger = self._dodgerList.get(self._dodgerList.find_index_byvalue(dodgerName, lambda x : x.get_name()))
                    # Increment the score of the dodger
                    name_dodger.increment_score()
                else:
                    # Check if the benchBackName is a benched player
                    if self.isBenchedPlayer(benchBackName):
                        # Find the dodger using the index of the dodgerName
                        name_dodger = self._dodgerList.get(self._dodgerList.find_index_byvalue(dodgerName, lambda x : x.get_name()))
                        # Find the bench player using the index of the benchBackName
                        name_bench = self._benchList.get(self._benchList.find_index_byvalue(benchBackName, lambda x : x.get_name()))
                        # Increment the score of the thrower
                        name_dodger.increment_score()
                        # Insert bench player to the dodgerList a position after the dodger index
                        self._dodgerList.insert(self._dodgerList.find_index_byvalue(name_dodger)+2, name_bench)
                        # Remove the bench player from the benchList
                        self._benchList.remove(self._benchList.find_index_byvalue(name_bench))
                    else:
                        # Raise a ValueError if the benchBackName is not a benched player
                        raise ValueError(f"{benchBackName} is not a benched player")
            else:
                # Raise a ValueError if the dodger is not an active dodger
                raise ValueError(f"{dodgerName} is not an active dodger")
        else:
            raise ValueError(f"{throwerName} is not an active thrower")

	#######################
	#    Main Printing    #
	#######################

    def printThrowers(self):
        """Prints the throwers to stdout."""
        # Loop through the throwerList and print each player and their score
        for thrower in range(self._throwerList.length()):
            if thrower < self._throwerList.length()-1:
                print(f'{self._throwerList.get(thrower).__str__()}', end=",")
            else:

                print(f'{self._throwerList.get(thrower).__str__()}')

    def printDodgers(self):
        """Prints the dodgers to stdout."""
        # Loop through the dodgerList and print each player and their score
        for dodger in range(self._dodgerList.length()):
            if dodger < self._dodgerList.length()-1:
                print(f'{self._dodgerList.get(dodger).__str__()}', end=",")
            else:
                print(f'{self._dodgerList.get(dodger).__str__()}')

    def printBench(self):
        """Prints the benched players to stdout."""
        # Loop through the benchList and print each player and their score
        for benched in range(self._benchList.length()):
            if benched < self._benchList.length()-1:
                print(f'{self._benchList.get(benched).__str__()}', end=",")
            else:
                print(f'{self._benchList.get(benched).__str__()}')



	##########################
	#    Complex Printing    #
	##########################
    
    def printMVP(self):
        """Prints out the MVP(s) like a standard list (with scores)."""
        # Define sorted array
        sorted_array = self.printSortedScores()
        # Define MVP's
        print(f'{sorted_array.get(0).__str__()}', end=",")

        for player in range(0, sorted_array.length()-1):
            # Check if the player's score is not equal to the first player's score
            if sorted_array._A[player+1].get_score() == sorted_array._A[0].get_score():
                # Print the player's name and score
                if player < sorted_array.length()-2:
                    print(f'{sorted_array.get(player+1).__str__()}', end=",")
                else:
                    print(f'{sorted_array.get(player+1).__str__()}')

    def printSortedScores(self):
        """Prints out the sorted scores from highest to lowest, one on each line."""
        # Sort players by scores
        # self._dodgerList.sort(map_to_key=lambda x : x.get_score(), descending=True)
        # self._throwerList.sort(map_to_key=lambda x : x.get_score(), descending=True)
        # self._benchList.sort(map_to_key=lambda x : x.get_score(), descending=True)
        # Define sorted array
        sorted_list = ArrayList()
        # Append players (throwers, dodgers, benched) to sorted array
        for thrower in range(self._throwerList.length()):
            sorted_list.append(self._throwerList._A[thrower])
        for dodger in range(self._dodgerList.length()):
            sorted_list.append(self._dodgerList._A[dodger])
        for bench in range(self._benchList.length()):
            sorted_list.append(self._benchList._A[bench])
        # Sort sorted array
        sorted_list.sort(map_to_key=lambda x : x.get_score(), descending=True)
        # Print sorted array
        for player in range(sorted_list.length()):
            # Check if the player is not the last player
            if player < sorted_list.length()-1:
                print(f'{sorted_list.get(player).__str__()}', end=",")
                print()
            # Check if the player is the last player
            else:
                print(f'{sorted_list.get(player).__str__()}')
                print()
        return sorted_list


# Test cases
# dm_typical_modifed = DodgeballManager(
#             ["A", "B", "C"],
#             ["D", "E", "F"])
# dm_typical_modifed.catchBall("A", "D")
# dm_typical_modifed.hit("A", "D")
# dm_typical_modifed.catchBall("A", "E")
# dm_typical_modifed.hit("B", "E")
# dm_typical_modifed.catchBall("A", "F")
# dm_typical_modifed.hit("C", "F")
# #dm_typical_modifed.printSortedScores()
# dm_typical_modifed.printMVP()