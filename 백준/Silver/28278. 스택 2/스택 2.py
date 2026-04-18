from collections import deque

commands = [input() for _ in range(int(input()))]
stack = deque()

for command in commands:
    command_split = command.split()

    match command_split[0]:
        case '1':
            stack.append(int(command_split[1]))
        case '2':
            if len(stack) == 0: print(-1)
            else: print(stack.pop())
        case '3':
            print(len(stack))
        case '4':
            print(1 if len(stack) == 0 else 0)
        case '5':
            if len(stack) == 0: print(-1)
            else: print(stack[-1])