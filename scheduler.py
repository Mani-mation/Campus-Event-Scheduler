from typing import List, Dict
from event import Event


def build_conflict_graph(events: List[Event]) -> Dict[int, List[int]]:

    graph: Dict[int, List[int]] = {event.event_id: [] for event in events}

    for i in range(len(events)):
        for j in range(i + 1, len(events)):
            e1, e2 = events[i], events[j]
            if e1.overlaps_with(e2):
                graph[e1.event_id].append(e2.event_id)
                graph[e2.event_id].append(e1.event_id)

    return graph


def color_graph_greedy(events: List[Event], graph: Dict[int, List[int]]) -> Dict[int, int]:
    
    color_assignment: Dict[int, int] = {}

    for event in events:
        neighbor_colors = {
            color_assignment[neighbor_id]
            for neighbor_id in graph[event.event_id]
            if neighbor_id in color_assignment
        }

        room = 0
        while room in neighbor_colors:
            room += 1

        color_assignment[event.event_id] = room

    return color_assignment


def assign_rooms(events: List[Event]) -> None:
 
    graph = build_conflict_graph(events)
    color_assignment = color_graph_greedy(events, graph)

    for event in events:
        room_number = color_assignment[event.event_id]
        event.room = f"Room-{room_number + 1}"


def rooms_needed(events: List[Event]) -> int:
    return len({event.room for event in events})
