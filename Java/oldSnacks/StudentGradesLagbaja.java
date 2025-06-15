import java.util.Scanner;


public class StudentGradesLagbaja {


	
	public static int[][] scoreAndGrade(int numOfStudents, int numOfSubjects) {

	Scanner input = new Scanner(System.in);

		int [][] grades = new int [numOfStudents][numOfSubjects];
		//this 2D array is to hold the student scores, the rows for each students,and the columns for each subject
		
		for(int student = 0; student < numOfStudents; student++) {

			for(int subject = 0; subject < numOfSubjects; subject++) {
				
				while (true) {

					System.out.println("Entering score for student " + (student + 1));
					System.out.println("Enter score for subject " + (subject + 1));
					int score = input.nextInt();			
					
					if(score > 0 && score <= 100) {
						System.out.println();
						System.out.println("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>>>");

						grades[student][subject] = score;

						System.out.println("Saved Successfully");
						System.out.println();
						break;

					} else {
	
						System.out.println("Invalid input, Try Again");
						continue;
					}
				}
			}

		}
		return grades;
	}

	

	public static Boolean gradeCalculation(int [][] grades) {

		int numOfStudents = grades.length;

		int numOfSubjects = grades[0].length;
		//to assume all students have the same number of subjects

		int[] totalScore = new int[numOfStudents];

		for(int student = 0; student < numOfStudents; student++) {
	
			int total = 0;
		
			for(int subject = 0; subject < numOfSubjects; subject++) {

				total += grades[student][subject];
				//add all the subject for each student
			}	
			totalScore[student] = total;
			//store the totol of the subject for each student
		}

		System.out.println("=============================================================================");

		System.out.print("STUDENT" + "\t\t");

		for (int index = 1; index <= numOfSubjects; index++) {
		//It prints column headers for each subject starting from 1
			System.out.print("SUB" + index + "\t");

		}

		System.out.print("TOT");

		System.out.print("\tAVE");

		System.out.print("\tPOS");

		System.out.println();

		System.out.println("=============================================================================");


		for (int student = 0; student < numOfStudents; student++) {

			System.out.print("Student " + (student + 1));
		

			for(int subject = 0; subject < numOfSubjects; subject++) {

				System.out.print(" \t " + grades[student][subject]);
			//iterate through each subject for each student and print the score
			}

			int total = totalScore[student];
				
			double average = (double)total / numOfSubjects;

			
			int position = 1;
			for(int counter = 0; counter < numOfStudents; counter++) {
			//compare each student’s totalScore to total
				if(totalScore[counter] > total) //when a student has a high score, increase the position
					position++;
	
			}
		

			System.out.print("\t" + total);

			System.out.printf("\t%.2f", average);

			System.out.print("\t" + position);
	
			System.out.println();
		
		}
		System.out.println("=============================================================================");
		System.out.println("=============================================================================");	
		System.out.println();
		
	return true;
	}

