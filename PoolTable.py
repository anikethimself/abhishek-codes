class PoolTable:
    def __init__(self):   # fixed constructor
        self.pool = []

    def add_literal(self, literal):
        if literal not in self.pool:
            self.pool.append(literal)
            print(f"Added literal: {literal}")
        else:
            print(f"Literal '{literal}' already exists.")

    def display(self):
        print("Current Pool Table:")
        for idx, literal in enumerate(self.pool):
            print(f"{idx} -> {literal}")


# Example Usage:
pool_table = PoolTable()
pool_table.add_literal("=5")
pool_table.add_literal("=10")
pool_table.display()
