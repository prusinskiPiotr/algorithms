import fileinput

reactions = [line.rstrip().split(' ') for line in fileinput.input()]

ore_instructions = [i[:2]+i[3:] for i in reactions if "ORE" in i]
base_instructions = [i[-1] for i in ore_instructions]
fuel_instructions = [i for i in reactions if "FUEL" in i][0]
other_instructions = [i for i in reactions if "ORE" not in i and "FUEL" not in i]
instruction_stack = fuel_instructions[:-3]
counter = 0
while instruction_stack:
    print(f"stack:{instruction_stack},counter:{counter}")
    counter += 1
    next_reaction = instruction_stack.pop()
    next_reaction_multiplier = instruction_stack.pop()
    print(next_reaction, next_reaction_multiplier)
    for i in other_instructions:
        if i[-1] == next_reaction:
            for j in range(0, len(i)-3, 2):
                instruction_stack.append(i[j])
                instruction_stack.append(i[j+1])
    
    # print(next_reaction, next_reaction_multiplier)




