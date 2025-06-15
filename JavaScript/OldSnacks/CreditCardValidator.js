const prompt = require('prompt-sync')();


function validateCard(cardNumber) {

	if(cardNumber.length <= 13 || cardNumber.length > 16){
		return "Invalid Card Length";
	}

	if(cardNumber.charAt(0) == '4'){
		return "VisaCard";
	}

	else if(cardNumber.charAt(0) == '5'){
	
		return "MasterCard";
	}

	else if(cardNumber.charAt(0) == '6'){

		return "DiscoverCard";
	}

	else if(cardNumber.charAt(0) == '3' && cardNumber.charAt(1) == '7'){
		return "American Express";

	}
	
	else 
		return "Invalid Card";

}



function checkValidity(cardNumber) {



	let sumOdd = 0
	let sumEven = 0
	let totalSum = 0;
	
	let size = cardNumber.length;


	for (let index = size - 1; index >= 0; index--) {
		
		let digits = Number(cardNumber.charAt(index));

		if ((size - index) % 2 == 0) { 

			digits *= 2;
	
			if(digits > 9) {

				digits = Math.floor(digits / 10) + (digits % 10);
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




let userInput = String(prompt("Hello, Kindly Enter Card details to verify: "));

console.log()

console.log("****************************************");

console.log("***Credit Card Type: " + validateCard(userInput));

console.log("***Credit Card Number: " + userInput);

console.log("***Credit Card Digit Length: " +  userInput.length);

console.log("***Credit Card Validity Status: " + checkValidity(userInput));

console.log("****************************************");























