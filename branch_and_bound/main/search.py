from branch_and_bound.main.utils import *
from branch_and_bound.graph_and_node.node import *
from branch_and_bound.graph_and_node.graph import *

def graph_search(problem, fringe):
    """Search through the successors of a problem to find a goal.
    The argument fringe should be an empty queue.
    If two paths reach a state, only use the best one. [Fig. 3.18]"""
    closed = {}
    numeroNodosExpandidos = 1
    numeroNodosVisitados = 1
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            print("Numero de nodos visitado:"+str(numeroNodosVisitados))
            print("Numero de nodos expandidos:"+str(numeroNodosExpandidos))
            return node
        if node.state not in closed:
            closed[node.state] = True
            fringe.extend(node.expand(problem))
            numeroNodosExpandidos+=len(node.expand(problem))
        numeroNodosVisitados+=1
    return None


def breadth_first_graph_search(problem):
    """Search the shallowest nodes in the search tree first. [p 74]"""
    return graph_search(problem, FIFOQueue())  # FIFOQueue -> fringe


def depth_first_graph_search(problem):
    """Search the deepest nodes in the search tree first. [p 74]"""
    return graph_search(problem, Stack())