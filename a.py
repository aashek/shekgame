def get_next_input():
    return tuple(map(int, input().split()))

def hit(coords, grid, search_tile):
    return any(
        grid[i][j] != -1 and grid[i][j] != search_tile
        for i in range(coords[0] - 1, coords[0] + 2)
        for j in range(coords[1] - 1, coords[1] + 2)
        if 0 <= i <= 7 and 0 <= j <= 7
    )

grid = [[-1] * 8 for _ in range(8)]
p1 = True

while True:
    coords = get_next_input()

    if hit(coords, grid, 1 if p1 else 0):
        print(f"p{1 if p1 else 2} loses")
        break

    grid[coords[0]][coords[1]] = 1 if p1 else 0
    p1 = not p1
