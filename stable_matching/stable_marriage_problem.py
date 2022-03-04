# ----------
# The Gale–Shapley algorithm finds a stable matching between two equally sized sets of elements given an ordering of preferences for each element.
# https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm
# ----------

class Proposor:
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
        self.engaged_to = False
        
    def propose(self):
        return self.preferences.pop(0)
        
class Acceptor:
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
        self.engaged_to = False
        
    def is_better_proposor(self, new_proposor):
        if self.engaged_to == False:
            return True
        else:
            current_proposor = self.engaged_to
            current_proposor_index = self.preferences.index(current_proposor.name)
            new_proposor_index = self.preferences.index(new_proposor.name)
            if new_proposor_index < current_proposor_index:                
                current_proposor.engaged_to = False    # break current engagement
                return True
            else:
                return False             

def stable_matching(proposors, acceptors):
    iterations = 0
    engaged = [False] * len(proposors)
    while not all(engaged):
        for p in proposors:
            if p.engaged_to == False:
                propose_to = p.propose()
                for a in acceptors:
                    if (a.name == propose_to) and (a.is_better_proposor(p)):
                        p.engaged_to = a
                        a.engaged_to = p
        
        # check who is engaged -> if all values are true loop stops
        for i, p in enumerate(proposors):
            if p.engaged_to == False:
                engaged[i] = False
            else:
                engaged[i] = True 
                
        iterations += 1
    
    print("Solution found in {} iterations:".format(iterations))   
    for p in proposors:    
        print("{} -> {}".format(p.name, p.engaged_to.name))


if __name__ == "__main__":
    proposors = [Proposor("V", ["A", "B", "C", "D", "E"]),
                 Proposor("W", ["B", "C", "D", "A", "E"]),
                 Proposor("X", ["C", "D", "A", "B", "E"]),
                 Proposor("Y", ["D", "A", "B", "C", "E"]),
                 Proposor("Z", ["A", "B", "C", "D", "E"])] 
           
    acceptors = [Acceptor("A", ["W", "X", "Y", "Z", "V"]),
                 Acceptor("B", ["X", "Y", "Z", "V", "W"]),
                 Acceptor("C", ["Y", "Z", "V", "W", "X"]),
                 Acceptor("D", ["Z", "V", "W", "X", "Y"]),
                 Acceptor("E", ["V", "W", "X", "Y", "Z"])]
    
    stable_matching(proposors, acceptors)