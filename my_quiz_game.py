from __future__ import print_function
import BuzzController
import time
import thread
from random import shuffle

import_questions = [
    {"question": "what Is the capital of Australia", "Answers": ["Canberra", "Sydney", "Hobart", "Melbourne"]},
    {"question": "What is the capital of Japan", "Answers": ["Tokyo", "Hiroshima", "Osaka", "Kyoto"]},
]
questions = []
score = [0, 0, 0, 0]
for question in import_questions:
    buttons = ["blue", "orange", "green", "yellow"]
    new_answer = {}
    shuffle(buttons)
    new_answer['question'] = question['question']
    for i in range(4):
        if i == 0:
            new_answer["correct"] = buttons[i]
            new_answer[buttons[i]] = question["answers"][i]
            questions.append(new_answer)

            buzz = BuzzController.BuzzController()
            for question in questions:
                question_answered = False
                available_answers = ["Blue", "Orange"]
