from collections import deque

commands = [input() for _ in range(int(input()))]
stack = deque()

for command in commands:
    command_split = command.split()

    match command_split[0]:
        case 'push':
            stack.append(int(command_split[1]))
        case 'pop':
            if len(stack) == 0: print(-1)
            else: print(stack.popleft())
        case 'size':
            print(len(stack))
        case 'empty':
            print(1 if len(stack) == 0 else 0)
        case 'front':
            if len(stack) == 0: print(-1)
            else: print(stack[0])
        case 'back':
            if len(stack) == 0: print(-1)
            else: print(stack[-1])