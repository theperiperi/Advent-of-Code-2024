def parse_input(filename):
    # Read and parse input file into number list
    with open(filename, "r") as data:
        return [int(line.strip()) for line in data]

def prune(number):
    # Prune number to stay within bounds
    return number % 16777216

def mix(num_a, num_b):
    # Mix two numbers using XOR
    return num_a ^ num_b

def gen_next_number(number):
    # Generate next number in sequence using mix and prune
    sixty_four = number * 64
    first_mix = mix(number, sixty_four)
    first_prune = prune(first_mix)

    thirty_two = first_prune//32
    second_mix = mix(first_prune, thirty_two)
    second_prune = prune(second_mix)

    twenty_forty_eight = second_prune*2048
    third_mix = mix(second_prune, twenty_forty_eight)
    return prune(third_mix)

def part2(number_list):
    # Calculate part 2 answer using sequence differences
    differences_dict = {}
    prices_list = []
    
    # Generate sequences
    for num in number_list:
        new_list = []
        new_list.append(num % 10)
        current = num
        for _ in range(2000):
            next_num = gen_next_number(current)
            new_list.append(next_num % 10)
            current = next_num
        prices_list.append(new_list)
    
    # Find patterns in differences
    for sequence in prices_list:
        current_sequence = []
        sequences_set = set()
        prev_num = sequence[0]
        
        for n in range(1, len(sequence)):
            next_num = sequence[n]
            difference = next_num - prev_num
            current_sequence.append(difference)
            prev_num = next_num
            
            if len(current_sequence) <= 3:
                continue
            elif len(current_sequence) >= 5:
                current_sequence.pop(0)
                
            sequence_tuple = tuple(current_sequence)
            if sequence_tuple in sequences_set:
                continue
                
            sequences_set.add(sequence_tuple)
            if sequence_tuple in differences_dict:
                differences_dict[sequence_tuple] += next_num
            else:
                differences_dict[sequence_tuple] = next_num
    
    return max(differences_dict.values())

numbers = parse_input('day22/input.txt')
print(part2(numbers))
