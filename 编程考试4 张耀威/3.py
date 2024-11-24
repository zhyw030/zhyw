import random as r
import time

# 数据文件名称，用于保存测试结果
DATA_FILE = "math_test_results.txt"

# 生成一道符合要求的口算题
def generate_question():
    operators = ["+", "-", "*", "/"]
    # 确保每种运算类型至少出现2次
    selected_operators = r.sample(operators, 4)
    question = ""
    num1 = 0
    num2 = 0
    operator = ""
    while True:
        operator = r.choice(selected_operators)
        if operator == "+":
            num1 = r.randint(1, 99)
            num2 = r.randint(1, 100 - num1)
            result = num1 + num2
            if result <= 100:
                question = f"{num1} {operator} {num2}"
                break
        elif operator == "-":
            num1 = r.randint(1, 99)
            num2 = r.randint(1, num1)
            question = f"{num1} {operator} {num2}"
            break
        elif operator == "*":
            num1 = r.randint(1, 10)
            num2 = r.randint(1, 100 // num1)
            result = num1 * num2
            if result <= 100:
                question = f"{num1} {operator} {num2}"
                break
        elif operator == "/":
            num1 = r.randint(1, 100)
            factors = [i for i in range(1, num1 + 1) if num1 % i == 0]
            num2 = r.choice(factors[1:])  # 排除1，避免太简单
            question = f"{num1} {operator} {num2}"
            break
    return question

# 判断答案是否正确
def check_answer(question, user_answer):
    parts = question.split()
    num1 = int(parts[0])
    operator = parts[1]
    num2 = int(parts[2])
    correct_answer = 0
    if operator == "+":
        correct_answer = num1 + num2
    elif operator == "-":
        correct_answer = num1 - num2
    elif operator == "*":
        correct_answer = num1 * num2
    elif operator == "/":
        correct_answer = num1 // num2
    return user_answer == correct_answer, correct_answer

# 根据分数给出评价
def get_evaluation(score):
    if score >= 90:
        return "非常棒，你的口算能力很强哦！"
    elif score >= 60:
        return "还不错，继续加油呀，争取更好的成绩呢。"
    else:
        return "要再加把劲啦，多练习一下口算会有很大进步的哦。"

# 将测试结果写入数据文件
def write_results_to_file(name, questions, correct_answers, user_answers):
    with open(DATA_FILE, 'a') as file:
        file.write(f"学生姓名：{name}\n")
        for i in range(len(questions)):
            file.write(f"题目 {i + 1}: {questions[i]}，正确答案：{correct_answers[i]}，你的答案：{user_answers[i]}\n")
        file.write("\n")

# 执行口算测试流程
def main():
    print("欢迎使用小学数学口算测试程序")
    while True:
        name = input("请输入你的姓名：")
        questions = []
        correct_answers = []
        user_answers = []
        score = 0
        for _ in range(10):
            question = generate_question()
            questions.append(question)
            print(f"请回答：{question} = ")
            try:
                user_answer = int(input())
                is_correct, correct_answer = check_answer(question, user_answer)
                user_answers.append(user_answer)
                correct_answers.append(correct_answer)
                if is_correct:
                    print(f"答对啦！正确答案就是 {correct_answer}，加10分哦。")
                    score += 10
                else:
                    print(f"答错了哦，正确答案是 {correct_answer}，继续加油呀。")
            except ValueError:
                print("请输入整数哦，这道题算答错啦，继续加油呀。")
        print(f"{name}，你的总分数是 {score} 分。")
        print(get_evaluation(score))
        write_results_to_file(name, questions, correct_answers, user_answers)
        play_again = input("是否想再测试一次？（输入y继续，其他任意键退出）")
        if play_again.lower()!= "y":
            break


if __name__ == "__main__":
    main()
