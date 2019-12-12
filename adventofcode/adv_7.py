from itertools import permutations

initial_list = [3,8,1001,8,10,8,105,1,0,0,21,46,55,68,89,110,191,272,353,434,99999,3,9,1002,9,3,9,1001,9,3,9,102,4,9,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,3,9,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,5,9,1002,9,2,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,101,3,9,9,102,3,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]
dupa = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

def intcode_computer(input_list, input_code_one, input_code_two, amp_list):
    n = 0
    param_mode_opcodes = [1, 2, 5 ,6, 7, 8]
    first_input_processed = False
    while input_list[n] != 99:
        opcode = int(str(input_list[n])[-2:])
        instruction = str(input_list[n])
        param1 = int(instruction[-3]) if len(instruction) > 2 else 0
        param2 = int(instruction[-4]) if len(instruction) > 3 else 0
        if opcode in param_mode_opcodes:
            param1_val = input_list[n+1] if param1 else input_list[input_list[n+1]]
            param2_val = input_list[n+2] if param2 else input_list[input_list[n+2]]
        if opcode == 1:
            temp = param1_val + param2_val
            input_list[input_list[n+3]] = temp
            n += 4
        elif opcode == 2:
            temp2 = param1_val * param2_val
            input_list[input_list[n+3]] = temp2
            n += 4
        elif opcode == 3:
            input_val = input_code_one if not first_input_processed else input_code_two
            input_list[input_list[n+1]] = input_val
            n += 2
            first_input_processed = True
        elif opcode == 4:
            exit_signal = input_list[input_list[n+1]]
            n += 2
            # print(exit_signal)
        elif opcode == 5:
            n = param2_val if param1_val else n + 3
        elif opcode == 6:
            n = param2_val if not param1_val else n + 3
        elif opcode == 7:
            input_list[input_list[n+3]] = 1 if param1_val < param2_val else 0
            n += 4
        elif opcode == 8:
            input_list[input_list[n+3]] = 1 if param1_val == param2_val else 0
            n += 4

    while amp_list:
        intcode_computer(input_list, amp_list.pop(), exit_signal, amp_list)
    
    # this should be moved to return
    all_thruster_signals.append(exit_signal)
    return exit_signal


all_amp_codes = [list(i) for i in permutations([0, 1, 2, 3, 4], 5)]
all_thruster_signals = []
for i, num in enumerate(all_amp_codes):
    initial_amp_code = num.pop()
    intcode_computer(initial_list, initial_amp_code, 0, num)
    
print(max(all_thruster_signals))