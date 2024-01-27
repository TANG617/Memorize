# from ollama import Client
# import ollama
import re
from ollama import Client


client = Client(host='http://api.tritium.top:11434',timeout=1000)
def llama_link(word):
    response = client.chat(model='llama2', messages=[
          {
            'role': 'user',
            # 'prompt': 'you are a judge aimed at sorting the following English vocabulary into 5 classes based on the difficulties of people memorizing. '
            #           'I will give you the word and you should give me the number from 1 to 5, '
            #           'in which, 1 is the easiest and 5 is the hardest',

            'content': 'you are a judge aimed at mark the following English word into 10 classes based on the difficulties for university student to memorize '
                        'I will give you the word and you should give me the number from 0 to 9, in which, 0 is the easiest and 9 is the hardest'
                        'for example , if I give you word <apple> you should answer me <Level 0>'
                        # 'if you understood, do not reply any word and just begin the task:'

          },
        {
            'role': 'assistant',
            'content': 'Of course! I\'d be happy to help. Please provide the English word you would like me to classify, and I will give you a difficulty level score on a scale of 0 to 9.'

        },
        {
            'role': 'user',
            'content':'the word is <' + word + '>'
        }
    ])

    pattern = r'[0-9]'
    ans = response['message']['content']
    print(ans)
    matches = re.findall(pattern, ans)

    try:
        print("【" + word + ":" + matches[0] + "】")
        return matches[0]
    except:
        print("ERROR")
        return 0