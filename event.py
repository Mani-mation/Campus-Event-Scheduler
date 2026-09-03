from dataclasses import dataclass


@dataclass
class Event:
    event_id: int
    name: str
    club: str
    start: int
    end: int
    room: str = None      
    def overlaps_with(self, other: "Event") -> bool:
        return self.start < other.end and other.start < self.end

    def __str__(self):
        room_str = self.room if self.room else "UNASSIGNED"
        return f"[{self.event_id}] {self.name} ({self.club}) | {self.start}:00-{self.end}:00 | Room: {room_str}"
