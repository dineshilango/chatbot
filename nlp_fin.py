import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
from nltk.corpus import stopwords
import json
import math
import re
from nltk.tokenize import sent_tokenize, word_tokenize

with open('data.json') as json_data:
    d = json.load(json_data)
# def isDigit(x):
#     try:
#         float(x)
#         return True
#     except ValueError:
#         return False
# def intLog(x):
#     try:
#         math.log(x,2)
#         return True
#     except ValueError:
#         return False

train = [("Great place to be when you are in Bangalore.", "pos"),
  ("The place was being renovated when I visited so the seating was limited.", "neg"),
  ("Loved the ambience, loved the food", "pos"),
  ("The food is delicious but not over the top.", "neg"),
  ("Mushroom fried rice was spicy", "pos"),
  ("shouldn't be", "neg"),
  ("should be", "pos"),
  ("must be", "pos"),
  ("may be", "pos"),
  ("can be", "pos"),
  ("would be", "pos"),
  ("should not be", "neg"),
  ("may not be", "neg"),
  ("would not be", "neg"),
  ("cannot be", "neg"),
  ("can't be", "neg"),
  ("shouldn't be", "neg"),
  ("wouldn't be", "neg"),
  ("without", "neg"),
  ("with", "pos"),
  ("budget should be ", "pos"),
  ("its cost should be less than 20000","pos")
]
dictionary = set(word2.lower() for passage in train for word2 in word_tokenize(passage[0]))
t = [({word2: (word2 in word_tokenize(x[0])) for word2 in dictionary}, x[1]) for x in train]
classifier = nltk.NaiveBayesClassifier.train(t)

# word = "Budget should be 13000rs to 90000rs. RAM with 4gb. Rating with 4 to 5. Storage with 64gb. Screen with 6.22 inches. Camera with 13MP. Processor with mediatek. Battery with 3260 mah"
# print("Hii\nI am Mobile Guru\nI'll help you in choosing best mobile based on your wish...(To stop the query type end)")

word = ''
word_temp = ''
# while (word_temp.lower()!='end'):
#     word_temp = ''
#     word_temp += " "
#     word_temp = input("How can I help you...?\n")
#     if word_temp.lower() == 'end' :
#         break
#     if word_temp[-1]=='.':
#         word+= word_temp.rstrip('.')+' . '
#     else:
#         word+= word_temp+' . '

def rest (word):
    def isDigit(x):
        try:
            float(x)
            return True
        except ValueError:
            return False
    def intLog(x):
        try:
            math.log(x,2)
            return True
        except ValueError:
            return False

    word = word.lower()
    word = word.replace('rs', ' ')
    word = word.replace('gb', ' ')
    word = word.replace('inches', ' ')
    word = word.replace('inch', ' ')
    word = word.replace('mp', ' ')
    sent2 = []
    stopWords = set(stopwords.words('english'))
    word_tok3 = nltk.word_tokenize(word)
    for i in word_tok3:
        if i == ',' or i == 'and':
            word_tok3 = word.split(i)
            sent2.append(word_tok3[0])
            sent2.append(word_tok3[1])
    for i in sent2:
        print(str(i))
        word = word.replace(str(i),"")
    print(word)
    word = word.replace(",","")
    word = word.replace("and","")
    sent3 = nltk.sent_tokenize(word)
    for i in sent3:
        sent2.append(i)
    print(sent2)
    sent=[]
    keyword = ['cost','budget','price','rating','ram','memory','internal','storage','display','screen','camera','battery','processor','chipset']
    user_cond = {}
    for j in sent2:
        j = j.lower()
        sent.append(j)
    print(sent)
    bs = ["want", "phone","need", "smartphone", "show", "around","mobile","mobiles"]
    for sen in sent:
        word_tok2 = word_tokenize(sen.lower().strip())
        #print(word_tok)
        test_data_features = {word2.lower(): (word2 in word_tok2) for word2 in dictionary}
        if classifier.classify(test_data_features)=='pos':
            worth = []
            user_key = []
            temp = []
            word_tok = nltk.word_tokenize(sen)
            for key in word_tok:
                if key not in stopWords and key not in bs:
                    worth.append(key)
                if (key == 'above') or (key == 'less') or (key == 'lesser') or (key == 'greater') or (key == 'below') or (key == 'under'):
                    temp.append(key)
            for usr_key in worth:
                for def_key in keyword:
                    if usr_key == def_key:
                        if usr_key == 'cost' or usr_key == 'budget' or usr_key == 'price' :
                            user_key.append('cost')
                            continue
                        elif usr_key == 'ram' or usr_key == 'memory' :
                            user_key.append('ram')
                            continue
                        elif usr_key == 'display' or usr_key == 'screen' :
                            user_key.append('display')
                            continue
                        elif usr_key == 'internal' or usr_key == 'storage' :
                            user_key.append('internal')
                        elif usr_key == 'processor' or usr_key == 'chipset' :
                            user_key.append('chipset')
                            # temp = sen
                        else:
                            user_key.append(usr_key)
                if usr_key != '.' and usr_key not in keyword:
                    temp.append(usr_key)
            user_cond[user_key[-1]] = temp


    if user_cond != [] :
        res_dis_cost = []
        res_dis_ram = []
        res_dis_rat = []
        res_dis_int = []
        res_dis_display = []
        res_dis_cam = []
        res_dis_chip = []
        res_dis_bat = []
        for ke in user_cond.keys() :
            if ke == 'cost' :
                no_el=[]
                todo_el = []
                te = user_cond[ke]
                for el in te:
                    if el.isdigit() :
                        no_el.append(int(el))
                    else :
                        todo_el.append(el)
                if len(no_el) == 2:
                    maxi = max(no_el[0],no_el[1])
                    mini = min(no_el[0],no_el[1])
                elif len(no_el) == 1:
                    if todo_el:
                        print(todo_el)
                        for to in todo_el:
                            if to == 'above' or to == 'greater':
                                mini = no_el[0]
                                maxi = '120000'
                            elif to == 'below' or to == 'less' or to == 'lesser' or to == 'under':
                                maxi = no_el[0]
                                mini = '0'
                            else :
                                print("Couldn't understand you...")
                                return("Couldn't understand you...")
                    else:
                        maxi = int(no_el[0])+5000
                        mini = int(no_el[0])-5000
                        if mini < 0:
                            mini = 0
                for j in d:
                    j["cost"] = j["cost"].replace(",", "").strip()
                    if int(j["cost"]) >= int(mini) and int(j["cost"]) <= int(maxi):
                        res_dis_cost.append(j)

            if ke == 'ram' :
                no_el=[]
                ram = []
                todo_el = []
                te = user_cond[ke]
                for el in te:
                    if el.isdigit() :
                        no_el.append(int(el))
                    else :
                        todo_el.append(el)

                if len(no_el) == 2:
                    for i in range(min(no_el[0],no_el[1]),max(no_el[0],no_el[1]+1)):
                        ram.append(i)
                elif len(no_el) == 1:
                    print(todo_el)
                    if todo_el:
                        for to in todo_el:
                            if to == 'above' or to == 'greater':
                                for i in range(no_el[0],12):
                                    ram.append(i)

                            elif to == 'below' or to == 'less' or to == 'lesser':
                                for i in range(1,no_el[0]):
                                    ram.append(i)
                            else :
                                print("Couldn't understand you...")
                                return("Couldn't understand you...")
                    else:
                        
                        ram.append(no_el[0])

                for j in d:
                    if "ram" in j.keys():
                        for i in ram:
                            if (j["ram"]) == str(i)+" GB":
                                res_dis_ram.append(j)

            if ke == 'rating' :
                no_el=[]
                todo_el = []
                te = user_cond[ke]
                for el in te:
                    if isDigit(el) :
                        no_el.append(int(el))
                    else :
                        todo_el.append(el)
                if len(no_el) == 2:
                    maxi = max(no_el[0],no_el[1])
                    mini = min(no_el[0],no_el[1])
                elif len(no_el) == 1:
                    if todo_el:
                        print(todo_el)
                        for to in todo_el:
                            if to == 'above' or to == 'greater':
                                mini = no_el[0]
                                maxi = '5'
                            elif to == 'below' or to == 'less' or to == 'lesser':
                                maxi = no_el[0]
                                mini = '0'
                            else :
                                print("Couldn't understand you...")
                                return("Couldn't understand you...")
                    else:
                        maxi = float(no_el[0])
                        mini = float(no_el[0])
                        if mini < 0 or mini > 5:
                            print("Couldn't understand you...")
                            return("Couldn't understand you...")
                # elif
                for j in d:
                    # j[""] = j["cost"].replace(",", "").strip()
                    if j["rating"] != "no rating":
                        if float(j["rating"]) >= float(mini) and float(j["rating"]) <= float(maxi):
                            res_dis_rat.append(j)
            if ke == 'internal':
                no_el=[]
                todo_el = []
                te = user_cond[ke]
                for el in te:
                    if el.isdigit() :
                        no_el.append(int(el))
                    else :
                        todo_el.append(el)
                if len(no_el) == 2:
                    maxi = max(math.log(int(no_el[0]),2),math.log(int(no_el[1]),2))
                    mini = min(math.log(int(no_el[0]),2),math.log(int(no_el[1]),2))
                elif len(no_el) == 1:
                    if todo_el:
                        print(todo_el)
                        for to in todo_el:
                            if to == 'above' or to == 'greater':
                                mini = math.log(int(no_el[0]),2)
                                maxi = '9'
                            elif to == 'below' or to == 'less' or to == 'lesser':
                                maxi = math.log(int(no_el[0]),2)
                                mini = '0'
                            else :
                                print("Couldn't understand you...")
                                return("Couldn't understand you...")
                    else:
                        maxi = math.log(int(no_el[0]),2)
                        mini = math.log(int(no_el[0]),2)
                        if mini < 0:
                            mini = 0
                for j in d:
                    if "internal" in j.keys():
                        j["internal"] = j["internal"].replace(" GB", "").strip()
                        if isDigit(j["internal"]):
                            if intLog(int(j["internal"])):
                                if math.log(int(j["internal"]),2) >= int(mini) and math.log(int(j["internal"]),2) <= int(maxi):
                                    res_dis_int.append(j)

            if ke == 'display' :
                no_el=[]
                todo_el = []
                te = user_cond[ke]
                for el in te:
                    if isDigit(el) :
                        no_el.append(int(el))
                    else :
                        todo_el.append(el)
                if len(no_el) == 2:
                    maxi = max(no_el[0],no_el[1])
                    mini = min(no_el[0],no_el[1])
                elif len(no_el) == 1:
                    if todo_el:
                        print(todo_el)
                        for to in todo_el:
                            if to == 'above' or to == 'greater':
                                mini = no_el[0]
                                maxi = '7.5'
                            elif to == 'below' or to == 'less' or to == 'lesser':
                                maxi = no_el[0]
                                mini = '0'
                            else :
                                print("Couldn't understand you...")
                                return("Couldn't understand you...")
                    else:
                        maxi = float(no_el[0])
                        mini = float(no_el[0])
                        if mini < 0 or mini > 7.5:
                            print("Couldn't understand you...")
                            return("Couldn't understand you...")
                # elif
                for j in d:
                    # j[""] = j["cost"].replace(",", "").strip()
                    if "display" in j.keys():
                        b = j["display"].split("(")
                        b3 = b[1].split("inch")
                        b2 = b3[0].strip()
                        if float(b2) >= float(mini) and float(b2) <= float(maxi):
                            res_dis_display.append(j)
            if ke == 'camera' :
                no_el=[]
                todo_el = []
                te = user_cond[ke]
                cam = []
                for el in te:
                    if isDigit(el) :
                        no_el.append(int(el))
                    else :
                        todo_el.append(el)
                if len(no_el) == 2:
                    for i in range(no_el[0],no_el[1]+1):
                        cam.append(i)
                elif len(no_el) == 1:
                    if todo_el:
                        print(todo_el)
                        for to in todo_el:
                            if to == 'above' or to == 'greater':
                                mini = int(no_el[0])
                                maxi = 60
                                for i in range(mini,maxi+1):
                                    cam.append(i)
                            elif to == 'below' or to == 'less' or to == 'lesser':
                                maxi =int(no_el[0])
                                mini = 0
                                for i in range(mini,maxi+1):
                                    cam.append(i)
                            else :
                                print("Couldn't understand you...")
                                return("Couldn't understand you...")
                    else:
                        cam.append(no_el[0])
                        mini = int(no_el[0])
                        maxi = int(no_el[0])
                        if mini < 0 or maxi > 60:
                            print("Couldn't understand you...")
                            return("Couldn't understand you...")
                for j in d:
                    if "Rear camera" in j.keys():
                        for i in cam:

                            b = re.search(str(i)+"MP",j["Rear camera"])
                            if b:
                                res_dis_cam.append(j)
    
            if ke == 'chipset' :
                te = user_cond[ke]
                chip = ""
                for i in range(0,len(te)):
                    chip += str(te[i])+" "
                for j in d:
                    if "chipset" in j.keys():
                        chip.strip()
                        b = re.search(str(chip),j["chipset"].lower())
                        if b:
                            res_dis_chip.append(j)
            if ke == 'battery' :
                te = user_cond[ke]
                chip = ""
                for i in range(0,len(te)):
                    chip += str(te[i])+" "
                for j in d:
                    if "battery" in j.keys():
                        chip.strip()
                        b = re.search(str(chip),j["battery"].lower())
                        if b:
                            res_dis_bat.append(j)
    #print(res_dis_cost)

    def dict_to_set(res_dis_cost):
        res_unique = []
        for i in res_dis_cost:
            phone_attr = i.values()
            res_unique.append(list(phone_attr))

        return(res_unique)


    final = []
    unique_url = []
    flag = False 


    def check_in(list_dis):
        final = []
        if not flag:
            for i in list_dis:
                if i[2] not in unique_url:
                    final.append(i)
                    unique_url.append(i[2])
        
        else:
            for i in list_dis:
                if i[2] in unique_url:
                    final.append(i)

        return final



    set_dis_cost = dict_to_set(res_dis_cost)
    set_dis_ram = dict_to_set(res_dis_ram)
    set_dis_cam = dict_to_set(res_dis_cam)
    set_dis_rat = dict_to_set(res_dis_rat)
    set_dis_int = dict_to_set(res_dis_int)
    set_dis_display = dict_to_set(res_dis_display)
    set_dis_chip = dict_to_set(res_dis_chip)
    set_dis_bat = dict_to_set(res_dis_bat)

    # check_in(set_dis_cost)
    # check_in(set_dis_ram)
    # check_in(set_dis_rat)
    # check_in(set_dis_int)

    conds = list(user_cond.keys())

    if('cost' in conds):
        if(not flag):
            final = check_in(set_dis_cost)
            flag = True
        else:
            final = check_in(set_dis_cost)
        
    if('ram' in conds):
        
        if(not flag):
            final = check_in(set_dis_ram)
            flag = True
        else:
            final = check_in(set_dis_ram)

    if('rating' in conds):     
        if(not flag):
            final = check_in(set_dis_rat)
            flag = True
        else:
            final = check_in(set_dis_rat)

    if('camera' in conds):     
        if(not flag):
            final = check_in(set_dis_cam)
            flag = True
        else:
            final = check_in(set_dis_cam)

    if('internal' in conds):
        if(not flag):
            final = check_in(set_dis_int)
            flag = True
        else:
            final = check_in(set_dis_int)

    if('display' in conds):
        if(not flag):
            final = check_in(set_dis_display)
            flag = True
        else:
            final = check_in(set_dis_display)

    if('battery' in conds):
        if(not flag):
            final = check_in(set_dis_bat)
            flag = True
        else:
            final = check_in(set_dis_bat)

    if('chipset' in conds):
        if(not flag):
            final = check_in(set_dis_chip)
            flag = True
        else:
            final = check_in(set_dis_chip)




    fin = []
    count = 1
    if not final:
        print("No such phones Exist")
        return("No such phones Exist")
    
    else:
        for i in final:
            # print("{}: Name: {}, Cost: {}, URL: {}".format(count, i[0], i[3],i[2]))
            fin.append(i[0])
            fin.append(i[2])
            # fin.append("c")
            count = count+1
    # print(str(fin))
    return(fin)

# res_dis = []
# # res_dis = set(res_dis_cost).intersection(set(res_dis_ram),set(res_dis_rat))
# for i in res_dis_cost:
#     if i in res_dis_ram:
#         if i in res_dis_rat:
#             if i in res_dis_int:
#                 if i in res_dis_display:
#                     if i in res_dis_chip:
#                         if i in res_dis_bat:
#                             res_dis.append(i)

# print(res_dis)
# print(user_cond.keys())
# condi = []
# for i in user_cond.keys():
#     if i == 'cost':
#         condi.append(res_dis_cost)
#     if i == 'ram':
#         condi.append(res_dis_ram)
#     if i == 'rating':
#         condi.append(res_dis_rat)
#     if i == 'internal':
#         condi.append(res_dis_int)
#     if i == 'display':
#         condi.append(res_dis_display)
#     if i == 'chipset':
#         condi.append(res_dis_chip)
#     if i == 'battery':
#         condi.append(res_dis_bat)
# res_dis = []
# result = []
# # for i in range(0,len(condi)):
# #     result.append(list(set(res_dis).intersection(set(condi[i]))))

# print(set(condi[0]))
    
# # print(res_dis_display)
# rest("ram with 4gb and budget with 12000rs.")
