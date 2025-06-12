public class TestMBTI {

	@Test
	public void testFunctionIsValid1() {
        	String actual = MBTI.extrovertIntrovert("ola");
		String expected = "I";
		assertEquals(expected, actual);
	}


	@Test
	public void testFunctionIsValid2() {
        	String actual = MBTI.extrovertIntrovert("ola");
		String expected = "E";
		assertEquals(expected, actual);
	}


	@Test
	public void testFunctionIsValid3() {
        	String actual = MBTI.sensingIntuitive("ola");
		String expected = "S";
		assertEquals(expected, actual);
	}


	@Test
	public void testFunctionIsValid4() {
        	String actual = MBTI.sensingIntuitive("ola");
		String expected = "N";
		assertEquals(expected, actual);
	}


	@Test
	public void testFunctionIsValid5() {
        	String actual = MBTI.thinkingFeeling("ola");
		String expected = "T";
		assertEquals(expected, actual);
	}


	@Test
	public void testFunctionIsValid6() {
        	String actual = MBTI.thinkingFeeling("ola");
		String expected = "F";
		assertEquals(expected, actual);
	}


	@Test
	public void testFunctionIsValid7() {
        	String actual = MBTI.judgingPerceptive("ola");
		String expected = "J";
		assertEquals(expected, actual);
	}



	@Test
	public void testFunctionIsValid8() {
        	String actual = MBTI.judgingPerceptive("ola");
		String expected = "P";
		assertEquals(expected, actual);
	}

}