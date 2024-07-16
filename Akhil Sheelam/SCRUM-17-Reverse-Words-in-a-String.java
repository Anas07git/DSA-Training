public class ReverseWords {
    public static void main(String[] args) {
        String input = "I joined as a intern in synclovis"; // Example input
        String output = reverseWords(input);
        System.out.println("Output: \"" + output + "\"");
    }

    public static String reverseWords(String s) {
        String[] words = s.split(" "); // Split by spaces
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < words.length; i++) {
            String reversedWord = new StringBuilder(words[i]).reverse().toString();
            result.append(reversedWord);
            if (i < words.length - 1) {
                result.append(" "); // Add space only between words
            }
        }

        return result.toString(); // Return the final result
    }
}
