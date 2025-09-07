/* Name: Talha Mansoor
NSID: kgy284
Student Number: 11346490
Assignment 2 CMPT 270-01
lab- T15
*/

import java.util.Scanner;
import java.util.Arrays;
import java.util.StringTokenizer;

public class a2q3
{

    public static void dislay_squares(int[][] arr)
            //displays the arrays in console
    {
        for (int[] row : arr)

            // converting each row as string
            // and then printing in a separate line
            System.out.println(Arrays.toString(row));
    }
    public static Boolean check(int[][] arr) {
        //checks array with final goal
        int[][] fin = {{1, 1, 1},
                {2, 2, 2},
                {3, 3, 3}};

        return Arrays.deepEquals(arr, fin);

    }


    public static Boolean Left(int[][] arr,char x,int y,Boolean c)
    {
        //Left rotation. Makes ccopy. Checks block and executes
        int x00=arr[0][0];
        int x01=arr[0][1];
        int x02=arr[0][2];
        int x10=arr[1][0];
        int x11=arr[1][1];
        int x12=arr[1][2];
        int x20=arr[2][0];
        int x21=arr[2][1];
        int x22=arr[2][2];

        if (y == 0){
        arr[0][0] = x01;
        arr[0][1] = x11;
        arr[1][0] = x00;
        arr[1][1] = x10;


    } else if (y==1) {
            arr[0][1] = x02;
            arr[0][2] = x12;
            arr[1][1] = x01;
            arr[1][2] = x11;
        }else if (y==2) {
            arr[1][0] = x11;
            arr[1][1] = x21;
            arr[2][0] = x10;
            arr[2][1] = x20;
        }else if (y==3) {
            arr[1][1] = x12;
            arr[1][2] = x22;
            arr[2][1] = x11;
            arr[2][2] = x21;
        }

        dislay_squares(arr);
        System.out.println(check(arr));
        return check(arr);
    }


    public static Boolean Right(int[][] arr,char x,int y,Boolean c){
        //Right rotation. Makes copy. Checks block and executes
        int x00=arr[0][0];
        int x01=arr[0][1];
        int x02=arr[0][2];
        int x10=arr[1][0];
        int x11=arr[1][1];
        int x12=arr[1][2];
        int x20=arr[2][0];
        int x21=arr[2][1];
        int x22=arr[2][2];

        if (y == 0) {
            arr[0][0] = x10;
            arr[0][1] = x00;
            arr[1][0] = x11;
            arr[1][1] = x01;
        } else if (y==1) {
            arr[0][1] = x11;
            arr[0][2] = x01;
            arr[1][1] = x12;
            arr[1][2] = x02;
        }else if (y==2) {
            arr[1][0] = x20;
            arr[1][1] = x10;
            arr[2][0] = x21;
            arr[2][1] = x11;
        }else if (y==3) {
            arr[1][1] = x21;
            arr[1][2] = x11;
            arr[2][1] = x22;
            arr[2][2] = x12;
        }

        dislay_squares(arr);
        System.out.println(check(arr));
        return check(arr);
    }



    public static void main(String[] args)
    {
        //origianl array displayued
        int[][] A1 = {   { 1, 2, 1 },
                         { 1, 3, 2},
                         {3,3,2} };

        dislay_squares(A1);
        Boolean check_var=false;
        //while loop keeps going until correct goal

        while (check_var== false) {

            Scanner myObj = new Scanner(System.in);

            System.out.println("Enter rotation (L/R): ");

            // String input

            char RL = myObj.nextLine().charAt(0);
            System.out.println("Enter block (0/1/2/3): ");
            // Numerical input
            int block = myObj.nextInt();
            System.out.println("rotation: " + RL);
            System.out.println("Block: " + block);
            if (RL =='L') {
               Boolean x= Left(A1, RL, block,check_var);
                if (x==true)
                {

                    System.out.println("CONGRATS U WON!!");
                    break;
                }
            }else if (RL =='R'){
                Boolean x=Right(A1, RL, block, check_var);
                if (x==true)
                {

                    System.out.println("CONGRATS U WON!!");
                    break;
                }
            }
            else{
                System.out.println("TRY AGAIN INCOrrect input");
            }
        }


    }

}
