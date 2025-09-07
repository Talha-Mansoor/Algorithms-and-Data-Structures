//Talha Mansoor
//kgy284
//11346490
//CMPT360

import java.util.*;
import java.util.Scanner;

public class T {
    static class Triangle {
        int[] x = new int[3];
        int[] y = new int[3];

        // constructor  init triangle
        Triangle(int[] x, int[] y) {
            System.arraycopy(x, 0, this.x, 0, 3);
            System.arraycopy(y, 0, this.y, 0, 3);
        }

        @Override
        public String toString() {
            return "(" + x[0] + "," + y[0] + "),(" + x[1] + "," + y[1] + "),(" + x[2] + "," + y[2] + ")";
        }
    }

    static List<String> results = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // ask input for tree array
        System.out.print("Enter the tree array T (comma-separated, e.g., 1,1,1,0,0,...): ");
        String[] input = scanner.nextLine().split(",");
        int[] T = new int[input.length];
        for (int i = 0; i < input.length; i++) {
            T[i] = Integer.parseInt(input[i].trim());
        }

        // ask input fore root triangle
        System.out.print("Enter the coordinates for the root triangle (format: x1,y1 x2,y2 x3,y3): ");
        String[] coordinates = scanner.nextLine().split(" ");
        int[] x = new int[3];
        int[] y = new int[3];
        for (int i = 0; i < 3; i++) {
            String[] point = coordinates[i].split(",");
            x[i] = Integer.parseInt(point[0].trim());
            y[i] = Integer.parseInt(point[1].trim());
        }
        Triangle rootTriangle = new Triangle(x, y);

        // solve problem using input tree and root triangle
        solve(T, rootTriangle);

        // print  result
        for (int i = 0; i < results.size(); i++) {
            System.out.println(i + " " + results.get(i));
        }
    }

    static void solve(int[] T, Triangle rootTriangle) {
        results.clear();
        if (T[0] == 1) {
            partition(T, 0, rootTriangle);
        }
    }

    static void partition(int[] T, int index, Triangle triangle) {
        if (index >= T.length || T[index] == 0) {
            results.add("0");
            return;
        }

        // add current triangle results list
        results.add(triangle.toString());

        // check if enough entries in T for children
        if (3 * index + 1 >= T.length) {
            return;
        }

        // create sub-triangles that partition current triangle
        Triangle[] children = new Triangle[3];
        int[] x = triangle.x;
        int[] y = triangle.y;

        // calculate points to create subtriangles so each subtriangle shares 1 side with the parent
        int midX01 = (x[0] + x[1]) / 2;
        int midY01 = (y[0] + y[1]) / 2;
        int midX12 = (x[1] + x[2]) / 2;
        int midY12 = (y[1] + y[2]) / 2;
        int midX20 = (x[2] + x[0]) / 2;
        int midY20 = (y[2] + y[0]) / 2;

        // first child (shares side btw points 0 & 1, and includes midpoint of side 2-0)
        children[0] = new Triangle(new int[]{x[0], midX01, midX20},
                new int[]{y[0], midY01, midY20});

        // second child (shares side btw pts 1 & 2, and includes midpoint of side 0-1)
        children[1] = new Triangle(new int[]{x[1], midX12, midX01},
                new int[]{y[1], midY12, midY01});

        // third child (shares side betw pts 2 & 0, and includes midpoint of side 1-2)
        children[2] = new Triangle(new int[]{x[2], midX20, midX12},
                new int[]{y[2], midY20, midY12});

        // recursively partition  children
        for (int i = 0; i < 3; i++) {
            if (3 * index + 1 + i < T.length && T[3 * index + 1 + i] == 1) {
                partition(T, 3 * index + 1 + i, children[i]);
            } else {
                results.add("0");
            }
        }
    }
}

/*
Test
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0
Enter the coordinates for the root triangle (format: x1,y1 x2,y2 x3,y3): 6,8 0,0 12,0
0 (6,8),(0,0),(12,0)
1 (6,8),(3,4),(9,4)
2 (6,8),(4,6),(7,6)
3 (3,4),(6,4),(4,6)
4 (9,4),(7,6),(6,4)
5 (0,0),(6,0),(3,4)
6 (0,0),(3,0),(1,2)
7 (6,0),(4,2),(3,0)
8 (3,4),(1,2),(4,2)
9 (12,0),(9,4),(6,0)
10 0
11 0
12 0
*/
