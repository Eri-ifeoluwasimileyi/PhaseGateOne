const prompt = require('prompt-sync')();


function extrovertIntrovert(name) {

	let extroCount = 0;
	let introCount = 0;
	let responses = [];
	let count = 0;

	while (true) {

		console.log(`
A: expand energy, enjoy groups
B: conserve energy, enjoy one-on-ones
		`)

		let result = prompt('choose A or B: ');

		result = result.toUpperCase();

		if (result === 'A') {
			extroCount++;
			responses[count++] = 'A: expand energy, enjoy groups';
			break;

		} else if (result === 'B') {
			introCount++;
			responses[count++] = 'B: conserve energy, enjoy one-on-ones';
			break
		} else {
			console.log('Expected A or B as response');
			console.log('I know this is an error please try again');
			continue;
		}
	}


	while (true) {

		console.log(`
A: more outgoing, thinking loud
B: more reserved, thinking to yourself		
			`);
		
		let userInput = prompt("choose A or B: ");

		userInput = userInput.toUpperCase();

		if (userInput === 'A') {

			extroCount++;
			responses[count++] = 'A: more outgoing, thinking loud';
			break;

		} else if (userInput === 'B') {
			introCount++;
			responses[count++] = 'B: more reserved, thinking to yourself';
			break;
		} else {
			console.log('Expected A or B as response')
			console.log('I know this is an error please try again')
			continue;
		}


	}




	while (true) {

        console.log(`
A: seek many tasks, public activities, interaction with others
B: seek private, solitary activities with quiet to concentrate	
			`);
		
		let answer = prompt("choose A or B: ");

		answer = answer.toUpperCase();

		if (answer === 'A') {

			extroCount++;
			responses[count++] = 'A: seek many tasks, public activities, interaction withothers';
			break;

		} else if (answer === 'B') {
			introCount++;
			responses[count++] = 'B: seek private, solitary activities with quiet to concentrate';
			break;
		} else {
			console.log('Expected A or B as response')
			console.log('I know this is an error please try again')
			continue;
		}


	}



	while (true) {

        console.log(`
A: external, communicative, express yourself
B: internal, reticent, keep to yourself	
			`);
		
		let choice = prompt("choose A or B: ");

		choice = choice.toUpperCase();

		if (choice === 'A') {

			extroCount++;
			responses[count++] = 'A: external, communicative, express yourself';
			break;

		} else if (choice === 'B') {
			introCount++;
			responses[count++] = 'B: internal, reticent, keep to yourself';
			break;

		} else {
			console.log('Expected A or B as response')
			console.log('I know this is an error please try again')
			continue;
		}


	}





	while (true) {

        console.log(`
A: active, initiate
B: reflective, deliberate
			`);
		
		let userOutput = prompt("choose A or B: ");

		userOutput = userOutput.toUpperCase();

		if (userOutput === 'A') {

			extroCount++;
			responses[count++] = 'A: active, initiate';
			break;

		} else if (userOutput === 'B') {
			introCount++;
			responses[count++] = 'B: reflective, deliberate';
			break;

		} else {
			console.log('Expected A or B as response');
			console.log('I know this is an error please try again');
			continue;
		}


	}



	console.log(`Hello ${name}. You seleted: `);

	for (let ans = 0; ans < responses.length; ans++) {

		console.log(`${responses[ans]}`);
	}

	console.log(`Number of A selected is: ${extroCount}`);
	console.log(`Number of B selected is: ${introCount}`);

	if (extroCount > introCount) {
		return "E";
	
	} else {

		return "I";
	}


} 







function sensingIntuitive(name) {

	let sensingCount = 0;
	let intuitiveCount = 0;
	let responses = [];
	let count = 0;

	while (true) {

		console.log(`
A: Interpret literally
B: look for meaning and possibilities	
		`)

		let result = prompt('choose A or B: ');

		result = result.toUpperCase();

		if (result === 'A') {
			sensingCount++;
			responses[count++] = 'A: Interpret literally';
			break;

		} else if (result === 'B') {
			intuitiveCount++;
			responses[count++] = 'B: look for meaning and possibilities';
			break

		} else {
			console.log('Expected A or B as response');
			console.log('I know this is an error please try again');
			continue;
		}
	}


	while (true) {

		console.log(`
A: practical, realistic, experiential
B: imaginative, innovative, theoretical	
			`);
		
		let userInput = prompt("choose A or B: ");

		userInput = userInput.toUpperCase();

		if (userInput === 'A') {

			sensingCount++;
			responses[count++] = 'A: practical, realistic, experiential';
			break;

		} else if (userInput === 'B') {
			intuitiveCount++;
			responses[count++] = 'B: imaginative, innovative, theoretical';
			break;

		} else {
			console.log('Expected A or B as response')
			console.log('I know this is an error please try again')
			continue;
		}


	}




	while (true) {

        console.log(`
A: standard, usual, conventional
B: different, novel, unique
			`);
		
		let answer = prompt("choose A or B: ");

		answer = answer.toUpperCase();

		if (answer === 'A') {

			sensingCount++;
			responses[count++] = 'A: standard, usual, conventional';
			break;

		} else if (answer === 'B') {
			intuitiveCount++;
			responses[count++] = 'B: different, novel, unique';
			break;
		} else {
			console.log('Expected A or B as response')
			console.log('I know this is an error please try again')
			continue;
		}


	}



	while (true) {

        console.log(`
A: focus on here-and-now
B: look to the future, global perspective, big picture	
			`);
		
		let choice = prompt("choose A or B: ");

		choice = choice.toUpperCase();

		if (choice === 'A') {

			sensingCount++;
			responses[count++] = 'A: focus on here-and-now';
			break;

		} else if (choice === 'B') {
			intuitiveCount++;
			responses[count++] = 'B: look to the future, global perspective, big picture';
			break;

		} else {
			console.log('Expected A or B as response')
			console.log('I know this is an error please try again')
			continue;
		}


	}





	while (true) {

        console.log(`
A: facts, things, what is
B: ideas, dreams, what could be, philosophical	
			`);
		
		let userOutput = prompt("choose A or B: ");

		userOutput = userOutput.toUpperCase();

		if (userOutput === 'A') {

			sensingCount++;
			responses[count++] = 'A: facts, things, what is';
			break;

		} else if (userOutput === 'B') {
			intuitiveCount++;
			responses[count++] = 'B: ideas, dreams, what could be, philosophical';
			break;

		} else {
			console.log('Expected A or B as response');
			console.log('I know this is an error please try again');
			continue;
		}


	}



	console.log(`Hello ${name}. You seleted: `);

	for (let ans = 0; ans < responses.length; ans++) {

		console.log(`${responses[ans]}`);
	}

	console.log(`Number of A selected is: ${sensingCount}`);
	console.log(`Number of B selected is: ${intuitiveCount}`);

	if (sensingCount > intuitiveCount) {
		return "S";
	
	} else {

		return "N";

	}
	
} 





function thinkingFeeling(name) {

	let thinkingCount = 0;
	let feelingCount = 0;
	let responses = [];
	let count = 0;

	while (true) {

		console.log(`
A: logical, thinking, questioning
B: empathetic, feeling, accommodating
		`)

		let result = prompt('choose A or B: ');

		result = result.toUpperCase();

		if (result === 'A') {
			thinkingCount++;
			responses[count++] = 'A: logical, thinking, questioning';
			break;

		} else if (result === 'B') {
			feelingCount++;
			responses[count++] = 'B: empathetic, feeling, accommodating';
			break

		} else {
			console.log('Expected A or B as response');
			console.log('I know this is an error please try again');
			continue;
		}
	}


	while (true) {

		console.log(`
A: candid, straight forward, frank
B: tactful, kind, encouraging
			`);
		
		let userInput = prompt("choose A or B: ");

		userInput = userInput.toUpperCase();

		if (userInput === 'A') {

			thinkingCount++;
			responses[count++] = 'A: candid, straight forward, frank';
			break;

		} else if (userInput === 'B') {
			feelingCount++;
			responses[count++] = 'B: tactful, kind, encouraging';
			break;

		} else {
			console.log('Expected A or B as response')
			console.log('I know this is an error please try again')
			continue;
		}


	}




	while (true) {

        console.log(`
A: firm, tend to criticise, hold the line
B: gentle, tend to appreciate, conciliate
			`);
		
		let answer = prompt("choose A or B: ");

		answer = answer.toUpperCase();

		if (answer === 'A') {

			thinkingCount++;
			responses[count++] = 'A: firm, tend to criticise, hold the line';
			break;

		} else if (answer === 'B') {
			feelingCount++;
			responses[count++] = 'B: gentle, tend to appreciate, conciliate';
			break;
		} else {
			console.log('Expected A or B as response')
			console.log('I know this is an error please try again')
			continue;
		}


	}



	while (true) {

        console.log(`
A: tough-minded, just
B: tender-hearted, merciful
			`);
		
		let choice = prompt("choose A or B: ");

		choice = choice.toUpperCase();

		if (choice === 'A') {

			thinkingCount++;
			responses[count++] = 'A: tough-minded, just';
			break;

		} else if (choice === 'B') {
			feelingCount++;
			responses[count++] = 'B: tender-hearted, merciful';
			break;

		} else {
			console.log('Expected A or B as response')
			console.log('I know this is an error please try again')
			continue;
		}


	}





	while (true) {

        console.log(`
A: matter of fact, issue-oriented
B: sensitive, people-oriented, compassionate	
			`);
		
		let userOutput = prompt("choose A or B: ");

		userOutput = userOutput.toUpperCase();

		if (userOutput === 'A') {

			thinkingCount++;
			responses[count++] = 'A: matter of fact, issue-oriented';
			break;

		} else if (userOutput === 'B') {
			feelingCount++;
			responses[count++] = 'B: sensitive, people-oriented, compassionate';
			break;

		} else {
			console.log('Expected A or B as response');
			console.log('I know this is an error please try again');
			continue;
		}


	}



	console.log(`Hello ${name}. You seleted: `);

	for (let ans = 0; ans < responses.length; ans++) {

		console.log(`${responses[ans]}`);
	}

	console.log(`Number of A selected is: ${thinkingCount}`);
	console.log(`Number of B selected is: ${feelingCount}`);

	if (thinkingCount > feelingCount) {
		return "T";
	
	} else {

		return "F";
	}


} 







function judgingPerceptive(name) {

	let judgingCount = 0;
	let percepCount = 0;
	let responses = [];
	let count = 0;

	while (true) {

		console.log(`
A: organised, orderly
B: flexible, adaptable
		`)

		let result = prompt('choose A or B: ');

		result = result.toUpperCase();

		if (result === 'A') {
			judgingCount++;
			responses[count++] = 'A: organised, orderly';
			break;

		} else if (result === 'B') {
			percepCount++;
			responses[count++] = 'B: flexible, adaptable';
			break

		} else {
			console.log('Expected A or B as response');
			console.log('I know this is an error please try again');
			continue;
		}
	}


	while (true) {

		console.log(`
A: plan, schedule
B: unplanned, spontaneous
			`);
		
		let userInput = prompt("choose A or B: ");

		userInput = userInput.toUpperCase();

		if (userInput === 'A') {

			judgingCount++;
			responses[count++] = 'A: plan, schedule';
			break;

		} else if (userInput === 'B') {
			percepCount++;
			responses[count++] = 'B: unplanned, spontaneous';
			break;

		} else {
			console.log('Expected A or B as response')
			console.log('I know this is an error please try again')
			continue;
		}


	}




	while (true) {

        console.log(`
A: regulated, structured
B: easy-going, live and let live
			`);
		
		let answer = prompt("choose A or B: ");

		answer = answer.toUpperCase();

		if (answer === 'A') {

			judgingCount++;
			responses[count++] = 'A: regulated, structured';
			break;

		} else if (answer === 'B') {
			percepCount++;
			responses[count++] = 'B: easy-going, live and let live';
			break;
		} else {
			console.log('Expected A or B as response')
			console.log('I know this is an error please try again')
			continue;
		}


	}



	while (true) {

        console.log(`
A: preparation, plan ahead
B: go with the flow, adapt as you go
			`);
		
		let choice = prompt("choose A or B: ");

		choice = choice.toUpperCase();

		if (choice === 'A') {

			judgingCount++;
			responses[count++] = 'A: preparation, plan ahead';
			break;

		} else if (choice === 'B') {
			percepCount++;
			responses[count++] = 'B: go with the flow, adapt as you go';
			break;

		} else {
			console.log('Expected A or B as response')
			console.log('I know this is an error please try again')
			continue;
		}


	}





	while (true) {

        console.log(`
A: control, govern
B: latitude, freedom	
	`);
		
		let userOutput = prompt("choose A or B: ");

		userOutput = userOutput.toUpperCase();

		if (userOutput === 'A') {

			judgingCount++;
			responses[count++] = 'A: control, govern';
			break;

		} else if (userOutput === 'B') {
			percepCount++;
			responses[count++] = 'B: latitude, freedom';
			break;

		} else {
			console.log('Expected A or B as response');
			console.log('I know this is an error please try again');
			continue;
		}


	}



	console.log(`Hello ${name}. You seleted: `);

	for (let ans = 0; ans < responses.length; ans++) {

		console.log(`${responses[ans]}`);
	}

	console.log(`Number of A selected is: ${judgingCount}`);
	console.log(`Number of B selected is: ${percepCount}`);

	if (judgingCount > percepCount) {
		return "J";
	
	} else {

		return "P";

	}

} 





function mbtiDescription(mbti) {


	switch(mbti) {


		case "ISTJ":

			return (`ISTJ: ISTJ (Logistician) is a personality type with the Introverted, Observant, Thinking, and Judging traits. These people tend to be reserved yet willful, with a rational outlook on life.  They compose their actions carefully and carry them out with methodical purpose."
People with the ISTJ personality type (Logisticians) mean what they say and say what they mean, and when they commit to doing something, they make sure to follow through. With their responsible and dependable nature, it might not be so surprising that ISTJ personalities also tend to have a deep respect for structure and tradition. They are often drawn to organizations, workplaces, and educational settings that offer clear hierarchies and expectations.
While ISTJs may not be particularly flashy or attention seeking, they do more than their share to keep society on a sturdy, stable foundation. In their families and their communities, people with this personality type often earn respect for their reliability, their practicality, and their ability to stay grounded and logical in even the most stressful situation.`)




		case "ISFJ":

			return (`ISFJ: ISFJ (Defender) is a personality type with the Introverted, Observant, Feeling, and Judging traits. These people tend to be warm and unassuming in their own steady way. They’re efficient and responsible, giving careful attention to practical details in their daily lives.
One of the greatest ISFJ strengths is loyalty. They rarely allow a friendship or relationship to fade away from lack of effort. Instead, they invest a great deal of energy into maintaining strong connections with their loved ones – and not just by sending “How are you doing?” texts. People with this personality type are known for dropping everything and lending a hand whenever a friend or family member is going through a hard time.`)



		case "INFJ":

			return (`INFJ: INFJ (Advocate) is a personality type with the Introverted, Intuitive, Feeling, and Judging traits. They tend to approach life with deep thoughtfulness and imagination. Their inner vision, personal values, and a quiet, principled version of humanism guide them in all things.
Idealistic and principled, people with the INFJ personality type (Advocates) aren’t content to coast through life – they want to stand up and make a difference. For these compassionate personalities, success doesn’t come from money or status but from seeking fulfillment, helping others, and being a force for good in the world.`)



		case "INTJ":

			return (`INTJ: INTJ (Architect) is a personality type with the Introverted, Intuitive, Thinking, and Judging traits. These thoughtful tacticians love perfecting the details of life, applying creativity and rationality to everything they do. Their inner world is often a private, complex one.
People with the INTJ personality type (Architects) are intellectually curious individuals with a deep-seated thirst for knowledge. INTJs tend to value creative ingenuity, straightforward rationality, and self-improvement. They consistently work toward enhancing intellectual abilities and are often driven by an intense desire to master any and every topic that piques their interest.`)




		case "ISTP":

			return (`ISTP: ISTP (Virtuoso) is a personality type with the Introverted, Observant, Thinking, and Prospecting traits. They tend to have an individualistic mindset, pursuing goals without needing much external connection. They engage in life with inquisitiveness and personal skill, varying their approach as needed.
People with the ISTP personality type (Virtuosos) love to explore with their hands and their eyes, touching and examining the world around them with an impressive diligence, a casual curiosity, and a healthy dose of skepticism.`)




		case "ISFP":

			return (`ISFP: ISFP (Adventurer) is a personality type with the Introverted, Observant, Feeling, and Prospecting traits. They tend to have open minds, approaching life, new experiences, and people with grounded warmth. Their ability to stay in the moment helps them uncover exciting potentials.
"People with the ISFP personality type (Adventurers) are true artists – although not necessarily in the conventional sense. For these types, life itself is a canvas for self-expression. From what they wear to how they spend their free time, they act in ways that vividly reflect who they are as unique individuals. With their exploratory spirit and their ability to find joy in everyday life, ISFPs can be among the most interesting people you’ll ever meet.`)




		case "INFP":

			return (`INFP: INFP (Mediator) is a personality type with the Introverted, Intuitive, Feeling, and Prospecting traits. These rare personality types tend to be quiet, open-minded, and imaginative, and they apply a caring and creative approach to everything they do.
Although they may seem quiet or unassuming, people with the INFP personality type (Mediators) have vibrant, passionate inner lives. Creative and imaginative, they happily lose themselves in daydreams, inventing all sorts of stories and conversations in their mind.
INFPs are known for their sensitivity – these personalities can have profound emotional responses to music, art, nature, and the people around them. They are known to be extremely sentimental and nostalgic, often holding onto special keepsakes and memorabilia that brighten their days and fill their heart with joy.`)




		case "INTP":

			return (`INTP: INTP (Logician) is a personality type with the Introverted, Intuitive, Thinking, and Prospecting traits. These flexible thinkers enjoy taking an unconventional approach to many aspects of life. They often seek out unlikely paths, mixing willingness to experiment with personal creativity.
People with the INTP personality type (Logicians) pride themselves on their unique perspective and vigorous intellect. They can’t help but puzzle over the mysteries of the universe – which may explain why some of the most influential philosophers and scientists of all time have been INTPs.`)



		case "ESTP":

			return (`ESTP: ESTP (Entrepreneur) is a personality type with the Extraverted, Observant, Thinking, and Prospecting traits. They tend to be energetic and action-oriented, deftly navigating whatever is in front of them. They love uncovering life’s opportunities, whether socializing with others or in more personal pursuits.
People with the ESTP personality type (Entrepreneurs) are vibrant individuals brimming with an enthusiastic and spontaneous energy. They tend to be on the competitive side, often assuming that a competitive mindset is a necessity in order to achieve success in life. With their driven, action-oriented attitudes, they rarely waste time thinking about the past. In fact, they excel at keeping their attention rooted in their present – so much so that they rarely find themselves fixated on the time throughout the day.`)




		case "ESFP":

			return (`ESFP: ESFP (Entertainer) is a personality type with the Extraverted, Observant, Feeling, and Prospecting traits. These people love vibrant experiences, engaging in life eagerly and taking pleasure in discovering the unknown. They can be very social, often encouraging others into shared activities.
If anyone is to be found spontaneously breaking into song and dance, it is people with the ESFP personality type (Entertainers). They get caught up in the excitement of the moment and want everyone else to feel that way too. No other type is as generous with their time and energy when it comes to encouraging others, and no other type does it with such irresistible style.`)





		case "ENFP":

			return (`ENFP: ENFP (Campaigner) is a personality type with the Extraverted, Intuitive, Feeling, and Prospecting traits. These people tend to embrace big ideas and actions that reflect their sense of hope and goodwill toward others. Their vibrant energy can flow in many directions.
People with the ENFP personality type (Campaigners) are true free spirits – outgoing, openhearted, and open-minded. With their lively, upbeat approach to life, ENFPs stand out in any crowd. But even though they can be the life of the party, they don’t just care about having a good time. These personalities have profound depths that are fueled by their intense desire for meaningful, emotional connections with others.`)





		case "ENTP":

			return (`ENTP: ENTP (Debater) is a personality type with the Extraverted, Intuitive, Thinking, and Prospecting traits. They tend to be bold and creative, deconstructing and rebuilding ideas with great mental agility. They pursue their goals vigorously despite any resistance they might encounter.
Quick-witted and audacious, people with the ENTP personality type (Debaters) aren’t afraid to disagree with the status quo. In fact, they’re not afraid to disagree with pretty much anything or anyone. Few things light up these personalities more than a bit of verbal sparring – and if the conversation veers into controversial terrain, so much the better.
It would be a mistake, though, to think of ENTPs as disagreeable or mean-spirited. Instead, people with this personality type are knowledgeable and curious with a playful sense of humor, and they can be incredibly entertaining.`)




		case "ESTJ":

			return (`ESTJ: ESTJ (Executive) is a personality type with the Extraverted, Observant, Thinking, and Judging traits. They possess great fortitude, emphatically following their own sensible judgment. They often serve as a stabilizing force among others, able to offer solid direction amid adversity.
ESTJs are classic images of the model citizen:  they help their neighbors, uphold the law, and try to make sure that everyone participates in the communities and organizations that they hold so dear.`)





		case "ESFJ":

			return (`ESFJ: ESFJ (Consul) is a personality type with the Extraverted, Observant, Feeling, and Judging traits. They are attentive and people-focused, and they enjoy taking part in their social community. Their achievements are guided by decisive values, and they willingly offer guidance to others.
For people with the ESFJ personality type (Consuls), life is sweetest when it’s shared with others. These social individuals form the bedrock of many communities, opening their homes – and their hearts – to friends, loved ones, and neighbors.`);




		case "ENFJ":

			return (`ENFJ: ENFJ (Protagonist) is a personality type with the Extraverted, Intuitive, Feeling, and Judging traits. These warm, forthright types love helping others, and they tend to have strong ideas and values. They back their perspective with the creative energy to achieve their goals.
People with the ENFJ personality type (Protagonists) feel called to serve a greater purpose in life. Thoughtful and idealistic, ENFJs strive to have a positive impact on other people and the world around them. These personalities rarely shy away from an opportunity to do the right thing, even when doing so is far from easy.`);




		case "ENTJ":

			return (`ENTJ: ENTJ (Commander) is a personality type with the Extraverted, Intuitive, Thinking, and Judging traits. They are decisive people who love momentum and accomplishment. They gather information to construct their creative visions but rarely hesitate for long before acting on them.
Their intensity might sometimes rub people the wrong way, but ultimately, ENTJs take pride in both their work ethic and their impressive level of self-discipline.ENTJs respect those who can match them intellectually and also display precision and quality in their actions, equal to their own. These personalities have a particular skill in recognizing the talents of others, and this helps in their team-building efforts (since no one, no matter how brilliant, can do everything alone). However, they also have a particular skill in calling out others’ failures with a chilling degree of insensitivity, and this is where they really start to run into trouble.`);



		case _:
		
			return "Description not found for this MBTI type.";


	}
}









let name = prompt("What is your name: ");


let extroIntro = extrovertIntrovert(name);

let senseIntuit = sensingIntuitive(name);

let thinkFeel = thinkingFeeling(name);

let judgePercep = judgingPerceptive(name);


let mbtiTog = extroIntro + senseIntuit + thinkFeel + judgePercep;

let description = mbtiDescription(mbtiTog);


console.log(`Your MBTI personality type is: ${mbtiTog}`);

console.log(`${description}`);