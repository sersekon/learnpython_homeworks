question_answer = {
    "Как дела ?": "Хорошо!",
 "Что делаешь?": "Программирую"
 }

while True:
    question = input(" ")
    if question in question_answer:
        print(question_answer[question])
    else:
        print()
        