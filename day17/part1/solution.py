def parse_input(filename):
    # Read and parse input file into program instructions
    with open(filename) as fname:
        lines = fname.readlines()
        initial_a = int(lines[0].split(": ")[1])
        initial_b = int(lines[1].split(": ")[1])
        initial_c = int(lines[2].split(": ")[1])
        program = [int(x) for x in lines[4].split(": ")[1].split(",")]
        return initial_a, initial_b, initial_c, program

def part1(initial_a, initial_b, initial_c, program):
    # Solve part 1: Run program with given initial values
    # Returns comma-separated string of outputs
    
    # Registers
    A = initial_a
    B = initial_b
    C = initial_c
    
    # Program Counter
    ip = 0
    
    # Output storage
    output = []
    
    def combo_value(operand):
        # Helper function to get the value of a combo operand
        if operand in range(4):  # Literal values 0-3
            return operand
        elif operand == 4:  # Value of register A
            return A
        elif operand == 5:  # Value of register B
            return B
        elif operand == 6:  # Value of register C
            return C
        else:
            raise ValueError("Invalid operand: 7 encountered")
    
    # Execute the program
    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]
        
        if opcode == 0:  # adv: A = A // (2 ** combo_value)
            A = A // (2 ** combo_value(operand))
        elif opcode == 1:  # bxl: B = B ^ operand
            B = B ^ operand
        elif opcode == 2:  # bst: B = combo_value % 8
            B = combo_value(operand) % 8
        elif opcode == 3:  # jnz: if A != 0, jump to operand
            if A != 0:
                ip = operand
                continue
        elif opcode == 4:  # bxc: B = B ^ C
            B = B ^ C
        elif opcode == 5:  # out: output combo_value % 8
            output.append(combo_value(operand) % 8)
        elif opcode == 6:  # bdv: B = A // (2 ** combo_value)
            B = A // (2 ** combo_value(operand))
        elif opcode == 7:  # cdv: C = A // (2 ** combo_value)
            C = A // (2 ** combo_value(operand))
        else:
            raise ValueError(f"Invalid opcode: {opcode}")
        
        ip += 2
    
    return ",".join(map(str, output))

initial_a, initial_b, initial_c, program = parse_input('day17/input.txt')
print(part1(initial_a, initial_b, initial_c, program))

