with open('answer.txt','r') as f:
    answers = f.readlines()
    
with open('questions.txt','r') as q:
    questions = q.readlines()

with open('solution.txt','r') as s:
    solutions = s.readlines()

ans = [1,2,3,4]
rightCount = 0
wrongCount = 0

for k in questions:
    print(f'Q => {k}')
    j = answers[questions.index(k)]
    answer = j.split(',')
    print('Your options are :')
    z = 1
    for l in answer:
        print(f'{z} - {l}')
        z += 1
    answerChoice = int(input('Enter your choice :'))
    while answerChoice in ans:
        if answerChoice == int(solutions[questions.index(k)]):
            print('right answer.')
            rightCount += 1
            break
        elif answerChoice in ans:
            print('wrong answer.')
            print('The right answer was :',answer[int(solutions[questions.index(k)])-1])
            wrongCount += 1
            break
        else:
            print('Please enter a correct choice.')
            answerChoice = int(input('Enter your choice :'))
print('Total number of right answer :',rightCount)
print('Total number of wrong answer :',wrongCount)
    
