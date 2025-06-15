def extrovert_introvert(name):

	extro_count = 0
	intro_count = 0
	responses = []	

	while True:

		print("""
A: expand energy, enjoy groups
B: conserve energy, enjoy one-on-ones	
			""")	

		result = str(input('choose A or B: '))

		result = result.upper()

		if result == 'A':
			extro_count += 1
			responses.append('A: expand energy, enjoy groups')
			break

		if result == 'B':
			intro_count += 1
			responses.append('B: conserve energy, enjoy one-on-ones')
			break
		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue



	while True:

		print("""
A: more outgoing, thinking loud
B: more reserved, thinking to yourself		
			""")
		
		user_input = str(input('choose A or B: '))

		user_input = user_input.upper()

		if user_input == 'A':
			extro_count += 1
			responses.append('A: more outgoing, thinking loud')
			break

		if user_input == 'B':
			intro_count += 1
			responses.append('B: more reserved, thinking to yourself')
			break
		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue


		
	while True:

		print("""
A: seek many tasks, public activities, interaction with others
B: seek private, solitary activities with quiet to concentrate	
			""")

		choice = str(input('choose A or B: '))

		choice = choice.upper()

		if choice == 'A':
			extro_count += 1
			responses.append('A: seek many tasks, public activities, interaction with others')
			break

		if choice == 'B':
			intro_count += 1
			responses.append('B: seek private, solitary activities with quiet to concentrate')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue


	while True:

		print("""
A: external, communicative, express yourself
B: internal, reticent, keep to yourself		
			""")

		answer = str(input('choose A or B: '))

		answer = answer.upper()

		if answer == 'A':
			extro_count += 1
			responses.append('A: external, communicative, express yourself')
			break

		if answer == 'B':
			intro_count += 1
			responses.append('B: internal, reticent, keep to yourself')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue

	while True:

		print("""
A: active, initiate
B: reflective, deliberate	
			""")

		output = str(input('choose A or B: '))

		output = output.upper()

		if output == 'A':
			extro_count += 1
			responses.append('A: active, initiate')
			break

		if output == 'B':
			intro_count += 1
			responses.append('B: reflective, deliberate')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue

			

	print()
	print(f'Hello {name}. You selected: ')
	
	for ans in responses:

		print(f'{ans}')

	print()	
	print(f'Number of A selected is: {extro_count}')

	print(f'Number of B selected is: {intro_count}')

	if extro_count > intro_count:
	
		return 'E'
	else:
		return 'I'




def sensing_intuitive(name):

	
	sensing_count = 0
	intuitive_count = 0
	responses = []
	
	while True:

		print("""
A: Interpret literally
B: look for meaning and possibilities	
			""")	

		result = str(input('choose A or B: '))

		result = result.upper()

		if result == 'A':
			sensing_count += 1
			responses.append('A: Interpret literally')
			break

		if result == 'B':
			intuitive_count += 1
			responses.append('B: look for meaning and possibilities')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue

	while True:

		print("""
A: practical, realistic, experiential
B: imaginative, innovative, theoretical	
			""")

		user_input = str(input('choose A or B: '))

		user_input = user_input.upper()

		if user_input == 'A':
			sensing_count += 1
			responses.append('A: practical, realistic, experiential')
			break

		if user_input == 'B':
			intuitive_count += 1
			responses.append('B: imaginative, innovative, theoretical')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue

	while True:

		print("""
A: standard, usual, conventional
B: different, novel, unique	
			""")
		
		choice = str(input('choose A or B: '))

		choice = choice.upper()

		if choice == 'A':
			sensing_count += 1
			responses.append('A: standard, usual, conventional')
			break

		if choice == 'B':
			intuitive_count += 1
			responses.append('B: different, novel, unique')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue
		
	while True:

		print("""
A: focus on here-and-now
B: look to the future, global perspective, big picture	
			""")

		answer = str(input('choose A or B: '))

		answer = answer.upper()

		if answer == 'A':
			sensing_count += 1
			responses.append('A: focus on here-and-now')
			break

		if answer == 'B':
			intuitive_count += 1
			responses.append('B: look to the future, global perspective, big picture')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue

	while True:

		print("""
A: facts, things, what is
B: ideas, dreams, what could be, philosophical		
			""")

		output = str(input('choose A or B: '))

		output = output.upper()

		if output == 'A':
			sensing_count += 1
			responses.append('A: facts, things, what is')
			break

		if output == 'B':
			intuitive_count += 1
			responses.append('B: ideas, dreams, what could be, philosophical')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue



	print(f'Hello {name}. You selected: ')
	
	for ans in responses:

		print(f'{ans}')
		
	print(f'Number of A selected is: {sensing_count}')

	print(f'Number of B selected is: {intuitive_count}')

	if sensing_count > intuitive_count:

		return 'S'
	else:
		return 'N'


	
	

def thinking_feeling(name):

	
	thinking_count = 0
	feeling_count = 0
	responses = []
	
	while True:

		print("""
A: logical, thinking, questioning
B: empathetic, feeling, accommodating
			""")	

		result = str(input('choose A or B: '))

		result = result.upper()

		if result == 'A':
			thinking_count += 1
			responses.append('A: logical, thinking, questioning')
			break

		if result == 'B':
			feeling_count += 1
			responses.append('B: empathetic, feeling, accommodating')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue

	while True:

		print("""
A: candid, straight forward, frank
B: tactful, kind, encouraging
			""")

		user_input = str(input('choose A or B: '))

		user_input = user_input.upper()

		if user_input == 'A':
			thinking_count += 1
			responses.append('A: candid, straight forward, frank')
			break

		if user_input == 'B':
			feeling_count += 1
			responses.append('B: tactful, kind, encouraging')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue

	while True:

		print("""
A: firm, tend to criticise, hold the line
B: gentle, tend to appreciate, conciliate	
			""")
		
		choice = str(input('choose A or B: '))

		choice = choice.upper()

		if choice == 'A':
			thinking_count += 1
			responses.append('A: firm, tend to criticise, hold the line')
			break

		if choice == 'B':
			feeling_count += 1
			responses.append('B: gentle, tend to appreciate, conciliate')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue
		

	while True:

		print("""
A: tough-minded, just
B: tender-hearted, merciful
			""")

		answer = str(input('choose A or B: '))

		answer = answer.upper()

		if answer == 'A':
			thinking_count += 1
			responses.append('A: tough-minded, just')
			break

		if answer == 'B':
			feeling_count += 1
			responses.append('B: tender-hearted, merciful')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue

	while True:

		print("""
A: matter of fact, issue-oriented
B: sensitive, people-oriented, compassionate		
			""")

		output = str(input('choose A or B: '))

		output = output.upper()

		if output == 'A':
			thinking_count += 1
			responses.append('A: matter of fact, issue-oriented')
			break

		if output == 'B':
			feeling_count += 1
			responses.append('B: sensitive, people-oriented, compassionate')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue


	print(f'Hello {name}. You selected: ')
	
	for ans in responses:

		print(f' {ans}')
		
	print(f'Number of A selected is: {thinking_count}')

	print(f'Number of B selected is: {feeling_count}')

	if thinking_count > feeling_count:

		return 'T'
	else:
		return 'F'


	


def judging_percerptive(name):


	judging_count = 0
	percerp_count = 0
	responses = []
	
	while True:

		print("""
A: organised, orderly
B: flexible, adaptable
			""")	

		result = str(input('choose A or B: '))

		result = result.upper()

		if result == 'A':
			judging_count += 1
			responses.append('A: organised, orderly')
			break

		if result == 'B':
			percerp_count += 1
			responses.append('B: flexible, adaptable')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue

	while True:

		print("""
A: plan, schedule
B: unplanned, spontaneous
			""")

		user_input = str(input('choose A or B: '))

		user_input = user_input.upper()

		if user_input == 'A':
			judging_count += 1
			responses.append('A: plan, schedule')
			break

		if user_input == 'B':
			percerp_count += 1
			responses.append('B: unplanned, spontaneous')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue

	while True:

		print("""
A: regulated, structured
B: easy-going, live and let live	
			""")
		
		choice = str(input('choose A or B: '))

		choice = choice.upper()

		if choice == 'A':
			judging_count += 1
			responses.append('A: regulated, structured')
			break

		if choice == 'B':
			percerp_count += 1
			responses.append('B: easy-going, live and let live')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue
		

	while True:

		print("""
A: preparation, plan ahead
B: go with the flow, adapt as you go
			""")

		answer = str(input('choose A or B: '))

		answer = answer.upper()

		if answer == 'A':
			judging_count += 1
			responses.append('A: preparation, plan ahead')
			break

		if answer == 'B':
			percerp_count += 1
			responses.append('B: go with the flow, adapt as you go')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue


	while True:

		print("""
A: control, govern
B: latitude, freedom		
			""")

		output = str(input('choose A or B: '))

		output = output.upper()

		if output == 'A':
			judging_count += 1
			responses.append('A: control, govern')
			break

		if output == 'B':
			percerp_count += 1
			responses.append('B: latitude, freedom')
			break

		else:
			print('Expected A or B as response')
			print('I know this is an error please try again')
			continue
	

	print(f'Hello {name}. You selected: ')
	
	for ans in responses:

		print(f' {ans}')
		
	print(f'Number of A selected is: {judging_count}')

	print(f'Number of B selected is: {percerp_count}')

	if judging_count > percerp_count:
	
		return 'J'
	else:
 
		return 'P'	




def mbti_description(m_b_t_i):


	match m_b_t_i:

		case "ISTJ":

			return ("""ISTJ: ISTJ (Logistician) is a personality type with the Introverted, Observant, Thinking, and Judging traits. These people tend to be reserved yet willful, with a rational outlook on life.  They compose their actions carefully and carry them out with methodical purpose."
People with the ISTJ personality type (Logisticians) mean what they say and say what they mean, and when they commit to doing something, they make sure to follow through. With their responsible and dependable nature, it might not be so surprising that ISTJ personalities also tend to have a deep respect for structure and tradition. They are often drawn to organizations, workplaces, and educational settings that offer clear hierarchies and expectations.
While ISTJs may not be particularly flashy or attention seeking, they do more than their share to keep society on a sturdy, stable foundation. In their families and their communities, people with this personality type often earn respect for their reliability, their practicality, and their ability to stay grounded and logical in even the most stressful situation.""")


		case "ISFJ":

			return ("""ISFJ: ISFJ (Defender) is a personality type with the Introverted, Observant, Feeling, and Judging traits. These people tend to be warm and unassuming in their own steady way. They’re efficient and responsible, giving careful attention to practical details in their daily lives.
One of the greatest ISFJ strengths is loyalty. They rarely allow a friendship or relationship to fade away from lack of effort. Instead, they invest a great deal of energy into maintaining strong connections with their loved ones – and not just by sending “How are you doing?” texts. People with this personality type are known for dropping everything and lending a hand whenever a friend or family member is going through a hard time.""")

		case "INFJ":

			return ("""INFJ: INFJ (Advocate) is a personality type with the Introverted, Intuitive, Feeling, and Judging traits. They tend to approach life with deep thoughtfulness and imagination. Their inner vision, personal values, and a quiet, principled version of humanism guide them in all things.
Idealistic and principled, people with the INFJ personality type (Advocates) aren’t content to coast through life – they want to stand up and make a difference. For these compassionate personalities, success doesn’t come from money or status but from seeking fulfillment, helping others, and being a force for good in the world.""")

		case "INTJ":

			return ("""INTJ: INTJ (Architect) is a personality type with the Introverted, Intuitive, Thinking, and Judging traits. These thoughtful tacticians love perfecting the details of life, applying creativity and rationality to everything they do. Their inner world is often a private, complex one.
People with the INTJ personality type (Architects) are intellectually curious individuals with a deep-seated thirst for knowledge. INTJs tend to value creative ingenuity, straightforward rationality, and self-improvement. They consistently work toward enhancing intellectual abilities and are often driven by an intense desire to master any and every topic that piques their interest.""")

		case "ISTP":

			return ("""ISTP: ISTP (Virtuoso) is a personality type with the Introverted, Observant, Thinking, and Prospecting traits. They tend to have an individualistic mindset, pursuing goals without needing much external connection. They engage in life with inquisitiveness and personal skill, varying their approach as needed.
People with the ISTP personality type (Virtuosos) love to explore with their hands and their eyes, touching and examining the world around them with an impressive diligence, a casual curiosity, and a healthy dose of skepticism.""")

		case "ISFP":

			return ("""ISFP: ISFP (Adventurer) is a personality type with the Introverted, Observant, Feeling, and Prospecting traits. They tend to have open minds, approaching life, new experiences, and people with grounded warmth. Their ability to stay in the moment helps them uncover exciting potentials.
"People with the ISFP personality type (Adventurers) are true artists – although not necessarily in the conventional sense. For these types, life itself is a canvas for self-expression. From what they wear to how they spend their free time, they act in ways that vividly reflect who they are as unique individuals. With their exploratory spirit and their ability to find joy in everyday life, ISFPs can be among the most interesting people you’ll ever meet.""")

		case "INFP":

			return ("""INFP: INFP (Mediator) is a personality type with the Introverted, Intuitive, Feeling, and Prospecting traits. These rare personality types tend to be quiet, open-minded, and imaginative, and they apply a caring and creative approach to everything they do.
Although they may seem quiet or unassuming, people with the INFP personality type (Mediators) have vibrant, passionate inner lives. Creative and imaginative, they happily lose themselves in daydreams, inventing all sorts of stories and conversations in their mind.
INFPs are known for their sensitivity – these personalities can have profound emotional responses to music, art, nature, and the people around them. They are known to be extremely sentimental and nostalgic, often holding onto special keepsakes and memorabilia that brighten their days and fill their heart with joy.""")

		case "INTP":

			return ("""INTP: INTP (Logician) is a personality type with the Introverted, Intuitive, Thinking, and Prospecting traits. These flexible thinkers enjoy taking an unconventional approach to many aspects of life. They often seek out unlikely paths, mixing willingness to experiment with personal creativity.
People with the INTP personality type (Logicians) pride themselves on their unique perspective and vigorous intellect. They can’t help but puzzle over the mysteries of the universe – which may explain why some of the most influential philosophers and scientists of all time have been INTPs.""")

		case "ESTP":

			return ("""ESTP: ESTP (Entrepreneur) is a personality type with the Extraverted, Observant, Thinking, and Prospecting traits. They tend to be energetic and action-oriented, deftly navigating whatever is in front of them. They love uncovering life’s opportunities, whether socializing with others or in more personal pursuits.
People with the ESTP personality type (Entrepreneurs) are vibrant individuals brimming with an enthusiastic and spontaneous energy. They tend to be on the competitive side, often assuming that a competitive mindset is a necessity in order to achieve success in life. With their driven, action-oriented attitudes, they rarely waste time thinking about the past. In fact, they excel at keeping their attention rooted in their present – so much so that they rarely find themselves fixated on the time throughout the day.""")

		case "ESFP":

			return ("""ESFP: ESFP (Entertainer) is a personality type with the Extraverted, Observant, Feeling, and Prospecting traits. These people love vibrant experiences, engaging in life eagerly and taking pleasure in discovering the unknown. They can be very social, often encouraging others into shared activities.
If anyone is to be found spontaneously breaking into song and dance, it is people with the ESFP personality type (Entertainers). They get caught up in the excitement of the moment and want everyone else to feel that way too. No other type is as generous with their time and energy when it comes to encouraging others, and no other type does it with such irresistible style.""")

		case "ENFP":

			return ("""ENFP: ENFP (Campaigner) is a personality type with the Extraverted, Intuitive, Feeling, and Prospecting traits. These people tend to embrace big ideas and actions that reflect their sense of hope and goodwill toward others. Their vibrant energy can flow in many directions.
People with the ENFP personality type (Campaigners) are true free spirits – outgoing, openhearted, and open-minded. With their lively, upbeat approach to life, ENFPs stand out in any crowd. But even though they can be the life of the party, they don’t just care about having a good time. These personalities have profound depths that are fueled by their intense desire for meaningful, emotional connections with others.""")

		case "ENTP":

			return ("""ENTP: ENTP (Debater) is a personality type with the Extraverted, Intuitive, Thinking, and Prospecting traits. They tend to be bold and creative, deconstructing and rebuilding ideas with great mental agility. They pursue their goals vigorously despite any resistance they might encounter.
Quick-witted and audacious, people with the ENTP personality type (Debaters) aren’t afraid to disagree with the status quo. In fact, they’re not afraid to disagree with pretty much anything or anyone. Few things light up these personalities more than a bit of verbal sparring – and if the conversation veers into controversial terrain, so much the better.
It would be a mistake, though, to think of ENTPs as disagreeable or mean-spirited. Instead, people with this personality type are knowledgeable and curious with a playful sense of humor, and they can be incredibly entertaining.""")

		case "ESTJ":

			return ("""ESTJ: ESTJ (Executive) is a personality type with the Extraverted, Observant, Thinking, and Judging traits. They possess great fortitude, emphatically following their own sensible judgment. They often serve as a stabilizing force among others, able to offer solid direction amid adversity.
ESTJs are classic images of the model citizen:  they help their neighbors, uphold the law, and try to make sure that everyone participates in the communities and organizations that they hold so dear.""")

		case "ESFJ":

			return ("""ESFJ: ESFJ (Consul) is a personality type with the Extraverted, Observant, Feeling, and Judging traits. They are attentive and people-focused, and they enjoy taking part in their social community. Their achievements are guided by decisive values, and they willingly offer guidance to others.
For people with the ESFJ personality type (Consuls), life is sweetest when it’s shared with others. These social individuals form the bedrock of many communities, opening their homes – and their hearts – to friends, loved ones, and neighbors.""")

		case "ENFJ":

			return ("""ENFJ: ENFJ (Protagonist) is a personality type with the Extraverted, Intuitive, Feeling, and Judging traits. These warm, forthright types love helping others, and they tend to have strong ideas and values. They back their perspective with the creative energy to achieve their goals.
People with the ENFJ personality type (Protagonists) feel called to serve a greater purpose in life. Thoughtful and idealistic, ENFJs strive to have a positive impact on other people and the world around them. These personalities rarely shy away from an opportunity to do the right thing, even when doing so is far from easy.""")
		
		case "ENTJ":

			return ("""ENTJ: ENTJ (Commander) is a personality type with the Extraverted, Intuitive, Thinking, and Judging traits. They are decisive people who love momentum and accomplishment. They gather information to construct their creative visions but rarely hesitate for long before acting on them.
Their intensity might sometimes rub people the wrong way, but ultimately, ENTJs take pride in both their work ethic and their impressive level of self-discipline.ENTJs respect those who can match them intellectually and also display precision and quality in their actions, equal to their own. These personalities have a particular skill in recognizing the talents of others, and this helps in their team-building efforts (since no one, no matter how brilliant, can do everything alone). However, they also have a particular skill in calling out others’ failures with a chilling degree of insensitivity, and this is where they really start to run into trouble.""")

		case _:
		
			return "Description not found for this MBTI type."


