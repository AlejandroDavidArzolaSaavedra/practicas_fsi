from utils import *
from node import *
from graph import *

def graph_search(problem, fringe):
    """ The argument fringe should be an empty queue.
    If two paths reach a state, only use the best one. [Fig. 3.18]"""
    closed = {}
    global numeroNodosVisitados
    global numeroNodosExpandidos
    global cost 
    cost = 0
    numeroNodosExpandidos = 1
    numeroNodosVisitados = 1
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            cost=node.path_cost
            return node
        if node.state not in closed:
            closed[node.state] = True
            fringe.extend(node.expand(problem))
            numeroNodosExpandidos+=len(node.expand(problem))
        numeroNodosVisitados+=1
    return None


def breadth_first_graph_search(problem):
    return graph_search(problem, FIFOQueue()),numeroNodosVisitados, numeroNodosExpandidos, cost


def depth_first_graph_search(problem):
    return graph_search(problem, Stack()),numeroNodosVisitados, numeroNodosExpandidos, cost


def branch_and_bound_With(problem):
    return graph_search(problem, Branch_and_Bound_With_Subestimation(problem)),numeroNodosVisitados, numeroNodosExpandidos, cost


def branch_and_bound_Without(problem):
    return graph_search(problem, Branch_and_Bound_Without_Subestimation()),numeroNodosVisitados, numeroNodosExpandidos, cost