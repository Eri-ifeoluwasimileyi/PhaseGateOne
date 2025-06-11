import mbti
from mbti import *

name = str(input('What is your name: '))


extro_intro = extrovert_introvert(name)

sense_intuit = sensing_intuitive(name)

think_feel = thinking_feeling(name)

judge_percerp = judging_perceptive(name)



m_b_t_i = extro_intro + sense_intuit  + think_feel + judge_percerp

description = mbti_description(m_b_t_i)

print()
print(f'Your MBTI personality type is: {m_b_t_i}')

print()
print(description)