
import time
questionBank = {'2 x 2 = ':[2,4,7,5], 'Who is prime minister of India?':['Narendra Modi','L K Advani','Mamta Banerji','Rahul Gandhi']}

answers = [1,2,3,4]
rightCount = 0
wrongCount = 0
questions = []
for i in questionBank.keys():
    questions.append(i)
solution = {questions[0]: 2,questions[1]: 1}
print('Enter 1,2,3,4 for choice 1,2,3,4 respectively.')
time.sleep(3)
for question in questions:
    print(f'Q => {question}')
    time.sleep(2)
    j = 1
    print('Your options are :')
    for i in questionBank[question]:
        print(j,'-',i)
        time.sleep(1)
        j += 1
    answerChoice = int(input('Enter your choice :'))
    if question in solution.keys():
        if answerChoice == solution[question]:
            print('Right answer.')
            rightCount += 1
        elif answerChoice in answers:
            print('Wrong answer.')
            print('The right answer was :',questionBank[question][solution[question]- 1])
            wrongCount += 1
        else:
            print('Enter the correct choice.')
print('Total number of right answer :',rightCount)
print('Total number of wrong answer :',wrongCount)
    
