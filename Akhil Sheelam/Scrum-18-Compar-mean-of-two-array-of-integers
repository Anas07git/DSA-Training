import java.util.Scanner;

public class CompareArraySums {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter elements of the first array (comma-separated): ");
        int[] arr1 = readArray(scanner);

        System.out.print("Enter elements of the second array (comma-separated): ");
        int[] arr2 = readArray(scanner);

        boolean sumsEqual = calculateSum(arr1) == calculateSum(arr2);
        System.out.println("Sums are equal: " + sumsEqual);

        scanner.close();
    }

    private static int[] readArray(Scanner scanner) {
        String[] input = scanner.nextLine().split(",");
        int[] arr = new int[input.length];
        for (int i = 0; i < input.length; i++) {
            arr[i] = Integer.parseInt(input[i].trim());
        }
        return arr;
    }

    private static int calculateSum(int[] arr) {
        int sum = 0;
        for (int num : arr) {
            sum += num;  // Sum all elements
        }
        return sum;  // Return total sum
    }
}
