from __future__ import annotations
from typing import Dict, List, Tuple, Any
import heapq

Graph = Dict[str, Dict[str, float]]
Path = List[str]

class PriorityQueue:
    def __init__(self) -> None:
        self._heap: List[Tuple[float, int, Any]] = []
        self._i = 0

    def push(self, priority: float, item: Any) -> None:
        self._i += 1
        heapq.heappush(self._heap, (priority, self._i, item))

    def pop(self) -> Any:
        return heapq.heappop(self._heap)[-1]

    def __len__(self) -> int:
        return len(self._heap)

def reconstruct_path(came_from: Dict[str, str], current: str) -> Path:
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def path_cost(graph: Graph, path: Path) -> float:
    if not path or len(path) == 1:
        return 0.0
    cost = 0.0
    for u, v in zip(path, path[1:]):
        cost += float(graph[u][v])
    return cost
