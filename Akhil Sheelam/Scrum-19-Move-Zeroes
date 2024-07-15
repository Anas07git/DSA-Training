import java.util.Arrays;
import java.util.Scanner;

public class MoveZeroes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter elements of the array (comma-separated): ");
        
        String input = scanner.nextLine();
        int[] nums = Arrays.stream(input.split(","))
                           .mapToInt(Integer::parseInt)
                           .toArray();

        moveZeroes(nums);
        System.out.println("Modified array: " + Arrays.toString(nums));
        scanner.close();
    }

    private static void moveZeroes(int[] nums) {
        int lastNonZeroIndex = 0;

        for (int num : nums) {
            if (num != 0) nums[lastNonZeroIndex++] = num;
        }

        while (lastNonZeroIndex < nums.length) nums[lastNonZeroIndex++] = 0;
    }
}
