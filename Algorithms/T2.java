//Talha Mansoor
//kgy284
//11346490
//CMPT360
import java.util.*;

public class T {
    static class Point {
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "(" + x + "," + y + ")";
        }
    }

    static class Triangle {
        Point p1, p2, p3;

        Triangle(Point p1, Point p2, Point p3) {
            this.p1 = p1;
            this.p2 = p2;
            this.p3 = p3;
        }

        @Override
        public String toString() {
            return p1 + "," + p2 + "," + p3;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input tree array T
        System.out.print("Enter the tree array T (comma-separated, e.g., 1,1,1,0,0,...): ");
        String[] tInput = scanner.nextLine().split(",");
        int[] T = new int[tInput.length];
        for (int i = 0; i < tInput.length; i++) {
            T[i] = Integer.parseInt(tInput[i].trim());
        }

        // Input root triangle coordinates
        System.out.print("Enter the coordinates for the root triangle (format: x1,y1 x2,y2 x3,y3): ");
        String[] coords = scanner.nextLine().split(" ");
        Point p1 = parsePoint(coords[0]);
        Point p2 = parsePoint(coords[1]);
        Point p3 = parsePoint(coords[2]);
        Triangle root = new Triangle(p1, p2, p3);

        Map<Integer, Triangle> result = new HashMap<>();
        if (assignTriangles(T, 0, root, result)) {
            for (int i = 0; i < T.length; i++) {
                if (T[i] == 0) {
                    System.out.println(i + " 0");
                } else {
                    System.out.println(i + " " + result.get(i));
                }
            }
        } else {
            System.out.println("None");
        }
    }

    static Point parsePoint(String coord) {
        String[] xy = coord.split(",");
        return new Point(Integer.parseInt(xy[0].trim()), Integer.parseInt(xy[1].trim()));
    }

    static boolean assignTriangles(int[] T, int index, Triangle current, Map<Integer, Triangle> result) {
        if (index >= T.length || T[index] == 0) {
            return true;
        }

        result.put(index, current);

        // Calculate adjusted centroid to avoid collinearity
        Point centroid = new Point(
                (current.p1.x + current.p2.x + current.p3.x) / 3,
                (current.p1.y + current.p2.y + current.p3.y) / 3
        );

        // Slightly perturb centroid to ensure non-collinearity
        centroid.x += (centroid.x == current.p1.x && centroid.x == current.p2.x) ? 1 : 0;
        centroid.y += (centroid.y == current.p1.y && centroid.y == current.p2.y) ? 1 : 0;

        // Create the three child triangles using centroid to ensure correct partitioning
        Triangle child1 = new Triangle(current.p1, current.p2, centroid);
        Triangle child2 = new Triangle(current.p2, current.p3, centroid);
        Triangle child3 = new Triangle(current.p3, current.p1, centroid);

        // Recursively assign triangles to children
        if (!assignTriangles(T, 3 * index + 1, child1, result)) {
            return false;
        }
        if (!assignTriangles(T, 3 * index + 2, child2, result)) {
            return false;
        }
        if (!assignTriangles(T, 3 * index + 3, child3, result)) {
            return false;
        }

        return true;
    }
}




/*
Test
Enter the tree array T (comma-separated, e.g., 1,1,1,0,0,...): 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0
Enter the coordinates for the root triangle (format: x1,y1 x2,y2 x3,y3): 6,8 0,0 12,0
0 (6,8),(0,0),(12,0)
1 (6,8),(0,0),(6,2)
2 (0,0),(12,0),(6,2)
3 (12,0),(6,8),(6,2)
4 (6,8),(0,0),(4,3)
5 (0,0),(6,2),(4,3)
6 (6,2),(6,8),(4,3)
7 (0,0),(12,0),(6,1)
8 (12,0),(6,2),(6,1)
9 (6,2),(0,0),(6,1)
10 0
11 0
12 0
*/
