# Intermediate Code Program in Python

MOT = {
    "STOP": "(IS,00)",
    "ADD": "(IS,01)",
    "SUB": "(IS,02)",
    "MULT": "(IS,03)",
    "MOVER": "(IS,04)",
    "MOVEM": "(IS,05)",
    "COMP": "(IS,06)",
    "BC": "(IS,07)",
    "DIV": "(IS,08)",
    "READ": "(IS,09)",
    "PRINT": "(IS,10)"
}

REGISTERS = {
    "AREG": "(RG,01)",
    "BREG": "(RG,02)",
    "CREG": "(RG,03)",
    "DREG": "(RG,04)"
}


def generate_intermediate_code(code_lines):
    intermediate_code = []
    location_counter = 0

    for line in code_lines:
        parts = line.strip().replace(",", "").split()

        if parts[0] == "START":
            location_counter = int(parts[1])
            intermediate_code.append(f"(AD,01) (C,{location_counter})")

        elif parts[0] in MOT:
            inst = MOT[parts[0]]
            if len(parts) == 2:
                operand = parts[1]
                operand_code = REGISTERS.get(operand, operand)
                intermediate_code.append(f"{inst} {operand_code}")
            elif len(parts) == 3:
                reg = REGISTERS.get(parts[1], parts[1])
                operand = parts[2]
                operand_code = f"(C,{operand.strip('=')})" if operand.startswith("='") else operand
                intermediate_code.append(f"{inst} {reg} {operand_code}")
            else:
                intermediate_code.append(inst)

        elif parts[0] == "END":
            intermediate_code.append("(AD,02)")

        location_counter += 1

    return intermediate_code


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

    ic = generate_intermediate_code(code)
    print("INTERMEDIATE CODE:")
    for line in ic:
        print(line)
