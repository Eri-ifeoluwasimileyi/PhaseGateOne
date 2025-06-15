const prompt = require('prompt-sync')();

let grades = [];

function scoreAndGrade(numOfStudents, numOfSubjects) {


	for(let student = 0; student < numOfStudents; student++) {
		grades[student] = [];

		for(let subject = 0; subject < numOfSubjects; subject++) {

			while(true) {
		
				console.log("Entering score for student " + (student + 1));
				let score = parseFloat(prompt("Enter score for subject " + (subject + 1) + ": "));
				
				if(score > 0 && score <= 100) {
		
			console.log();
					console.log("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>>>");

					grades[student][subject] = score;

					console.log("Saved Successfully");
					console.log();
					break;

				} else {

					console.log("Invalid input, Try Again");
					continue;
				}
			}

		}
	}
	return grades;

}


function gradeCalculation(grades) {

	let numOfStudents = grades.length;

	let numOfSubjects = grades[0].length;

	let totalScore = [];

	for(let student = 0; student < numOfStudents; student++) {

		let total = 0;
		
		for(let subject = 0; subject < numOfSubjects; subject++) {

			total += grades[student][subject];
		}
		totalScore[student] = total;
	}
	
	console.log("=============================================================================");

	let line = "STUDENT\t\t";

	for(let index = 1; index <= numOfSubjects; index++) {

		line += "SUB" + index + "\t";
	}

	console.log(line + "TOT\tAVE\tPOS");

	console.log();


	console.log("=============================================================================");

		for(let student = 0; student < numOfStudents; student++) {

			let line = "Student " + (student + 1);

			for(let subject = 0; subject < numOfSubjects; subject++) {

				line += "\t" + grades[student][subject];
			}
			
			let total = totalScore[student];
		
			let average = total / numOfSubjects;

			
			let position = 1;
			for(let counter = 0; counter < numOfStudents; counter++) {

				if(totalScore[counter] > total)
					
					position++;
			}

			line += "\t" + total + "\t" + parseFloat(average.toFixed(2)) + "\t" + position;
			console.log(line);
			console.log();

		}
	console.log("=========================================================================");

	console.log("=========================================================================");
	
	console.log();
}