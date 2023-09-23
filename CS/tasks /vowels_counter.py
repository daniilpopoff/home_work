# значит 1 нам надо понять какое это слово на латинице и кирилице для того чтобы поделить буквы 
#буквами Б, В, Г, Д, Ж, З, Й, К, Л, М, Н, П, Р, С, Т, Ф, Х, Ц, Ч, Ш, Щ. Гласные звуки передаются буквами А, И, О, У, Ы, Э.
#  нужны только глассные буквы из алфавита потому что можно ифом решить все согласные 


word = input("Если вы хотите выйти напишите: break  ")

# ставим нужные счетчики 
counter = 0
vowels_num = 0 
consonants_num = 0

# валидируем слово вдруг кто-то напишет предложение или специальные символы мы возьмем от туда только буквы   
letters_validated_word  = "".join([letter for letter in word if letter.isalpha()])
word = letters_validated_word
# ставим флаг для break чтобы самый нижний принт не выводился 
flag_break = False
# идем  циклом по буквам по что гласное добавляем к каунтеру то что согласное добавляем к другому 
while counter < len(word):
   if word.lower() == "break":
    flag_break = True
    break
   else :
    
    letter = word[counter]
    if letter.lower() in ["а", "и", "о", "у", "ы", "э", "a", "e", "y", "o", "u", "i"]:
        vowels_num += 1
    else :
        consonants_num += 1
    counter +=1
    # считаем сколько гласных и согласных в процентном соотшении 
    procent_vow = (vowels_num/len(word))*100 
    procent_con = (consonants_num/len(word))*100 

if flag_break:
   print("Вы вышли запустите заново чтобы зайти")

else:
 print(f"Слово: {word} состоит из  {len(word)} букв, {vowels_num} из которых гласные и {consonants_num} согласные, их процентрое соотножение гласных букв в слове  : {round(procent_vow,2)}% процентное отошение согласных букв в слове {round(procent_con,2)}%")
# РАБотает  ^・ω・^