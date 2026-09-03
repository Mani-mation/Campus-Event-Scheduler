import unittest
from event import Event
from scheduler import build_conflict_graph, color_graph_greedy, assign_rooms, rooms_needed


class TestOverlapDetection(unittest.TestCase):

    def test_full_overlap(self):
        e1 = Event(1, "A", "ClubA", 9, 12)
        e2 = Event(2, "B", "ClubB", 10, 11)
        self.assertTrue(e1.overlaps_with(e2))

    def test_partial_overlap(self):
        e1 = Event(1, "A", "ClubA", 9, 11)
        e2 = Event(2, "B", "ClubB", 10, 12)
        self.assertTrue(e1.overlaps_with(e2))

    def test_back_to_back_no_overlap(self):
        e1 = Event(1, "A", "ClubA", 9, 11)
        e2 = Event(2, "B", "ClubB", 11, 13)
        self.assertFalse(e1.overlaps_with(e2))

    def test_no_overlap_at_all(self):
        e1 = Event(1, "A", "ClubA", 9, 10)
        e2 = Event(2, "B", "ClubB", 14, 15)
        self.assertFalse(e1.overlaps_with(e2))

    def test_identical_time_slots(self):
        e1 = Event(1, "A", "ClubA", 9, 10)
        e2 = Event(2, "B", "ClubB", 9, 10)
        self.assertTrue(e1.overlaps_with(e2))


class TestConflictGraph(unittest.TestCase):
    def test_no_conflicts_graph_is_empty_adjacency(self):
        events = [
            Event(1, "A", "ClubA", 9, 10),
            Event(2, "B", "ClubB", 11, 12),
        ]
        graph = build_conflict_graph(events)
        self.assertEqual(graph[1], [])
        self.assertEqual(graph[2], [])

    def test_conflict_graph_is_symmetric(self):
        events = [
            Event(1, "A", "ClubA", 9, 11),
            Event(2, "B", "ClubB", 10, 12),
        ]
        graph = build_conflict_graph(events)
        self.assertIn(2, graph[1])
        self.assertIn(1, graph[2])


class TestGraphColoringRoomAssignment(unittest.TestCase):
    def test_two_conflicting_events_get_different_rooms(self):
        events = [
            Event(1, "A", "ClubA", 9, 11),
            Event(2, "B", "ClubB", 10, 12),
        ]
        assign_rooms(events)
        self.assertNotEqual(events[0].room, events[1].room)

    def test_non_conflicting_events_can_share_a_room(self):
        events = [
            Event(1, "A", "ClubA", 9, 10),
            Event(2, "B", "ClubB", 11, 12),
        ]
        assign_rooms(events)

        self.assertEqual(rooms_needed(events), 1)

    def test_three_mutually_conflicting_events_need_three_rooms(self):

        events = [
            Event(1, "A", "ClubA", 9, 11),
            Event(2, "B", "ClubB", 10, 12),
            Event(3, "C", "ClubC", 10, 11),
        ]
        assign_rooms(events)
        self.assertEqual(rooms_needed(events), 3)

    def test_every_event_gets_a_room_assigned(self):
        events = [
            Event(1, "A", "ClubA", 9, 10),
            Event(2, "B", "ClubB", 10, 11),
            Event(3, "C", "ClubC", 9, 11),
        ]
        assign_rooms(events)
        for e in events:
            self.assertIsNotNone(e.room)


if __name__ == "__main__":
    unittest.main()
