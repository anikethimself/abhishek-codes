# Symbol Table Program in Python

class Symbol:
    def __init__(self, name, address):
        self.name = name
        self.address = address

def generate_symbol_table(code_lines):
    symbol_table = {}
    location_counter = 0

    for line in code_lines:
        parts = line.strip().split()

        if parts[0] == "START":
            location_counter = int(parts[1])

        elif parts[0] in ["DS", "DC"]:
            symbol_name = parts[0]
            size = int(parts[1]) if parts[0] == "DS" else 1
            symbol_table[symbol_name] = Symbol(symbol_name, location_counter)
            location_counter += size

        elif len(parts) >= 2 and parts[1] in ["DS", "DC"]:
            symbol_name = parts[0]
            size = int(parts[2]) if parts[1] == "DS" else 1
            symbol_table[symbol_name] = Symbol(symbol_name, location_counter)
            location_counter += size

        else:
            location_counter += 1

    return symbol_table


if __name__ == "__main__":
    # Sample input code
    code = [
        "START 100",
        "READ X",
        "ADD AREG, ='5'",
        "X DC 2",
        "Y DS 1",
        "Z EQU X",
        "END"
    ]

    symbols = generate_symbol_table(code)
    print("SYMBOL TABLE:")
    for sym in symbols.values():
        print(f"{sym.name} -> {sym.address}")
