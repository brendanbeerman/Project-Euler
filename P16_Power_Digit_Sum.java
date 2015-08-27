import java.math.BigInteger;

public class P16_Power_Digit_Sum {

	public static void main(String[] args) {
		String power = BigInteger.valueOf(2).pow(1000).toString();
		
		int result = 0;
		char []char_array = power.toCharArray();
		
		for (int i = 0; i < char_array.length; i ++) {
			result += Character.getNumericValue(char_array[i]);
		}
		
		System.out.print(result);
	}

}
