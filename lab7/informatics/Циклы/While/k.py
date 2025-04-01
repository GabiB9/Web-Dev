from collections import deque

A = int(input())
B = int(input())
N = int(input())

def bfs(A, B, N):
    visited = set()
    queue = deque([(0, 0, [])])
    
    while queue:
        a, b, path = queue.popleft()
        
        if a == N or b == N:
            return path
        
        if (a, b) in visited:
            continue
        
        visited.add((a, b))
        
        # Выполнение команд
        next_states = [
            (A, b, path + [">A"]), # наполнить сосуд A
            (a, B, path + [">B"]), # наполнить сосуд B
            (0, b, path + ["A>"]), # вылить сосуд A
            (a, 0, path + ["B>"]), # вылить сосуд B
            (0, a + b, path + ["A>B"]), # перелить из A в B
            (a + b, 0, path + ["B>A"]), # перелить из B в A
        ]
        
        for state in next_states:
            if 0 <= state[0] <= A and 0 <= state[1] <= B:
                queue.append(state)
    
    return "Impossible"

result = bfs(A, B, N)
if result == "Impossible":
    print(result)
else:
    for command in result:
        print(command)
