from __future__ import annotations
from typing import Callable, Dict
from utils import PriorityQueue, reconstruct_path, Graph

def a_star_search(graph: Graph, start: str, goal: str, h: Dict[str, float] | Callable[[str], float]):
    if isinstance(h, dict):
        def h_fn(n: str) -> float: return float(h.get(n, float("inf")))
    else:
        h_fn = h

    frontier = PriorityQueue()
    frontier.push(h_fn(start), start)

    came_from: Dict[str, str] = {}
    g_score: Dict[str, float] = {start: 0.0}
    explored_order = []

    while frontier:
        current = frontier.pop()
        explored_order.append(current)

        if current == goal:
            path = reconstruct_path(came_from, current)
            return path, explored_order, g_score[current]

        for neighbor, step_cost in graph.get(current, {}).items():
            tentative_g = g_score[current] + float(step_cost)
            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + h_fn(neighbor)
                frontier.push(f, neighbor)

    return None, explored_order, None
