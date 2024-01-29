filename = "GRE_2.json"
tex_filename = "GRE_ver2_00.tex"
import json
from ollama_link import llama_rank, llama_sentence

file = open(filename, 'r', encoding='utf-8')
replace_list = [  ['[','【'],[']','】'],['%','\%'],['&','\&'],['_','-']] #,['$','\$']
level_list = [ #num chinese / sen pha
    [[0,0],
     [0,0],
     0
     ],
    [[1,0],
     [1,0],
     0
     ],
    [[2, 0],
     [2, 0],
     0
     ],
    [[3, 0],
     [3, 0],
     2
     ],
    [[3, 0],
     [5, 0],
     4
     ],
    [[4, 0],
     [6, 0],
     4
     ],
    [[6, 0],
     [6, 0],
     6
     ],
    [[6, 0],
     [6, 1],
     6
     ],
    [[8, 0],
     [8, 1],
     8
     ],
    [[999, 1],
     [999, 1],
     999
     ]
]


t_head = "\\documentclass[UTF8,4pt,a3paper,space]{article}\n\\usepackage{geometry}\n\\geometry{landscape}\n\\usepackage{setspace}\n\\setstretch{0.5}\n\\usepackage[UTF8]{ctex}\n\\usepackage{multicol}\n\\geometry{top = 0cm, bottom = 1.5cm, left = 1cm, right = 0.5cm}\n\\begin{document}\n\\begin{multicols}{4}\n"
t_tail= "\\end{multicols}\n\\end{document}\n"
t_content = ""



def d_word(data):
    head_word = data['headWord']
    t_word = "\\section{" + head_word
    return t_word
def d_tran(data):
    transCn = data['content']['word']['content']['trans'][0]['tranCn']
    t_tran = "\\subsubsection*{\ \ \ \ \ \ \ \ \ " + transCn + "}"
    return t_tran
def d_sentence(data , max_num = 999 , Chinese = 1):
    t_sentense = "\\begin{itemize}\n\\itemsep-0.5em\n"  # \\paragraph{Sentence}\n
    try:
        sentences = data['content']['word']['content']['sentence']['sentences']
        cnt = 0
        for sentence in sentences:
            if (cnt == max_num):
                break
            cnt = cnt + 1
            t_sentense = t_sentense + "    \\item " + sentence['sContent']
            if Chinese:
                t_sentense = t_sentense + "\\ \\ " + sentence['sCn'] + "\n"
    # if(cnt != max_num):
    except:
        pass
    t_sentense = t_sentense + "    \\item " + llama_sentence(data['headWord']) + " \n"
        # try:
        #     t_sentense = t_sentense + "    \\item " + llama_sentence(data['headWord']) +" \n"
        # except:
        #     pass
    t_sentense = t_sentense + "\\end{itemize}\n"
    return t_sentense
def d_phase(data , max_num = 999 , Chinese = 1):
    phrases = data['content']['word']['content']['phrase']['phrases']
    t_phase = "\\begin{itemize}\n\\itemsep-0.5em\n" #\\paragraph{Phase}\n
    cnt = 0
    for phrase in phrases:
        if (cnt == max_num):
            break
        cnt = cnt + 1
        t_phase = t_phase + "   \\item " + phrase['pContent']
        if(Chinese):
            t_phase = t_phase + "\\ \\ " + phrase['pCn'] + "\n"
    t_phase = t_phase + "\\end{itemize}\n"
    return t_phase
def d_related(data , max_num = 999 ):
    related_words = data['content']['word']['content']['relWord']['rels']
    t_related = "\\begin{itemize}\n\\itemsep-0.5em\n" #\\paragraph{Related Words}\n
    cnt = 0
    for related_word in related_words:
        if (cnt == max_num):
            break
        cnt = cnt + 1
        t_related = t_related + "   \\item " + "<" + related_word['pos'] + "> " + ", ".join([word['hwd'] for word in related_word['words']]) + "\n"
    t_related = t_related + "\\end{itemize}\n"
    return t_related
def d_block(data):
    t_block =  d_word(data)
    word = data['headWord']
    rank = int(llama_rank(word))
    # if(rank <= 3):
    #     return "\n"
    level = level_list[rank]
    t_block = t_block +  "$^" + str(rank) + "$}\n"

    t_block = t_block + d_tran(data)
    try:
        t_block = t_block + d_sentence(data,level[0][0],level[0][1])
    except:
        pass

    try:
        t_block = t_block + d_phase(data,level[1][0],level[1][1])
    except:
        pass

    # try:
    #     t_block = t_block + d_related(data,level[2])
    # except:
    #     pass

    return t_block + "\\hrulefill\n\n\n"



tex_file = open(tex_filename, 'w', encoding='utf-8')
tex_file.write(t_head)
tex_file.close()

cnt = 0
for line in file.readlines():
    try:
        tex_file = open(tex_filename, 'a+', encoding='utf-8')
        words = line.strip()
        data = json.loads(words)
        # if(int(data['wordRank']) == 100): break
        cnt = cnt+1
        print(cnt)
        t_block = d_block(data)
        for i in replace_list:
            t_block = t_block.replace(i[0], i[1])
        tex_file.write(t_block)
        tex_file.close()

    except:
        print("ERROR")
        pass



tex_file = open(tex_filename, 'a', encoding='utf-8')
tex_file.write(t_tail)
tex_file.close()


file.close()