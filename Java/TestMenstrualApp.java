import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestMenstrualApp {

	@Test
	public void testCheckMonthFor31Days() {
        	int actual = MenstrualApp.checkMonth(1);
		int expected = 31;
		assertEquals(expected, actual);
	}

	@Test
	public void testCheckMonthFor28Days() {
		int actual = MenstrualApp.checkMonth(2);
		int expected = 28;
		assertEquals(expected, actual);
	}


	@Test
	public void testCheckMonthFor30Days() {
		int actual = MenstrualApp.checkMonth(9);
		int expected = 30;
		assertEquals(expected, actual);
	}

	@Test
	public void testCheckDaysSameMonth() {
		int[] actual = MenstrualApp.checkDays(25, 1, 5);
		int[] expected = {30, 1};
		assertArrayEquals(expected, actual);
	}

	@Test
	public void testCheckDaysNextMonth() {
		int[] actual = MenstrualApp.checkDays(28, 1, 15);
		int[] expected = {12, 2};
		assertArrayEquals(expected, actual);
	}

	@Test
	public void testDateIsValidFForSingleDayWithZero() {
		String actual = MenstrualApp.dateformat(5, 3);
		String expected = "05 - 03";
		assertEquals(expected, actual);


	}

	@Test
	public void testDateIsValidForDouble() {
		String actual = MenstrualApp.dateformat(12, 11);
		String expected = "12 - 11";
		assertEquals(expected, actual);
	}
}
