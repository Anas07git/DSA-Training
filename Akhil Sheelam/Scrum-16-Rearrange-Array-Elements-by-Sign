import java.util.Arrays;
import java.util.Scanner;

public class RearrangeArray {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of elements (even number): ");
        int n = scanner.nextInt();
        int[] arr = new int[n];

        System.out.println("Enter the elements (positive and negative):");
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        int[] result = rearrange(arr);
        System.out.println("Rearranged array: " + Arrays.toString(result));
        
        scanner.close();
    }

    public static int[] rearrange(int[] arr) {
        int[] result = new int[arr.length];
        int posIndex = 0, negIndex = 1;

        for (int num : arr) {
            if (num >= 0) {
                result[posIndex] = num;
                posIndex += 2;
            } else {
                result[negIndex] = num;
                negIndex += 2;
            }
        }
        return result;
    }
}
