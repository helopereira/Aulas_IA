from __future__ import annotations
from typing import Callable, Dict, Set
from utils import PriorityQueue, reconstruct_path, path_cost, Graph

def greedy_best_first_search(graph: Graph, start: str, goal: str, h: Dict[str, float] | Callable[[str], float]):
    if isinstance(h, dict):
        def h_fn(n: str) -> float: return float(h.get(n, float("inf")))
    else:
        h_fn = h

    frontier = PriorityQueue()
    frontier.push(h_fn(start), start)
    came_from: Dict[str, str] = {}
    visited: Set[str] = set()
    explored_order = []

    while frontier:
        current = frontier.pop()
        explored_order.append(current)

        if current == goal:
            path = reconstruct_path(came_from, current)
            return path, explored_order, path_cost(graph, path)

        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph.get(current, {}):
            if neighbor not in visited:
                frontier.push(h_fn(neighbor), neighbor)
                if neighbor not in came_from:
                    came_from[neighbor] = current

    return None, explored_order, None
