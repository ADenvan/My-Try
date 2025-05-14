import random
import time
import threading


# Функция для генерации случайного примера на сложение с числами от 0 до 5
def generate_question():
    return random.randint(0, 5), random.randint(0, 5)


# Функция для проверки правильности ответа пользователя
def check_answer(num1, num2, answer):
    return num1 + num2 == answer


# Функция для обработки таймера сессии
def session_timer():
    global session_time  # Доступ к глобальной переменной времени сессии
    while session_time > 0:  # Цикл, пока время сессии не достигнет 0
        time.sleep(1)  # Пауза выполнения на 1 секунду
        session_time -= 1  # Уменьшение времени сессии на 1 секунду
    print("\nВремя сессии вышло!")  # Вывод сообщения, когда время сессии истекло
    end_session()  # Завершение сессии


# Функция для завершения сессии
def end_session():
    global session_ended  # Доступ к глобальной переменной, указывающей на завершение сессии
    session_ended = True  # Установка флага завершения сессии в значение True


# Основная функция для запуска сессии
def main():
    global session_time, session_ended  # Доступ к глобальным переменным
    session_time = 3  # Установка времени сессии на 3 секунды
    session_ended = False  # Изначально установка флага завершения сессии в False

    # Запуск отдельного потока для таймера сессии
    threading.Thread(target=session_timer).start()

    # Переменные для отслеживания правильных и неправильных ответов, а также общего количества вопросов
    correct_answers = 0
    incorrect_answers = 0
    total_questions = 0

    # Основной цикл для задания вопросов и обработки ввода пользователя
    while not session_ended:  # Цикл продолжается, пока сессия не завершена
        print(f"ВРЕМЯ СЕССИИ: > > {session_time}\n")
        if session_time == 0:  # Проверка, достигло ли время сессии 0
            end_session()  # Завершение сессии, если время истекло
            break

        num1, num2 = generate_question()  # Генерация случайного вопроса
        print(f"Сколько будет {num1} + {num2}?")  # Вывод вопроса

        start_time = time.time()  # Запись времени начала для ответа пользователя
        user_answer = input("Ваш ответ: ")  # Получение ответа пользователя
        end_time = time.time()  # Запись времени окончания для ответа пользователя

        if end_time - start_time > 3:  # Проверка, превысил ли пользователь лимит времени
            print("Время вышло!")  # Уведомление пользователя, если время истекло
            continue  # Переход к следующей итерации цикла

        try:
            user_answer = int(user_answer)  # Преобразование ввода пользователя в целое число
            if check_answer(num1, num2, user_answer):  # Проверка правильности ответа
                session_time += end_time - start_time
                print("Правильно!")  # Уведомление пользователя, если ответ правильный
                correct_answers += 1  # Увеличение количества правильных ответов
                total_questions += 1  # Увеличение общего количества вопросов
            else:
                print("Неправильно!")  # Уведомление пользователя, если ответ неправильный
                incorrect_answers += 1  # Увеличение количества неправильных ответов
                total_questions += 1  # Увеличение общего количества вопросов
        except ValueError:
            print("Неверный ввод! Пожалуйста, введите число.")  # Уведомление пользователя, если ввод некорректен

    # Отображение итогов сессии, когда она завершена
    print(
        f"\nСессия завершена!\nВсего вопросов: {total_questions}\nПравильных ответов: {correct_answers}\nНеправильных ответов: {incorrect_answers}")


if __name__ == "__main__":
    main()

####################################################################
# import random
# import time
# import math
#
# def generate_question():
#     return random.randint(0, 5), random.randint(0, 5)
#
#
# def check_answer(num1, num2, answer):
#     return num1 + num2 == answer
#
#
# def main():
#     correct_answers = 0
#     incorrect_answers = 0
#     total_questions = 0
#     total_time = 0
#
#     for t in range(3):
#         print(t, end='', flush=True)
#         time.sleep(1)
#         print()
#
#     while total_time <= 10:
#
#         num1, num2 = generate_question()
#         print(f"What is {num1} + {num2}?")
#
#         start_time = time.time()
#         user_answer = input("Your answer: ")
#         end_time = time.time()
#
#         if end_time - start_time > 3:
#             print(f"Time's up! {end_time}")
#             if total_time > 10:
#                 break
#             else:
#                 total_time += end_time - start_time
#                 continue
#
#         try:
#             user_answer = int(user_answer)
#             if check_answer(num1, num2, user_answer):
#                 print(f"Correct! end-time is: {round(end_time, 2)} > math: {math.ceil(end_time)}")
#                 correct_answers += 1
#                 total_questions += 1
#                 total_time += end_time - start_time
#                 print(f"{round(total_time)}")
#                 print(f"{round(end_time - start_time)}")
#                 if total_time >= 10:
#                     break
#             else:
#                 print(f"Incorrect! {round(end_time, 2)}")
#                 incorrect_answers += 1
#                 total_questions += 1
#                 # total_time += end_time - start_time
#                 print(f"{round(total_time)}")
#                 if total_time >= 10:
#                     break
#         except ValueError:
#             print("Invalid input! Please enter a number.")
#
#     print(
#         f"\nSession ended!\nTotal questions: {total_questions}\nCorrect answers: {correct_answers}\nIncorrect answers: {incorrect_answers}")
#
#
# if __name__ == "__main__":
#     main()



###################################################################
# import random
# import time
#
#
# def generate_question():
#     return random.randint(0, 5), random.randint(0, 5)
#
#
# def check_answer(num1, num2, answer):
#     return num1 + num2 == answer
#
#
# def main():
#     while True:
#         num1, num2 = generate_question()
#         print(f"What is {num1} + {num2}?")
#
#         start_time = time.time()
#         user_answer = input("Your answer: ")
#         end_time = time.time()
#
#         if end_time - start_time > 3:
#             print("Time's up! Next question...")
#             continue
#
#         try:
#             user_answer = int(user_answer)
#             if check_answer(num1, num2, user_answer):
#                 print("Correct! Next question...")
#             else:
#                 print("Incorrect! Next question...")
#         except ValueError:
#             print("Invalid input! Please enter a number.")
#
#
# if __name__ == "__main__":
#     main()
