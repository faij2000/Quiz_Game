import time

#Welcome to user
print("Welcome to the Simple Quiz Game")
time.sleep(1)

#chances
chances=1
print("You will have",chances,"chance to answer correctly.\nPlease put the alphabet of the answer\n")
time.sleep(2)

#score
score=0

#question 1
question_1=print("1) How many states in India?\n(a) 26\n(b) 21\n(c) 7\n(d) 28\n\n")
answer_1="d"

for i in range(chances):
    answer=input("answer: ")
    if (answer.lower() == answer_1):
        print("correct! GOOD JOB.\n")
        score=score+1
        break
    else:
        print("Incoreect!\n")
        time.sleep(0.5)
        print("The Correct answer is",answer_1,"\n\n")
        
time.sleep(1)

#question 2
question_2=print("2) What is the Capital of India?\n(a) Lucknow \n(b) Hydrabad \n(c) New Delhi\n(d) Chandigarh\n\n")
answer_2="c"

for i in range(chances):
    answer=input("answer: ")
    if (answer.lower() == answer_2):
        print("correct! GOOD JOB.\n")
        score=score+1
        break
    else:
        print("Incoreect!\n")
        time.sleep(0.5)
        print("The Correct answer is",answer_2,"\n\n")

time.sleep(1)

#question 3
question_3=print("3) What is the Capital of Uttar Pradesh?\n(a) Lucknow \n(b) Gorakhpur \n(c) Kanpur\n(d) Sitapur\n\n")
answer_3="a"

for i in range(chances):
    answer=input("answer: ")
    if (answer.lower() == answer_3):
        print("correct! GOOD JOB.\n")
        score=score+1
        break
    else:
        print("Incoreect!\n")
        time.sleep(0.5)
        print("The Correct answer is",answer_3,"\n\n")

time.sleep(1)

#question 4
question_4=print("4) '.MOV' extension refers usually to what kind of file?\n(a) Image file\n(b) Animation/movie file\n(c) Audio file\n(d) MS Office document\n\n")
answer_4="b"

for i in range(chances):
    answer=input("answer: ")
    if (answer.lower() == answer_4):
        print("correct! GOOD JOB.\n")
        score=score+1
        break
    else:
        print("Incoreect!\n")
        time.sleep(0.5)
        print("The Correct answer is",answer_4,"\n\n")
        
time.sleep(1)

#question 5
question_5=print("5) 'OS' Computer abbreviation usually means?\n(a) Order of Signature\n(b) Open Software\n(c) Operating System\n(d) Optical sensor\n\n")
answer_5="c"

for i in range(chances):
    answer=input("answer: ")
    if (answer.lower() == answer_5):
        print("correct! GOOD JOB.\n")
        score=score+1
        break
    else:
        print("Incoreect!\n")
        time.sleep(0.5)
        print("The Correct answer is",answer_5,"\n\n")
        
time.sleep(1)

#print the score
while score>=2:
    print("WELL DONE! YOUR SCORE WAS", score)
    break

while score<2:
    print("BETTER LUCK NEXT TIME! Your Score Was", score)
    break

#Goodbye message
print("THANK YOU FOR PLAYING THE SIMPLE QUIZ GAME ")

