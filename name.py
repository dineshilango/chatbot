import nltk


# def find_name(name):

#     if(name != None):
#         name_tokens = nltk.word_tokenize(name)
#         stop_words = ['my', 'name', 'is', 'they', 'call', 'me', 
#                     'i', 'am', 'what', 'your', 'do', 'you', 'this']
#         remove_words = []
#         for word in name_tokens:
#             lower = word.lower()
#             if lower in stop_words:
#                 remove_words.append(word)
        
#         for e in remove_words:
#             name_tokens.remove(e)

#         final_name = ' '.join(str(e) for e in name_tokens)
#         final_name = final_name.strip()
#         print(final_name)
#     return final_name

#def find_name(text):
#    tokens = nltk.tokenize.word_tokenize(text)
#    pos = nltk.pos_tag(tokens)
#    sentt = nltk.ne_chunk(pos, binary = False)
#    person = []
#    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
#        for leaf in subtree.leaves():
#            person.append(leaf[0])
#s    return (''.join(str(e) for e in person))

def is_name(name):

   for sent in nltk.sent_tokenize(name):
      for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
         if hasattr(chunk, 'label'):
            return(1)
   return(0)

def find_name(text):
   for sent in nltk.sent_tokenize(text):
      for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
         if hasattr(chunk, 'label'):
            return((' '.join(c[0] for c in chunk).strip()))

