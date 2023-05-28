## I Love Lance & Janice

The code performs a character substitution by inverting the positions of lowercase alphabets. Non-alphabetic characters remain unchanged.

Here's a breakdown of the code:

 - The input string `x` is iterated character by character using a for loop.
 - Each character c is checked if it falls within the range of lowercase alphabets `('a' to 'z')`.
 - If `c` is a lowercase alphabet, its position in the alphabet is calculated by subtracting the ASCII value of `'a'`.
 - The position is then inverted by subtracting it from 25 (the index of the last character in the alphabet).
 - The inverted position is added to the ASCII value of `'a'` to obtain the corresponding character.
 - If `c` is not a lowercase alphabet, it is added to the `final` list as is.
 - Finally, the characters in the `final` list are joined together using the `join()` method with an empty string as the separator and returned as the final result.
 - In the if `__name__ == "__main__":` block, there are two test cases:

 - `t1` is the string "wrw blf hvv ozhg mrtsg'h vkrhlwv?". The expected output is "did you see last night's episode?".
 - `t2` is the string "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!". The expected output is "Yeah! I can't believe Lance lost his job at the colony!!".
 - The output of the two test cases is printed using the print() function.

I hope this explanation helps you understand the code better. Let me know if you have any further questions!
