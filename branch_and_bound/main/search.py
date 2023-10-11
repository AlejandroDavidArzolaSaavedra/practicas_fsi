from branch_and_bound.main.utils import *
from branch_and_bound.graph_and_node.node import *
from branch_and_bound.graph_and_node.graph import *

def graph_search(problem, fringe):
    """ The argument fringe should be an empty queue.
    If two paths reach a state, only use the best one. [Fig. 3.18]"""
    closed = {}
    global numeroNodosVisitados
    global numeroNodosExpandidos
    numeroNodosExpandidos = 1
    numeroNodosVisitados = 1
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node
        if node.state not in closed:
            closed[node.state] = True
            fringe.extend(node.expand(problem))
            numeroNodosExpandidos+=len(node.expand(problem))
        numeroNodosVisitados+=1
    return None


def breadth_first_graph_search(problem):
    return graph_search(problem, FIFOQueue()),numeroNodosVisitados, numeroNodosExpandidos


def depth_first_graph_search(problem):
    return graph_search(problem, Stack()),numeroNodosVisitados, numeroNodosExpandidos