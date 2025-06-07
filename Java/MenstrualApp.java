import java.util.Scanner;

public class MenstrualApp {


	public static int checkMonth(int month) {

		if(month == 2) return 28;

		else

		if(month == 4 || month == 6) return 30;
	
		if(month == 9 || month == 11) return 30;

		else return 31;

	}
	public static int[] checkDays(int lastPeriodDay, int periodMonth, int daysToAdd) {

		while(daysToAdd > 0) {

			int daysInAMonth = checkMonth(periodMonth);

			if(lastPeriodDay + daysToAdd <= daysInAMonth) {
				
				lastPeriodDay = lastPeriodDay + daysToAdd;
				return new int[]{lastPeriodDay, periodMonth};
			}else {
		
				daysToAdd -= (daysInAMonth - lastPeriodDay + 1);
				lastPeriodDay = 1;
				periodMonth++;
					
				if(periodMonth > 12) {
					periodMonth = 1;

			
				}
			}
		}

		return new int[] {lastPeriodDay, periodMonth};
	}




	public static String twoNumbers(int number) {
	
	if(number < 10) return "0" + number;

	else return "" + number;
	
	
	}

	


	public static String dateformat(int day, int month) {

		return twoNumbers(day) + " - " + twoNumbers(month);

	}





	public static void main(String[] args) {


		Scanner input = new Scanner(System.in);


		System.out.print("""

			====================
			Menstrual Calculator
			====================
					my pride!!
		
					""");	
		

	System.out.print("Enter first day of your last period (1-31): ");
	int lastPeriod = input.nextInt();
	System.out.println();
	
	System.out.print("Enter the month (1-12): ");
	int periodMonth = input.nextInt();
	System.out.println();
	
	System.out.print("How long does your periods last on average: ");
	int periodDays = input.nextInt();
	System.out.println();

	System.out.print("What is your average cycle length (days): ");
	int cycleLength = input.nextInt();
	System.out.println();
	

	int ovulationDay = cycleLength / 2;

	int fertileWindow = ovulationDay - 5;

	int fertileWindowEnd = ovulationDay + 1;
	
	int nextPeriod = cycleLength + 1;

	int rangeOfNextPeriod = nextPeriod + periodDays;


	int[] ovulationDate = checkDays(lastPeriod, periodMonth, ovulationDay);

	int[] fertileStart = checkDays(lastPeriod, periodMonth, fertileWindow);
	
	int[] fertileEnd = checkDays(lastPeriod, periodMonth, fertileWindowEnd);

	int[] nextPeriodStart = checkDays(lastPeriod, periodMonth, nextPeriod);
	
	int[] nextPeriodEnd = checkDays(lastPeriod, periodMonth, rangeOfNextPeriod);



	System.out.println("Calculating, please wait......");
	System.out.println();
	System.out.println();
	
	System.out.println("Your estimated ovulation date is: " + dateformat(ovulationDate[0], ovulationDate[1]));
	System.out.println();

	System.out.println("Fertile window starts: " + dateformat(fertileStart[0], fertileEnd[1]));
	System.out.println();

	System.out.println("Your next period is estimated to be between: " + dateformat(nextPeriodStart[0], nextPeriodStart[1]) + " and " + dateformat(nextPeriodEnd[0], nextPeriodEnd[1]));	
	System.out.println();



	}



}

