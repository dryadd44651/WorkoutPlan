class WorkoutPlan:
    def __init__(self, exercises, cycles):
        self.exercises = exercises
        self.cycles = cycles

    def generate_plan(self):
        plan = []
        for cycle in range(self.cycles):
            cycle_plan = []
            for rep in range(3):
                for exercise in self.exercises:
                    base_weight = exercise['initial_weight'] + (exercise['weight_increase_cycle'] * cycle)
                    weight = base_weight + (exercise['weight_increase_item'] * rep)
                    reps = [10, 8, 5][rep]
                    cycle_plan.append(f"{exercise['name']:<15}{rep + 1}: {weight:<4} X {reps}")
            plan.append(cycle_plan)
        return plan

    def display_plan(self):
        plan = self.generate_plan()
        for cycle_num, cycle in enumerate(plan):
            print(f"-- Cycle {cycle_num + 1} --")
            for item in cycle:
                print(item)
            print()

def read_exercises_from_file(filename):
    exercises = []
    cycles = 1
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            if line.startswith('cycles='):
                cycles = int(line.split('=')[1])
            else:
                name, initial_weight, weight_increase_item, weight_increase_cycle = line.split(',')
                exercises.append({
                    'name': name,
                    'initial_weight': float(initial_weight),
                    'weight_increase_item': float(weight_increase_item),
                    'weight_increase_cycle': float(weight_increase_cycle)
                })
    return exercises, cycles

# Example Usage
input_file = 'input.txt'
exercises, cycles = read_exercises_from_file(input_file)

workout_plan = WorkoutPlan(exercises, cycles)
workout_plan.display_plan()
