public class TaskEight {


	public static void main(String[] args) {
		

	for(int number = 1; number <= 10; number++) {
		int total = 0;

		if(number % 4 == 0) {

			int multiple = 1;

			int sum = 0;
			for(int count = 0; count < 5; count++) {  
				
				multiple *= number;
	
				sum += sum;

				total += sum;

				System.out.println(total);

			}

		}
	

	}


	}
}