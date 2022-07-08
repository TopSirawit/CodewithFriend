import java.util.Scanner;
public class TrinTrin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your score = ");
        int numberofsca = sc.nextInt();
        if (numberofsca >= 80){
            System.out.println("A");
        }else if (numberofsca >= 75){
            System.out.println("B+");
        }else if (numberofsca >= 70){
            System.out.println("B");
        }else if (numberofsca >= 65){
            System.out.println("C+");
        }else if (numberofsca >= 60){
            System.out.println("C");
        }else{
            System.out.println("F");
        }

    }
}
