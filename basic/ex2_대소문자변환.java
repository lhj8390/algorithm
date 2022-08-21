import java.util.*;
public class ex2_대소문자변환 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        char[] inputArray = input.toCharArray();
        int index = 0;
        for (char ch : inputArray) {
            if (ch == Character.toLowerCase(ch))
                inputArray[index] = Character.toUpperCase(ch);
            else
                inputArray[index] = Character.toLowerCase(ch);
            index++;
        }

        System.out.println(inputArray);

        return;
    }
}
