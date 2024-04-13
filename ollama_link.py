# from ollama import Client
# import ollama
import re
from ollama import Client


client = Client(host='http://api.tritium.top:11434',timeout=1000)
def llama_rank(word):
    response = client.chat(model='llama2', messages=[
          {
            'role': 'user',
            'content': 'you are a judge aimed at mark the following English word into 10 classes based on the difficulties for university student to memorize '
                        'I will give you the word and you should give me the number from 0 to 9, in which, 0 is the easiest and 9 is the hardest'
                        'for example , if I give you word <apple> you should answer me <Level 0>'
                        'if I give you word <groa> you should answer me <Level 8>'

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
    # print(ans)
    matches = re.findall(pattern, ans)

    try:
        print("【" + word + ":" + matches[0] + "】")
        return matches[0]
    except:
        print("ERROR")
        return 0

def llama_sentence(word):
    response = client.chat(model='llama2', messages=[
          {
            'role': 'user',
            'content': 'you are a native English speaker. I need you to make a sentence of word. '
                       'Do not answer anything except the sentence.'
                       'for example, the word is \'content\' you should answer me like  \' She felt content after finishing her favorite meal.\''
          },
        {
            'role': 'assistant',
            'content': 'Of course! I\'d be happy to help. '
                       'Please provide the English word and I would make a sentence directly without any other prompts'

        },
        {
            'role': 'user',
            'content':'the word is \"' + word + '\", please make a sentence with the word'
        }
    ])

    pattern = r'\n\s*(.*)'
    ans = response['message']['content']
    try:
        match = re.search(pattern, ans)[0]
        print(match[2:])
        return match[2:]
    except:
        print(ans)
        return ans
