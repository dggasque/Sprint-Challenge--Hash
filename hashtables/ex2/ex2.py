#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    dic = {}
    route = []
    for ticket in tickets:
        dic[ticket.source] = ticket.destination
    
    cur = dic["NONE"]
    route.append(cur)
    while cur != "NONE":
       cur = dic[cur]
       route.append(cur) 

    return route
