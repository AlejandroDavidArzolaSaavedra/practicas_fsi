from search import breadth_first_graph_search
from search import depth_first_graph_search
from search import branch_and_bound_With
from search import branch_and_bound_Without
from graph import UndirectedGraph
from gps_problem import GPSProblem
from  utils import Dict
import time, timeit

#########################
# Romania Graph
#########################

romania = UndirectedGraph(Dict(
    A=Dict(Z=75, S=140, T=118),
    B=Dict(U=85, P=101, G=90, F=211),
    C=Dict(D=120, R=146, P=138),
    D=Dict(M=75),
    E=Dict(H=86),
    F=Dict(S=99),
    H=Dict(U=98),
    I=Dict(V=92, N=87),
    L=Dict(T=111, M=70),
    O=Dict(Z=71, S=151),
    P=Dict(R=97),
    R=Dict(S=80),
    U=Dict(V=142)))

romania.locations = Dict(
    A=(91, 492), B=(400, 327), C=(253, 288), D=(165, 299),
    E=(562, 293), F=(305, 449), G=(375, 270), H=(534, 350),
    I=(473, 506), L=(165, 379), M=(168, 339), N=(406, 537),
    O=(131, 571), P=(320, 368), R=(233, 410), S=(207, 457),
    T=(94, 410), U=(456, 350), V=(509, 444), Z=(108, 531))

australia = UndirectedGraph(Dict(
    T=Dict(),
    SA=Dict(WA=1, NT=1, Q=1, NSW=1, V=1),
    NT=Dict(WA=1, Q=1),
    NSW=Dict(Q=1, V=1)))
australia.locations = Dict(WA=(120, 24), NT=(135, 20), SA=(135, 30),
                           Q=(145, 20), NSW=(145, 32), T=(145, 42), V=(145, 37))

#########################
# TODO: Implementar Ramificación y Acotación (Branch and Bound)
# Crear una funcion similar al  BFS y DFS y adaptarla para implementar la lógica de Ramificación y Acotación.
# Recuerdar que hay que medir el tiempo de ejecución y contar el número de nodos expandidos y visitados.
#########################

#########################
# TODO: Realizar test de comprobación
# Ejecutar los algoritmos de búsqueda (BFS, DFS, Branch and Bound) para diferentes problemas y comparar los resultados.
# Asegúrarsee de que los resultados son lógicos y consistentes con las expectativas.
#########################

# Caminos de las ciudades de Romania
node_pairs = [('A', 'B'), ('O', 'E'), ('G', 'Z'), ('N', 'D'), ('M', 'F')]
num_executions = 100 

for start_node, goal_node in node_pairs:
    gps_ubications = GPSProblem(start_node, goal_node, romania)

    # Calcular tiempo para BFS
    start_time = time.time_ns()
    timeit.timeit(lambda: breadth_first_graph_search(gps_ubications), number=num_executions) / num_executions
    end_time = time.time_ns()
    duration_bfs = (end_time - start_time) / 1_000_000
    duration_bfs = round(duration_bfs, 3)
    numeroNodosVisitados = 0
    bfs_path = breadth_first_graph_search(gps_ubications)[0].path()
    nodosVisitadosBFS = (breadth_first_graph_search(gps_ubications)[1])
    nodosExpandidosBFS = (breadth_first_graph_search(gps_ubications)[2])

    # Calcular tiempo para DFS
    start_time = time.time_ns()
    timeit.timeit(lambda: depth_first_graph_search(gps_ubications), number=num_executions) / num_executions
    end_time = time.time_ns()
    duration_dfs = (end_time - start_time) / 1_000_000
    duration_dfs = round(duration_dfs, 3)
    dfs_path = depth_first_graph_search(gps_ubications)[0].path()
    nodosVisitadosDFS = (depth_first_graph_search(gps_ubications)[1])
    nodosExpandidosDFS = (depth_first_graph_search(gps_ubications)[2])
    costdfs=(depth_first_graph_search(gps_ubications)[3])
    costbfs=(breadth_first_graph_search(gps_ubications)[3])
    # Imprimir resultados
    print(f"Path from {start_node} to {goal_node} (BFS): {bfs_path}")
    print(f"BFS Duration: {duration_bfs} microseconds")
    print(f"BFS nodos expandidos: {nodosExpandidosBFS}")
    print(f"BFS nodos visitados: {nodosVisitadosBFS}")
    print(f"Coste : {costbfs}")

    print(f"Path from {start_node} to {goal_node} (DFS): {dfs_path}")
    print(f"DFS Duration: {duration_dfs} microseconds")
    print(f"DFS nodos expandidos: {nodosExpandidosDFS}")
    print(f"DFS nodos visitados: {nodosVisitadosDFS}")
    print(f"Coste : {costdfs}")
    print()


     # Calcular tiempo para DFS
    start_time = time.time_ns()
    timeit.timeit(lambda:branch_and_bound_With(gps_ubications), number=num_executions) / num_executions
    end_time = time.time_ns()
    duration_bbw = (end_time - start_time) / 1_000_000
    duration_bbw = round(duration_dfs, 3)
    bbw_path = branch_and_bound_With(gps_ubications)[0].path()
    nodosVisitadosbbw = (branch_and_bound_With(gps_ubications)[1])
    nodosExpandidosbbw = (branch_and_bound_With(gps_ubications)[2])
    costbbw=(branch_and_bound_With(gps_ubications)[3])
    print(f"Path from {start_node} to {goal_node} (Branch_and_bound_With): {bbw_path}")
    print(f"Branch_and_bound_With Duration: {duration_bbw} microseconds")
    print(f"Branch_and_bound_With nodos expandidos: {nodosExpandidosbbw}")
    print(f"Branch_and_bound_With nodos visitados: {nodosVisitadosbbw}")
    print(f"Coste : {costbbw}")
    print()


    start_time = time.time_ns()
    timeit.timeit(lambda:branch_and_bound_Without(gps_ubications), number=num_executions) / num_executions
    end_time = time.time_ns()
    duration_bbw = (end_time - start_time) / 1_000_000
    duration_bbw = round(duration_dfs, 3)
    bbw_path = branch_and_bound_Without(gps_ubications)[0].path()
    nodosVisitadosbbw = (branch_and_bound_Without(gps_ubications)[1])
    nodosExpandidosbbw = (branch_and_bound_Without(gps_ubications)[2])
    costbbw=(branch_and_bound_Without(gps_ubications)[3])

    print(f"Path from {start_node} to {goal_node} (Branch_and_bound_Without): {bbw_path}")
    print(f"Branch_and_bound_Without Duration: {duration_bbw} microseconds")
    print(f"Branch_and_bound_Without nodos expandidos: {nodosExpandidosbbw}")
    print(f"Branch_and_bound_Without nodos visitados: {nodosVisitadosbbw}")
    print(f"Coste : {costbbw}")
    print()



# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
