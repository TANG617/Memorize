# def dump(data):
#     # print(word_json["headWord"]);
#     word_rank = data['wordRank']
#     # head_word = data['headWord']
#     # sentences = data['content']['word']['content']['sentence']['sentences']
#     us_phone = data['content']['word']['content']['usphone']
#     uk_phone = data['content']['word']['content']['ukphone']
#     synonyms = data['content']['word']['content']['syno']['synos']
#     # phrases = data['content']['word']['content']['phrase']['phrases']
#     related_words = data['content']['word']['content']['relWord']['rels']
# #     return head_word,phrases,sentences,synonyms,related_words
# #
# # def tex(head_word,phrases,sentences,synonyms,related_words):
# #     t_word = "\\section{"+head_word+"}\n"
# #     t_phase = "\\paragraph{Phase}\n\\begin{itemize}\n\\itemsep0em\n"
# #     for phrase in phrases:
# #         t_phase = t_phase + "   \\item " + phrase['pContent'] + "\\\\" + phrase['pCn'] + "\n"
# #     t_phase = t_phase + "\\end{itemize}\n"
#     # t_sentense = "\\paragraph{Sentence}\n\\begin{itemize}\n\\itemsep0em\n"
#     # for sentence in sentences:
#     #     t_sentense = t_sentense +  "    \\item " + sentence['sContent'] +  "\\\\" + sentence['sCn'] + "\n"
#     # t_sentense = t_sentense + "\\end{itemize}\n"
#     return t_word  + t_sentense + t_phase + "\\hrulefill\n\n\n"

# print("Word Rank:", word_rank)
# print("Head Word:", head_word)
# print("\nSentences:")
# for sentence in sentences:
#     print(sentence['sContent'], "-", sentence['sCn'])
#
# # print("\nUS Phone:", us_phone)
# # print("UK Phone:", uk_phone)
#
# print("\nSynonyms:")
# for syno in synonyms:
#     print(syno['pos'], ":", syno['tran'])
#
# print("\nPhrases:")
# for phrase in phrases:
#     print(phrase['pContent'], "-", phrase['pCn'])
#
# print("\nRelated Words:")
# for rel in related_words:
#     print(rel['pos'], ":", ", ".join([word['hwd'] for word in rel['words']]))