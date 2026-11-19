class ExpertSystem:
    def __init__(self):
        self.facts = set()          # mga facts na alam na
        self.rules = []             # listahan ng mga IF-THEN rules

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def infer_forward(self):
        pass                        # hindi gagamitin sa lab na ito

    def infer_backward(self, goal, visited=None):
        if visited is None:
            visited = set()

        print(f"Checking goal: {goal}")

        if goal in visited:
            return False
        visited.add(goal)

        if goal in self.facts:
            print(f"'{goal}' is a known fact.")
            return True

        applicable_rules = []
        for rule in self.rules:
            if rule['consequent'] == goal:
                applicable_rules.append(rule)

        if not applicable_rules:
            print(f"'{goal}' is unknown. No rules conclude it.")
            return False

        for rule in applicable_rules:
            print(f"Attempting to prove rule: IF {', '.join(rule['antecedent'])} THEN {rule['consequent']}")
            all_antecedents_proven = True
            for condition in rule['antecedent']:
                if not self.infer_backward(condition, visited.copy()):
                    all_antecedents_proven = False
                    break

            if all_antecedents_proven:
                print(f"All conditions for '{goal}' are proven. Adding to facts.")
                self.add_fact(goal)
                return True

        print(f"Not all conditions for '{goal}' could be proven.")
        return False


if __name__ == "__main__":
    system = ExpertSystem()

    system.add_fact("has_fur")
    system.add_fact("gives_milk")
    system.add_fact("eats_meat")
    system.add_fact("has_tawny_color")
    system.add_fact("has_black_stripes")

    system.add_rule({"antecedent": ["has_fur", "gives_milk"], "consequent": "is_mammal"})
    system.add_rule({"antecedent": ["is_mammal", "eats_meat"], "consequent": "is_carnivore"})
    
    system.add_rule({"antecedent": ["has_fur", "eats_meat", "has_tawny_color", "has_dark_spots"], "consequent": "cheetah"})
    system.add_rule({"antecedent": ["has_fur", "eats_meat", "has_tawny_color", "has_black_stripes"], "consequent": "tiger"})
    system.add_rule({"antecedent": ["has_feathers", "can_fly", "lays_eggs"], "consequent": "bird"})


    system.add_rule({"antecedent": ["has_fur", "gives_milk"], "consequent": "is_mammal"})
    system.add_rule({"antecedent": ["is_mammal", "eats_meat"], "consequent": "is_carnivore"})

    goal = input("Enter the animal to identify (e.g., 'cheetah'): ")
    result = system.infer_backward(goal)
    print(f"\nConclusion: The hypothesis that it is a '{goal}' is {result}.")
    print(f"Final set of facts: {system.facts}")
