import java.util.Scanner;
public class Image{

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int NumOfCases = scan.nextInt();
        int[] Count= new int[31];

        Count[0] = 1;
        for (int i = 0; i < NumOfCases; i++){
            int x = scan.nextInt();
            

            Count[1] = 3;
            Count[2] = 8;

            for (int j = 3; j <= 20; j++) {
                Count[j] = 3 * Count[j - 1] - Count[j - 2];
            }
            
            System.out.println(Count[x]);
        }

        scan.close();
    }
}