import collections

class MazeSolver:
    def __init__(self, maze):
        """
        Initializes the solver with a maze.
        0 = Path, 1 = Wall, S = Start, E = Exit
        """
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start = self._find_position("S")
        self.end = self._find_position("E")

    def _find_position(self, target):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.maze[r][c] == target:
                    return (r, c)
        return None

    def solve(self):
        """Finds the shortest path using Breadth-First Search (BFS)."""
        if not self.start or not self.end:
            return None

        # Queue stores (current_position, path_taken)
        queue = collections.deque([(self.start, [self.start])])
        visited = {self.start}

        while queue:
            (curr_r, curr_c), path = queue.popleft()

            # Check if we reached the exit
            if (curr_r, curr_c) == self.end:
                return path

            # Explore neighbors: Right, Down, Left, Up
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = curr_r + dr, curr_c + dc

                if (0 <= nr < self.rows and 0 <= nc < self.cols and 
                    self.maze[nr][nc] != 1 and (nr, nc) not in visited):
                    
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))

        return None

    def display_solution(self, path):
        """Prints the maze with the path marked by dots (.)."""
        if not path:
            print("No solution found.")
            return

        # Create a copy to modify for display
        display_maze = [row[:] for row in self.maze]
        for r, c in path:
            if display_maze[r][c] not in ("S", "E"):
                display_maze[r][c] = "."

        for row in display_maze:
            print(" ".join(str(cell) for cell in row))


if __name__ == "__main__":
    # Example Maze
    # 1 = Wall, 0 = Path, S = Start, E = End
    grid = [
        ["S", 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, "E"]
    ]

    solver = MazeSolver(grid)
    solution_path = solver.solve()

    print("--- Maze Solver ---")
    if solution_path:
        print(f"Path found! Length: {len(solution_path)} steps")
        print("Path Coordinates:", solution_path)
        print("\nVisual Solution ('.' is the path):")
        solver.display_solution(solution_path)
    else:
        print("No path exists for this maze.")
