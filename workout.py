class WorkoutPlan:
    def __init__(self, exercises):
        self.exercises = exercises

    def generate_plan(self, cycles):
        plan = []
        for cycle in range(cycles):
            cycle_plan = []
            for rep in range(4):
                for exercise in self.exercises:
                    base_weight = exercise['initial_weight'] + (exercise['weight_increase_cycle'] * cycle)
                    weight = base_weight + (exercise['weight_increase_item'] * rep)
                    reps = [12, 10, 8, 5][rep]
                    cycle_plan.append(f"{exercise['name']}{rep}: {weight} X{reps}")
            plan.append(cycle_plan)
        return plan

    def display_plan(self, cycles):
        plan = self.generate_plan(cycles)
        for cycle_num, cycle in enumerate(plan):
            print(f"-- Cycle {cycle_num + 1} --")
            for item in cycle:
                print(item)
            print()

# Example Usage
exercises = [
    {
        'name': 'bench press',
        'initial_weight': 50,
        'weight_increase_item': 5,
        'weight_increase_cycle': 2.5
    },
    {
        'name': 'squat',
        'initial_weight': 100,
        'weight_increase_item': 10,
        'weight_increase_cycle': 5
    },
    {
        'name': 'deadlift',
        'initial_weight': 150,
        'weight_increase_item': 10,
        'weight_increase_cycle': 5
    }
]

cycles = 3

workout_plan = WorkoutPlan(exercises)
workout_plan.display_plan(cycles)
