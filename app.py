import os
import openai
import csv
import time


input = "input.txt"
output = "output.csv"
keys = [
        "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",
        "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",
        "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"
        ]
waiterror = 60
showdebug = False

model_engine = "text-davinci-003"
max_tokens = 4024

w_file = open(output, mode="w", encoding='utf-8')
file_writer = csv.writer(w_file, delimiter=",", quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
file_writer.writerow(["Вопрос", "Ответ"])

with open(input, 'r', encoding='UTF-8') as file:
    lines = [line.rstrip() for line in file]
    index = 0
    key = 0
    while index<len(lines):
            print("Вопрос:",lines[index])
            try:
                openai.api_key = keys[key]
                completion = openai.Completion.create(
                    engine=model_engine,
                    prompt=lines[index],
                    max_tokens=max_tokens,
                    temperature=0.5,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                if showdebug:
                    print(completion)
                if "text" in completion.choices[0]:
                    file_writer.writerow([lines[index], completion.choices[0].text])
                    w_file.flush()
                else:
                    print("Ошибка")
                index += 1
            except Exception as e:
                print(e)
                if "exceeded your current quota" in str(e):
                    key += 1
                    if key < len(keys):
                        print("Лимит. Берем следующий ключ",keys[key])
                    else:
                        print("Ключи кончились")
                        break
                else:
                    time.sleep(waiterror)
