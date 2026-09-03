# Campus Event Scheduler

A lightweight Python application designed to schedule college club events and assign venue rooms with zero time conflicts. 

The project models "minimum room scheduling" as a classic **Graph Coloring Problem**, reducing event overlapping checks to graph adjacency list construction and applying a greedy graph coloring algorithm to assign rooms efficiently.

## Key Features

**Conflict Detection:** Identifies overlapping event times using half-open interval checking `[start, end)`. Back-to-back events (e.g., 9–11 and 11–13) are correctly processed without false conflict flags.
**Graph-Based Room Assignment:** Constructs a time-conflict graph and applies greedy coloring to allocate the minimum number of rooms needed.
**Interactive & Demo Modes:** Includes a scripted CLI demo for quick execution and an interactive command-line interface with input validation for custom scheduling.
**Comprehensive Unit Testing:** Includes test coverage for edge cases, graph symmetry, and room reuse optimization .

## Technical Overview

1. **Modeling Events:** Events are stored as instances of the `Event` dataclass containing tracking details, time ranges, and room assignment states[cite: 1].
2. **Conflict Graph Construction:** Compares pairs of events to generate an adjacency list where an edge represents an overlapping time slot .
3. **Greedy Graph Coloring:** Iterates through events and assigns the lowest available room index (`Room-1`, `Room-2`, etc.) not used by any adjacent conflicting neighbors .

## Project Structure
 event.py          # Event dataclass and time-overlap detection logic
 scheduler.py      # Core scheduling engine (conflict graph & room assignment)
 main.py           # Application entry point (Demo & Interactive modes)
 test_scheduler.py # Unit tests covering edge cases and scheduling rules
