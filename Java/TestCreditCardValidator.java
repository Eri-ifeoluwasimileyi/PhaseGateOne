import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestCreditCardValidator {



	@Test
	public void testVisaCardIsValid() {
	
	String card = "4132465789041896";

	String expected = "VisaCard";

	String returned = CreditCardValidator.validateCard(card);
	
	assertEquals(expected, returned);

	}



	@Test
	public void testMasterCardIsValid() {
	
	String card = "5132465789041896";

	String expected = "MasterCard";

	String returned = CreditCardValidator.validateCard(card);
	
	assertEquals(expected, returned);

	}


	@Test
	public void testDiscoverCardIsValid() {
	
	String card = "6132465789041896";

	String expected = "Discover Card";

	String returned = CreditCardValidator.validateCard(card);
	
	assertEquals(expected, returned);

	}


	@Test
	public void testAmericanExpressCardIsValid() {
	
	String card = "371246578904189";

	String expected = "America Express";

	String returned = CreditCardValidator.validateCard(card);
	
	assertEquals(expected, returned);

	}



	@Test
	public void testLengthIsInvalid() {
	
	String card = "4132465789";

	String expected = "Invalid Card Length";

	String returned = CreditCardValidator.validateCard(card);
	
	assertEquals(expected, returned);

	}




	@Test
	public void testMasterIsValid() {
	
	String card = "5399831619690403";

	String expected = "Valid";

	String returned = CreditCardValidator.checkValidity(card);
	
	assertEquals(expected, returned);

	}


	@Test
	public void testMasterIsInvalid() {
	
	String card = "5399831619690404";

	String expected = "Invalid";

	String returned = CreditCardValidator.checkValidity(card);
	
	assertEquals(expected, returned);

	}



	@Test
	public void testVisaIsValid() {
	
	String card = "4388576018410707";

	String expected = "Valid";

	String returned = CreditCardValidator.checkValidity(card);
	
	assertEquals(expected, returned);

	}



	@Test
	public void testVisaIsInvalid() {
	
	String card = "4388576018402626";

	String expected = "Invalid";

	String returned = CreditCardValidator.checkValidity(card);
	
	assertEquals(expected, returned);

	}


	@Test
	public void testAmericanIsValid() {
	
	String card = "3788576018402629";

	String expected = "Valid";

	String returned = CreditCardValidator.checkValidity(card);
	
	assertEquals(expected, returned);

	}



	@Test
	public void testAmericanIsInvalid() {
	
	String card = "3788576018402626";

	String expected = "Invalid";

	String returned = CreditCardValidator.checkValidity(card);
	
	assertEquals(expected, returned);

	}



	@Test
	public void testDicoverIsValid() {
	
	String card = "6388576018410702";

	String expected = "Valid";

	String returned = CreditCardValidator.checkValidity(card);
	
	assertEquals(expected, returned);

	}



	@Test
	public void testDicoverIsInvalid() {
	
	String card = "6388576018410703";

	String expected = "Invalid";

	String returned = CreditCardValidator.checkValidity(card);
	
	assertEquals(expected, returned);

	}






}








