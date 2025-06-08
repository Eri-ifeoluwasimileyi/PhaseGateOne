const prompt = require('prompt-sync')();

const dayjs = require('dayjs');



function checkName(name){

	if(!name) return false;
	
	if(name.startsWith(" ") || name.endsWith(" ")) return false;
	
	if(name.length < 2 || name.length > 30) return false;
	return true;


}

function checkAmount(amount){

	if(isNaN(Number(amount))) return false;
	else
	if(amount < 1) return false;
	else return true;

}

 

function printInvoice(cart, cashierName, customerName, discountRate){


	const now = dayjs();
	const date = now.format('DD-MMM-YYYY hh:mm:ss P');


	let subtotal = 0;

	for (const item of cart) {
		subtotal += item.price * item.quantity;
	}

	let discount = subtotal * (discountRate / 100);

	let afterDiscount = subtotal - discount;

	let VAT = afterDiscount * 0.075;

	let total = afterDiscount + VAT;


	console.log(`
	MID-DAY STORE
	MAIN BRANCH
	LOCATION: 545 Groove street, Lagos
	Tel: +2349027871650
	Date: ${date}
	Cashier: ${cashierName}
	Customer's name: ${customerName}
	
	=================================================
		ITEM           QTY     PRICE     TOTAL
	-------------------------------------------------
						`);

	for (item of cart) {

		let totalItem = item.price * item.quantity;

 		 console.log(`\t\t${item.name}\t\t${item.quantity}\t${item.price.toFixed(2)}\t${totalItem.toFixed(2)}`);
}

	console.log(`
	-------------------------------------------------
			Sub Total:   ${subtotal.toFixed(2)}
			Discount:    ${discount.toFixed(2)}
			VAT @ 7.5%:  ${VAT.toFixed(2)}
	=================================================
			Bill Total:  ${total.toFixed(2)}
	=================================================
	THIS IS NOT A RECEIPT. PAY: ${total.toFixed(2)}
	=================================================
						`);


	return total;
}



function printReceipt(cart, cashierName, customerName, discountRate, payment) {


	const now = dayjs();
	const date = now.format('DD-MMM-YYYY hh:mm:ss P');

	
	let subtotal = 0;

	for (const item of cart) {
		subtotal += item.price * item.quantity;
	}

	let discount = subtotal * (discountRate / 100);

	let afterDiscount = subtotal - discount;

	let VAT = afterDiscount * 0.075;

	let total = afterDiscount + VAT;

	let balance = payment - total;
	
	payment = Number(payment);


	console.log(`
	MID-DAY STORE
	MAIN BRANCH
	LOCATION: 545 Groove street, Lagos
	Tel: +2349027871650
	Date: ${date}
	Cashier: ${cashierName}
	Customer's name: ${customerName}

	==================================================
		ITEM      QTY      PRICE      TOTAL
	-------------------------------------------------
						`);

	for (const item of cart) {

		let totalItem = item.price * item.quantity;

 		 console.log(`\t\t${item.name}\t\t${item.quantity}\t${item.price.toFixed(2)}\t${totalItem.toFixed(2)}`);
};

	console.log(`
	-------------------------------------------------
			Sub Total:   ${subtotal.toFixed(2)}
			Discount:    ${discount.toFixed(2)}
			VAT @ 7.5%:  ${VAT.toFixed(2)}
	=================================================
			Bill Total:  ${total.toFixed(2)}
			Amount Paid: ${payment.toFixed(2)}
			Balance:     ${balance.toFixed(2)}
	=================================================
		THANK YOU FOR YOUR PATRONAGE
	=================================================
						`);

	return balance

};



let cart = [];

let customerName = prompt("What is the customer name: ");
if(!checkName(customerName)) {
	console.log("Invalid customer name.");

}else {


let check = true;

while (true) {

	while (check) {

		let name = prompt("What did the user buy?: ")
			
		if(!checkName(name)){
			
			console.log("invalid name");
			continue;
		}

		let quantity = prompt("How many pieces?: ");
		
		if(Number(quantity)) {
		
			if(quantity <= 0) {
				console.log("Invalid input");	 
				continue;
			}
		}else{
		console.log("Quantity must be a positive number.");
		continue;
		}

		let price = prompt("How much per unit?: ");

		if(!checkAmount(price)) {

			console.log("invalid input");
			continue;
		}

		cart[cart.length] = {'name': name, 'quantity': Number(quantity), 'price': Number(price)};

		while (check) {

			let userChoice = prompt("Do you want to add another item? (yes/no): ");
			userChoice = userChoice.toLowerCase();
	
			if(userChoice == "yes") {

				break;

			}else{
			
			if(userChoice == "no") {

				check = false
				break
			}
			}
		}
	}
	if(cart.length > 0) {

		
		let cashierName = prompt("Enter cashier name?: ");

		if(!checkName(cashierName)){
			
			console.log("invalid name");
			continue;
		}

		
		let discount = prompt("Enter discount rate: ");
		
		
			if(!checkAmount(discount)) {

				console.log("invalid input");
				continue;

				discount = 0.0;	

			}

		let total = printInvoice(cart, cashierName, customerName, discount);
		
		let cash = prompt("How much did the customer give to you?: ");

		if(!checkAmount(cash)) {

			console.log("invalid input");
			continue;
	
			cash = 0.0;
		}

		printReceipt(cart, cashierName, customerName, discount, cash);
		break;

	}else{
	
	console.log("No items in cart. Invoice cannot be raised.")
	}
	
}
}
			


