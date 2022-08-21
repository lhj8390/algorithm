import java.util.*;
public class ex1_문자찾기 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String input1 = in.next().toLowerCase();
        char[] input1Array = input1.toCharArray();

        char input2 = in.next().toLowerCase().charAt(0);

        int size = 0;
        for(int i = 0; i < input1.length(); i++) {
            if (input1Array[i] == input2) {
                size++;
            }
        }
        System.out.println(size);
        return ;
    }
}
