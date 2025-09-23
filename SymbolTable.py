class SymbolTable:
    def __init__(self):  
        self.table = {}

    def insert(self, symbol, address):
        if symbol in self.table:
            print(f"Symbol '{symbol}' already exists.")
        else:
            self.table[symbol] = address
            print(f"Inserted: {symbol} -> {address}")

    def search(self, symbol):
        if symbol in self.table:
            print(f"Found: {symbol} -> {self.table[symbol]}")
        else:
            print(f"Symbol '{symbol}' not found.")

    def update(self, symbol, new_address):
        if symbol in self.table:
            self.table[symbol] = new_address
            print(f"Updated: {symbol} -> {new_address}")
        else:
            print(f"Symbol '{symbol}' not found to update.")

    def display(self):
        print("Current Symbol Table:")
        for symbol, address in self.table.items():
            print(f"{symbol} -> {address}")

sym_table = SymbolTable()
sym_table.insert("LOOP", 100)
sym_table.search("LOOP")
sym_table.update("LOOP", 105)
sym_table.display()
