import java.util.Scanner;

public class CreditCardValidator {


	public static String validateCard(String cardNumber){

		if(cardNumber.length() <= 13 || cardNumber.length() > 16){
			return "Invalid Card Length";
		}

		if(cardNumber.charAt(0) == '4'){
			return "VisaCard";
		}

		else if(cardNumber.charAt(0) == '5'){
	
			return "MasterCard";
		}

		else if(cardNumber.charAt(0) == '6'){

			return "Discover Card";
		}

		else if(cardNumber.charAt(0) == '3' && cardNumber.charAt(1) == '7'){
			return "America Express";
		}
	
		else 
			return "Invalid Card";

	}
  

	public static String checkValidity(String cardNumber){

		int sumOdd = 0
		int sumEven = 0
		int totalSum = 0;
	
		int size = cardNumber.length();

	
        	for (int index = size - 1; index >= 0; index--) {
		
			int digits = cardNumber.charAt(index) - '0';

        	    	if ((size - index) % 2 == 0) { 
			// to count the second number from the back,15 -14
				digits *= 2;
	
				if(digits > 9) {

					digits = (digits / 10) + (digits % 10);
				}
				sumEven += digits;
			

			}
			else {
				sumOdd += digits;
			}
		}

        	totalSum = sumEven + sumOdd;
		
		if(totalSum % 10 == 0) return "Valid";

		else return "Invalid";

		
	}
	

	public static void main(String [] args) {

		Scanner input = new Scanner(System.in);

		System.out.println("Hello, Kindly Enter Card details to verify: ");
		String userInput = input.nextLine();

		System.out.println();

		System.out.println("****************************************");

		System.out.println("***Credit Card Type: " + validateCard(userInput));

		System.out.println("***Credit Card Number: " + userInput);

		System.out.println("***Credit Card Digit Length: " +  userInput.length());

		System.out.println("***Credit Card Validity Status: " + checkValidity(userInput));

		System.out.println("****************************************");

	}


}
