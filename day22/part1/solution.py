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

def part1(number_list):
    # Calculate part 1 answer using number sequences
    answer = 0
    prices_list = []
    
    for count, num in enumerate(number_list):
        new_list = []
        new_list.append(num % 10)
        current = num
        
        for _ in range(2000):
            next_num = gen_next_number(current)
            new_list.append(next_num % 10)
            current = next_num
        
        answer += next_num
        prices_list.append(new_list)
        if count % 100 == 6:
            print(count)
            
    return answer

numbers = parse_input('day22/input.txt')
print(part1(numbers))