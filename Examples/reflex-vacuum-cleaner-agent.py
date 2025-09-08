# Reflex Vacuum Cleaner Agent

# Design a reflex vacuum agent that operates in a 4-room environment (A, B, C, D).

# Requirements:
# 1. Each room can be Clean or Dirty randomly at the start.
# 2. The agent perceives its current location and the room’s status.
# 3. The agent follows a simple reflex policy:
#   If the current room is Dirty, Suck.
#   else, move according to a predefined path:
#       A → B → D → C → A …
# 4. Simulate the agent for a fixed number of steps and print its actions and perceptions.

import random

# -----------------------------
# Base Agent Class
# -----------------------------
class Agent:
    def __init__(self):
        # Placeholder program (will be defined in subclasses)
        def program(percept): 
            raise NotImplementedError
        self.program = program


# Room locations
loc_A, loc_B, loc_C, loc_D = 'A', 'B', 'C', 'D'


# -----------------------------
# Reflex Vacuum Agent
# -----------------------------
class ReflexVacuumAgent(Agent):
    def __init__(self):
        super().__init__()

        def program(percept):
            location, status = percept
            if status == 'Dirty':
                action = 'Suck'
            elif location == loc_A:
                action = 'Right'
            elif location == loc_B:
                action = 'Down'
            elif location == loc_D:
                action = 'Left'
            elif location == loc_C:
                action = 'Up'

            print(f"Agent perceives {percept} and does {action}")
            return action

        self.program = program


# -----------------------------
# Vacuum Environment
# -----------------------------
class VacuumEnvironment:
    def __init__(self):
        # Randomly assign clean/dirty status to each room
        self.status = {
            loc_A: random.choice(['Clean', 'Dirty']),
            loc_B: random.choice(['Clean', 'Dirty']),
            loc_C: random.choice(['Clean', 'Dirty']),
            loc_D: random.choice(['Clean', 'Dirty'])
        }

    def add_object(self, agent, location=None):
        agent.location = location or self.default_location(agent)

    def default_location(self, agent):
        return random.choice([loc_A, loc_B, loc_C, loc_D])

    def percept(self, agent):
        return (agent.location, self.status[agent.location])

    def execute_action(self, agent, action):
        if action == 'Right':
            agent.location = loc_B
        elif action == 'Down':
            agent.location = loc_D
        elif action == 'Left':
            agent.location = loc_C
        elif action == 'Up':
            agent.location = loc_A
        elif action == 'Suck':
            self.status[agent.location] = 'Clean'


# -----------------------------
# Simulation
# -----------------------------
agent = ReflexVacuumAgent()
env = VacuumEnvironment()
env.add_object(agent)

print("Initial room status:", env.status)
print()

# Run the simulation for 10 steps
for step in range(10):
    percept = env.percept(agent)
    action = agent.program(percept)
    env.execute_action(agent, action)
    print("Room status:", env.status)
    print()
