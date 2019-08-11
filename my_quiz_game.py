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
    buttons = ["Blue", "range", "green", "yellow"]
    new_answer = {}
    shuffle(buttons)
    new_answer['question'] = question['question']
    for i in range(4):
        if i == 0:
            new_answer["correct"] = buttons[i]
            new_answer[buttons[i]] = question["Answers"][i]
            questions.append(new_answer)

            buzz = BuzzController.BuzzController()
            for question in questions:
                question_answered = False
                available_answers = ["Blue", "Orange", "Green", "Yellow"]
                available_controllers = [0, 1, 2, 3]

                while not question_answered:
                    print(question["question"])

                    for i in available_answers:
                        print(i + " " + question[i.lower()])

                    thread.start_new_thread(buzz.light_blink, (available_controllers,))
                    controller = buzz.controller_get_first_pressed("Red", available_controllers)
                    buzz.light_blinking = False
                    buzz.light_set(controller, True)
                    time.sleep(0.5)

                    while True:
                        button = buzz.get_button_pressed(controller)
                        if button and button != "Red":
                            if button == question["correct"]:
                                print("Controller " + str(controller) + " was correct")
                                question_answered = True
                                score[controller] += 1
                                break
                            elif button.capitalize() in available_answers:
                                print("Sorry incorrect answer")
                            available_controllers.remove(controller)
                            available_answers.remove(button.capitalize())
                            break
                    buzz.light_set(controller, False)
                    time.sleep(1)

                    print("Final score:" + score)
