import java.util.Scanner;


public class MBTI {




	public static String extrovertIntrovert(String name) {

	Scanner input = new Scanner(System.in);


		int extroCount = 0;
		int introCount = 0;
		String[] responses = new String [5];
		int count = 0;
	
		while (true) {

			System.out.print("""
A: expand energy, enjoy groups
B: conserve energy, enjoy one-on-ones

		""");
			System.out.print("Choose A or B: ");
			String result = input.nextLine();

			result = result.toUpperCase();

			if (result.equals("A")) {
				extroCount++;
				responses[count++] = "A: expand energy, enjoy groups";
				break;

			} else if (result.equals("B")) {
				introCount++;
				responses[count++] = "B: conserve energy, enjoy one-on-ones";
				break;
	
			} else {
				System.out.println("Expected A or B as response");
				System.out.print("I know this is an error please try again");
				continue;
			}
		}



		while (true) {

			System.out.print("""
A: more outgoing, thinking loud
B: more reserved, thinking to yourself	
	
			""");
		
			System.out.print("Choose A or B: ");
			String userInput = input.nextLine();

			userInput = userInput.toUpperCase();

			if (userInput.equals("A")) {

				extroCount++;
				responses[count++] = "A: more outgoing, thinking loud";
				break;

			} else if (userInput.equals("B")) {
				introCount++;
				responses[count++] = "B: more reserved, thinking to yourself";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}


		}



	

		while (true) {

			System.out.println("""
A: seek many tasks, public activities, interaction with others
B: seek private, solitary activities with quiet to concentrate	

			""");
		
			System.out.print("Choose A or B: ");
			String answer = input.nextLine();

			answer = answer.toUpperCase();

			if (answer.equals("A")) {

			extroCount++;
			responses[count++] = "A: seek many tasks, public activities, interaction withothers";
			break;

			} else if (answer.equals("B")) {
				introCount++;
				responses[count++] = "B: seek private, solitary activities with quiet to concentrate";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}


		}


		while (true) {

        		System.out.println("""
A: external, communicative, express yourself
B: internal, reticent, keep to yourself	

			""");
		
			System.out.print("Choose A or B: ");
			String choice = input.nextLine();

			choice = choice.toUpperCase();


			if (choice.equals("A")) {
				extroCount++;
				responses[count++] = "A: external, communicative, express yourself";
				break;

			} else if (choice.equals("B")) {
				introCount++;
				responses[count++] = "B: internal, reticent, keep to yourself";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}

		}





		while (true) {

       			System.out.println("""
A: active, initiate
B: reflective, deliberate

		""");
		
			System.out.print("Choose A or B: ");
			String userOutput = input.nextLine();

			userOutput = userOutput.toUpperCase();

			if (userOutput.equals("A")) {
				extroCount++;
				responses[count++] = "A: active, initiate";
				break;

			} else if (userOutput.equals("B")) {
				introCount++;
				responses[count++] = "B: reflective, deliberate";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}

	
		}




		System.out.println("Hello " + name + ". You selected: ");

		for(int ans = 0; ans < responses.length; ans++) {

			System.out.println(responses[ans]);

		}
		System.out.println();
		System.out.println("Number of A selected: " + extroCount);
		System.out.println("Number of B selected: " + introCount);

		if (extroCount > introCount) {
			return "E";
	
		} else {

			return "I";
		}

	}




	
	public static String sensingIntuitive(String name) {

	Scanner input = new Scanner(System.in);



		int sensingCount = 0;
		int intuitiveCount = 0;
		String[] responses = new String [5];
		int count = 0;



		while (true) {

			System.out.print("""
A: Interpret literally
B: look for meaning and possibilities
	
		""");

			System.out.print("Choose A or B: ");
			String result = input.nextLine();

			result = result.toUpperCase();

			if (result.equals("A")) {
				sensingCount++;
				responses[count++] = "A: Interpret literally";
				break;

			} else if (result.equals("B")) {
				intuitiveCount++;
				responses[count++] = "B: look for meaning and possibilities";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}
		}




		while (true) {

			System.out.println("""
A: practical, realistic, experiential
B: imaginative, innovative, theoretical	

			""");
		
			System.out.print("Choose A or B: ");
			String userInput = input.nextLine();

			userInput = userInput.toUpperCase();

			if (userInput.equals("A")) {
				sensingCount++;
				responses[count++] = "A: practical, realistic, experiential";
				break;

			} else if (userInput.equals("B")) {
				intuitiveCount++;
				responses[count++] = "B: imaginative, innovative, theoretical";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}


		}




		while (true) {

       			System.out.print("""
A: standard, usual, conventional
B: different, novel, unique

			""");
		
			System.out.print("Choose A or B: ");
			String answer = input.nextLine();

			answer = answer.toUpperCase();

			if (answer.equals("A")) {
				sensingCount++;
				responses[count++] = "A: standard, usual, conventional";
				break;

			} else if (answer.equals("B")) {
				intuitiveCount++;
				responses[count++] = "B: different, novel, unique";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}


		}




		while (true) {

        		System.out.print("""
A: focus on here-and-now
B: look to the future, global perspective, big picture	

			""");
		
			System.out.print("Choose A or B: ");
			String choice = input.nextLine();

			choice = choice.toUpperCase();

			if (choice.equals("A")) {
				sensingCount++;
				responses[count++] = "A: focus on here-and-now";
				break;

			} else if (choice.equals("B")) {
				intuitiveCount++;
				responses[count++] = "B: look to the future, global perspective, big picture";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}


		}





		while (true) {

        		System.out.print("""
A: facts, things, what is
B: ideas, dreams, what could be, philosophical
	
			""");
		
			System.out.print("Choose A or B: ");
			String userOutput = input.nextLine();

			userOutput = userOutput.toUpperCase();

			if (userOutput.equals("A")) {
				sensingCount++;
				responses[count++] = "A: facts, things, what is";
				break;

			} else if (userOutput.equals("B")) {
				intuitiveCount++;
				responses[count++] = "B: ideas, dreams, what could be, philosophical";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}


		}




		System.out.println("Hello " + name + ". You selected: ");

		for(int ans = 0; ans < responses.length; ans++) {

			System.out.println(responses[ans]);

		}

		System.out.println();
		System.out.println("Number of A selected: " + sensingCount);
		System.out.println("Number of B selected: " + intuitiveCount);

		if (sensingCount > intuitiveCount) {
			return "S";
	
		} else {

			return "N";
		}

	}




	public static String thinkingFeeling(String name) {

	Scanner input = new Scanner(System.in);


		int thinkingCount = 0;
		int feelingCount = 0;
		String[] responses = new String [5];
		int count = 0;

		while (true) {

			System.out.print("""
A: logical, thinking, questioning
B: empathetic, feeling, accommodating

		""");

			System.out.print("Choose A or B: ");
			String result = input.nextLine();

			result = result.toUpperCase();
	
			if (result.equals("A")) {
				thinkingCount++;
				responses[count++] = "A: logical, thinking, questioning";
				break;

			} else if (result.equals("B")) {
				feelingCount++;
				responses[count++] = "B: empathetic, feeling, accommodating";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}
		}




		while (true) {

			System.out.print("""
A: candid, straight forward, frank
B: tactful, kind, encouraging

			""");
		
			System.out.print("Choose A or B: ");
			String userInput = input.nextLine();

			userInput = userInput.toUpperCase();
	
			if (userInput.equals("A")) {
				thinkingCount++;
				responses[count++] = "A: candid, straight forward, frank";
				break;

			} else if (userInput.equals("B")) {
				feelingCount++;
				responses[count++] = "B: tactful, kind, encouraging";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}

		}




		while (true) {

		        System.out.print("""
A: firm, tend to criticise, hold the line
B: gentle, tend to appreciate, conciliate

			""");
		
			System.out.print("Choose A or B: ");
			String answer = input.nextLine();

			answer = answer.toUpperCase();

			if (answer.equals("A")) {
				thinkingCount++;
				responses[count++] = "A: firm, tend to criticise, hold the line";
				break;

			} else if (answer.equals("B")) {
				feelingCount++;
				responses[count++] = "B: gentle, tend to appreciate, conciliate";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}


		}



	
	
		while (true) {

        		System.out.print("""
A: tough-minded, just
B: tender-hearted, merciful

			""");
		
			System.out.print("Choose A or B: ");
			String choice = input.nextLine();

			choice = choice.toUpperCase();

			if (choice.equals("A")) {
				thinkingCount++;
				responses[count++] = "A: tough-minded, just";
				break;

			} else if (choice.equals("B")) {
				feelingCount++;
				responses[count++] = "B: tender-hearted, merciful";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}


		}




		while (true) {

        		System.out.print("""
A: matter of fact, issue-oriented
B: sensitive, people-oriented, compassionate

			""");
		
			System.out.print("Choose A or B: ");
			String userOutput = input.nextLine();

			userOutput = userOutput.toUpperCase();

			if (userOutput.equals("A")) {
				thinkingCount++;
				responses[count++] = "A: matter of fact, issue-oriented";
				break;

			} else if (userOutput.equals("B")) {
				feelingCount++;
				responses[count++] = "B: sensitive, people-oriented, compassionate";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}


		}





		System.out.println("Hello " + name + ". You selected: ");

		for(int ans = 0; ans < responses.length; ans++) {

			System.out.println(responses[ans]);

		}

		System.out.println();
		System.out.println("Number of A selected: " + thinkingCount);
		System.out.println("Number of B selected: " + feelingCount);

		if (thinkingCount > feelingCount) {

			return "T";
	
		} else {

			return "F";
		}

	}





	public static String judgingPerceptive(String name) {

	Scanner input = new Scanner(System.in);
	

		int judgingCount = 0;
		int percepCount = 0;
		String[] responses = new String [5];
		int count = 0;


		while (true) {

			System.out.print("""
A: organised, orderly
B: flexible, adaptable

		""");

			System.out.print("Choose A or B: ");
			String result = input.nextLine();
	
			result = result.toUpperCase();
	
			if (result.equals("A")) {
				judgingCount++;
				responses[count++] = "A: organised, orderly";
				break;

			} else if (result.equals("B")) {
				percepCount++;
				responses[count++] = "B: flexible, adaptable";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}
		}






		while (true) {
	
			System.out.print("""
A: plan, schedule
B: unplanned, spontaneous

			""");
		
			System.out.print("Choose A or B: ");
			String userInput = input.nextLine();

			userInput = userInput.toUpperCase();

			if (userInput.equals("A")) {
				judgingCount++;
				responses[count++] = "A: plan, schedule";
				break;

			} else if (userInput.equals("B")) {
				percepCount++;
				responses[count++] = "B: unplanned, spontaneous";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}


		}




		while (true) {

        		System.out.print("""
A: regulated, structured
B: easy-going, live and let live

			""");
		
			System.out.print("Choose A or B: ");
			String answer = input.nextLine();

			answer = answer.toUpperCase();

			if (answer.equals("A")) {
				judgingCount++;
				responses[count++] = "A: regulated, structured";
				break;

			} else if (answer.equals("B")) {
				percepCount++;
				responses[count++] = "B: easy-going, live and let live";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}

		
		}







		while (true) {

        		System.out.print("""
A: preparation, plan ahead
B: go with the flow, adapt as you go

			""");
		
			System.out.print("Choose A or B: ");
			String choice = input.nextLine();

			choice = choice.toUpperCase();

			if (choice.equals("A")) {
				judgingCount++;
				responses[count++] = "A: preparation, plan ahead";
				break;

			} else if (choice.equals("B")) {
				percepCount++;
				responses[count++] = "B: go with the flow, adapt as you go";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}


		}





		while (true) {

       			System.out.print("""
A: control, govern
B: latitude, freedom
	
	""");
		
			System.out.print("Choose A or B: ");
			String userOutput = input.nextLine();

			userOutput = userOutput.toUpperCase();

			if (userOutput.equals("A")) {
				judgingCount++;
				responses[count++] = "A: control, govern";
				break;

			} else if (userOutput.equals("B")) {
				percepCount++;
				responses[count++] = "B: latitude, freedom";
				break;

			} else {
				System.out.println("Expected A or B as response");
				System.out.println("I know this is an error please try again");
				continue;
			}

	
		}




		System.out.println("Hello " + name + ". You selected: ");

		for(int ans = 0; ans < responses.length; ans++) {

			System.out.println(responses[ans]);

		}

		System.out.println();
		System.out.println("Number of A selected: " + judgingCount);
		System.out.println("Number of B selected: " + percepCount);

		if (judgingCount > percepCount) {

			return "J";
	
		} else {

			return "P";
		}

	}




	public static String mbtiDescription(String mbti) {

	
		switch(mbti.toUpperCase()) {
	

			case "ISTJ":

					return "ISTJ: ISTJ (Logistician) is a personality type with the Introverted, Observant, Thinking, and Judging traits.These people tend to be reserved yet willful, with a rational outlook on life.";


			case "ISFJ":

				return "ISFJ: ISFJ (Defender) is a personality type with the Introverted, Observant, Feeling, and Judging traits.These people tend to be warm and unassuming in their own steady way.";


			case "INFJ":

				return "INFJ: INFJ (Advocate) is a personality type with the Introverted, Intuitive, Feeling, and Judging traits.They tend to approach life with deep thoughtfulness and imagination.";


			case "INTJ":

				return "INTJ: INTJ (Architect) is a personality type with the Introverted, Intuitive, Thinking, and Judging traits.These thoughtful tacticians love perfecting the details of life, applying creativity and rationality to everything they do.";


	
			case "ISTP":

				return "ISTP: ISTP (Virtuoso) is a personality type with the Introverted, Observant, Thinking, and Prospecting traits.They tend to have an individualistic mindset, pursuing goals without needing much external connection.";



			case "ISFP":

				return "ISFP: ISFP (Adventurer) is a personality type with the Introverted, Observant, Feeling, and Prospecting traits.They tend to have open minds, approaching life, new experiences, and people with grounded warmth.";


			case "INFP":

				return "INFP: INFP (Mediator) is a personality type with the Introverted, Intuitive, Feeling, and Prospecting traits.These rare personality types tend to be quiet, open-minded, and imaginative, and they apply a caring and creative approach to everything they do.";


			case "INTP":

				return "INTP: INTP (Logician) is a personality type with the Introverted, Intuitive, Thinking, and Prospecting traits.These flexible thinkers enjoy taking an unconventional approach to many aspects of life.";


			case "ESTP":

				return "ESTP: ESTP (Entrepreneur) is a personality type with the Extraverted, Observant, Thinking, and Prospecting traits.They tend to be energetic and action-oriented, deftly navigating whatever is in front of them.";


			case "ESFP":

				return "ESFP: ESFP (Entertainer) is a personality type with the Extraverted, Observant, Feeling, and Prospecting traits.These people love vibrant experiences, engaging in life eagerly and taking pleasure in discovering the unknown.";


			case "ENFP":

				return "ENFP: ENFP (Campaigner) is a personality type with the Extraverted, Intuitive, Feeling, and Prospecting traits.These people tend to embrace big ideas and actions that reflect their sense of hope and goodwill toward others.";


			case "ENTP":

				return "ENTP: ENTP (Debater) is a personality type with the Extraverted, Intuitive, Thinking, and Prospecting traits.They tend to be bold and creative, deconstructing and rebuilding ideas with great mental agility.";


			case "ESTJ":

				return "ESTJ: ESTJ (Executive) is a personality type with the Extraverted, Observant, Thinking, and Judging traits.They possess great fortitude, emphatically following their own sensible judgment.";


			case "ESFJ":

				return "ESFJ: ESFJ (Consul) is a personality type with the Extraverted, Observant, Feeling, and Judging traits.They are attentive and people-focused, and they enjoy taking part in their social community." ;


			case "ENFJ":

				return "ENFJ: ENFJ (Protagonist) is a personality type with the Extraverted, Intuitive, Feeling, and Judging traits. These warm, forthright types love helping others, and they tend to have strong ideas and values.";


			case "ENTJ":

				return "ENTJ: ENTJ (Commander) is a personality type with the Extraverted, Intuitive, Thinking, and Judging traits.";



			default:
		
				return "Description not found for this MBTI type.";


	}
}



	public static void main(String[] args) {

	Scanner input = new Scanner(System.in);


		System.out.print("Enter your name: ");
		String name = input.nextLine();

		String extroIntro = extrovertIntrovert(name);

		String senseIntuit = sensingIntuitive(name);

		String thinkFeel = thinkingFeeling(name);
		
		String judgePercep = judgingPerceptive(name);


	
		String mbtiTog = extroIntro + senseIntuit + thinkFeel + judgePercep;

		String description = mbtiDescription(mbtiTog);



		System.out.println("Your MBTI personality type is: " + mbtiTog);
		System.out.println();
		System.out.println(description);

  	}


}















