#list_1 = [1, 2, 3, 4, 3, 5]
#k = 3
#print(list_1.count(k))
#print(count(k))

#list_1 = [1, 2, 0, 4, 5]
#k = 3

# Введите ваше решение ниже
#def n(list_1, k):
#    return min(list_1, key=lambda x: abs(k - abs(x)))
#print(n(list_1, k))

'''
import re 
def Scrabble(text): 
    return bool(re.search("[а-яА-Я]", text)) 
Rus = { 1:"А, В, Е, И, Н, О, Р, С, Т", 2:"Д, К, Л, М, П, У", 3:"Б, Г, Ё, Ь, Я", 4:"Й, Ы", 
       5:"Ж, З, Х, Ц, Ч", 8:"Ш, Э, Ю", 10:"Ф, Щ, Ъ"} 
Eng = { 1:"A, E, I, O, U, L, N, S, T, R ", 2:"D, G", 3:"B, C, M, P", 4:"F, H, V, W, Y", 
       5:"K", 8:"J, X"} 
text = input("Введите слово: ").upper() 
if Scrabble(text): 
    print(sum([k for i in text for k, v in Rus.items() if i in v])) 
else: 
    print(sum([k for i in text for k, v in Eng.items() if i in v]))
    '''

k = 'ноутбук'
list_letters = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}

'''summ = 0
for i in k:
    for n, v in list_letters.items():
        if i in v:
            summ += n
print(f"Стоимость слова: {summ}")'''

word = k.upper()
summ = 0
for i in word:
    for k, v in list_letters.items():
        if i in v:
            summ += k
print(summ)