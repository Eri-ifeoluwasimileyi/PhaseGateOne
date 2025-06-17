public class TaskSix {


	public static void main(String[] args) {
		
	for(int number = 1; number <= 10; number++) {

		if(number % 4 == 0) {

			int multiple = 1;

			for(int count = 0; count < 5; count++) {  
				
				multiple *= number;
	
				System.out.println(multiple);

			}

		}
	

	}


	}
}