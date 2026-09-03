from event import Event
from scheduler import build_conflict_graph, assign_rooms, rooms_needed


def print_section(title: str):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def get_demo_events():
    return [
        Event(1,"Robotics Demo Day","Robotics Club",9,11),
        Event(2,"Coding Contest Finals","Coding Club",10,12),
        Event(3,"Dance Rehearsal","Dance Society",9,10),
        Event(4,"Photography Workshop","Photo Club",13,15),
        Event(5,"Debate Finals","Debate Society",14,16),
        Event(6,"Music Jam Session","Music Club",13,14),
        Event(7,"Chess Tournament", "Chess Club",9,12),
    ]


def collect_events_interactively():
    events = []
    next_id = 1

    print("Enter event requests one at a time. Type 'done' as the event name when finished.\n")

    while True:
        name = input(f"[Event {next_id}] Event name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        if not name:
            print("  Event name can't be empty. Try again.")
            continue

        club = input("  Club/organizer name: ").strip()
        if not club:
            club = "Unknown Club"

        start = _prompt_for_hour("  Start time (enter hour, e.g. 9 for 9:00): ")
        end = _prompt_for_hour("  End time (enter hour, e.g. 11 for 11:00): ")

        while end <= start:
            print("  End time must be after start time. Please re-enter the end time.")
            end = _prompt_for_hour("  End time (enter hour, e.g. 11 for 11:00): ")

        events.append(Event(next_id, name, club, start, end))
        next_id += 1
        print(f"  Added: {name} ({club}) {start}:00-{end}:00\n")

    return events


def _prompt_for_hour(prompt_text: str) -> int:
    while True:
        raw = input(prompt_text).strip()
        try:
            return int(raw)
        except ValueError:
            print("  Please enter a whole number (e.g. 9, 13, 17).")


def run_scheduler(events):
    if not events:
        print("\nNo events submitted - nothing to schedule.")
        return

    print_section("SUBMITTED EVENT REQUESTS")
    for e in events:
        print(e)

    graph = build_conflict_graph(events)
    print_section("DETECTED TIME CONFLICTS")
    for event in events:
        conflicts = graph[event.event_id]
        if conflicts:
            conflict_names = [e.name for e in events if e.event_id in conflicts]
            print(f"Event {event.event_id} ({event.name}) conflicts with: {conflict_names}")
        else:
            print(f"Event {event.event_id} ({event.name}) has no time conflicts")

    assign_rooms(events)

    print_section("FINAL CONFLICT-FREE SCHEDULE")
    for e in events:
        print(e)

    print_section("SUMMARY")
    print(f"Total events scheduled: {len(events)}")
    print(f"Minimum rooms used: {rooms_needed(events)}")


def main():
    print_section("CAMPUS EVENT SCHEDULER")
    print("1. Run scripted demo (sample events)")
    print("2. Submit event requests interactively")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "2":
        events = collect_events_interactively()
    else:
        events = get_demo_events()

    run_scheduler(events)


if __name__ == "__main__":
    main()
