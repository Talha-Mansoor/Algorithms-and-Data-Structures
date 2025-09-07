import java.util.*;

public class Grid {
    static class Position {
        int row, col, moves;

        Position(int row, int col, int moves) {
            this.row = row;
            this.col = col;
            this.moves = moves;
        }
    }

    public static int minMovesToReachBottomRight(int[][] grid, int n, int m) {
        // Directions
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        // BFS Queue stores Position objs
        Queue<Position> queue = new LinkedList<>();
        queue.add(new Position(0, 0, 0));

        // track visited cells
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            Position current = queue.poll();
            int row = current.row;
            int col = current.col;
            int moves = current.moves;

            // If we reached the bottom-right corner, return the move count
            if (row == n - 1 && col == m - 1) {
                return moves;
            }

            // current jump val
            int jump = grid[row][col];

            // explore 4 possible directions
            for (int[] dir : directions) {
                int newRow = row + dir[0] * jump;
                int newCol = col + dir[1] * jump;

                // Check if the new position is within bounds and not visited
                if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < m && !visited[newRow][newCol]) {
                    visited[newRow][newCol] = true;
                    queue.add(new Position(newRow, newCol, moves + 1));
                }
            }
        }

        // If we exhaust the queue without reaching bot corner
        return -1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int[][] grid = new int[n][m];

        for (int i = 0; i < n; i++) {
            String line = scanner.next();
            for (int j = 0; j < m; j++) {
                grid[i][j] = line.charAt(j) - '0';
            }
        }

        int result = minMovesToReachBottomRight(grid, n, m);
        System.out.println(result);
    }
}
