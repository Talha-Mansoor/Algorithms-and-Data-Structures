/* Name: Talha Mansoor
NSID: kgy284
Student Number: 11346490
Assignment 2 CMPT 270-01
lab- T15
*/

import java.util.Scanner;
import java.util.Arrays;

/**
 * A2Q1: An incomplete VA Language interpreter
 */
public class a2q2
{

    /**
     * Implements the Va language interpreter in Basic Java.
     * @param HEAPSIZE: the number of doubles in the heap
     */
    public static void interpreter(int HEAPSIZE)
    {

        // the machine's memory model
        double register = 0.0;
        Boolean bregister=false;
        double[] heap = new double[HEAPSIZE];

        // variables for the command values
        String command;
        double value;
        int index;

        Scanner in = new Scanner(System.in);

        // the main interpreter loop
        do
        {
            // prompt for an input
            System.out.print(">> ");

            // read a command;
            command = in.next();

            if (command.equals("SET"))
            {
                // set register value
                register = in.nextDouble();
            } else if (command.equals("TELL"))
            {
                // print current register value
                System.out.println(register);
                System.out.println(bregister);
            } else if (command.equals("STORE"))
            {
                // move register value to heap
                index = in.nextInt();
                heap[index] = register;
            } else if (command.equals("ADD"))
            {
                // add passed in value to register value
                value = in.nextDouble();
                register += value;
            } else if (command.equals("SUB"))
            {
                // subtract passed in value from register value
                value = in.nextDouble();
                register -= value;
            } else if (command.equals("HALT"))
            {
                // Do nothing except avoid the catch-all case below
            } else if (command.equals("LOAD"))
            {
                // move heap value at index i to register
                index = in.nextInt();
                register=heap[index];
            } else if (command.equals("MUL"))
            {
                // multiply passed in value to register value
                value = in.nextDouble();
                register *= value;
            } else if (command.equals("DIV"))
            {
                // divide passed in value to register value
                value = in.nextDouble();
                register /= value;
            }else if (command.equals("ADDI"))
        {
            // add passed in index value in heap to register value
            index = in.nextInt();
            register +=heap[index];
        } else if (command.equals("SUBI"))
        {
            // SUBTRACT passed in index value in heap to register value
            index = in.nextInt();
            register -=heap[index];
        }else if (command.equals("MULI"))
        {
            // MULTIPLY passed in index value in heap to register value
            index = in.nextInt();
            register *=heap[index];
        }else if (command.equals("DIVI"))
        {
            // DIVIDE passed in index value in heap to register value
            index = in.nextInt();
            register /=heap[index];
        }else if (command.equals("STATE"))
        {
            //prints out following things
            System.out.println("REGISTER:"+register);
            System.out.println("Boolean REGISTER:"+bregister);
            System.out.println("heap[0]"+heap[0]);
            System.out.println("heap[1]"+heap[1]);
            System.out.println("heap[2]"+heap[2]);
            System.out.println("heap[3]"+heap[3]);
            System.out.println("heap[4]"+heap[4]);
        } else if(command.equals("LESS"))
            {
                value = in.nextDouble();
                bregister=register<value;
            }else if(command.equals("LESSEQ"))
            {
                value = in.nextDouble();
                bregister=register<=value;
            }else if(command.equals("EQUAL"))
            {
                value = in.nextDouble();
                bregister= register==value;
            }else if(command.equals("GREATEQ"))
            {
                value = in.nextDouble();
                bregister=register>=value;
            }else if(command.equals("GREAT"))
            {
                value = in.nextDouble();
                bregister=register>value;
            }


            else
            {
                String given = in.nextLine();
                System.out.println("Bad command: '" + command + given + "'");
                break;
            }
        } while (!command.equals("HALT"));
    }


    public static void main(String[] args)
    {
        // run the interpreter with a heap size of 5
        interpreter(5);


    }

}
