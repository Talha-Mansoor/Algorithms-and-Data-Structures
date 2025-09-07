import java.util.Scanner;
public class Minion{
    
    public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    int NumOfCases = scan.nextInt();
    int[] originalMoney = new int[31];
    
    originalMoney[0] = 0;
    for (int i = 0; i < NumOfCases; i++){
        int x = scan.nextInt();
        //Do not edit anything above
    
        //write the NSIDs of the members of your group here:
        //Talha Mansoor - kgy284 - 11346490
        //Write your code below

        //BEGIN
        if (0==originalMoney[1]) {
            for (int j = 1; j <= 30; j++) {
                originalMoney[j] = (1 << j) -1;
            }}
        //END

        //Do not edit anything below 
        System.out.println(originalMoney[x]);
    }
    
    scan.close();
    }
}