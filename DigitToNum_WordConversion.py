words_upto_19 = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEEN']
words_for_tens = ['','','TWENTY','THIRTY','FORTY','FIFTY','SIXTY','SEVENTY','EIGHTY','NINTY']
words_for_hundreds = ['','ONE HUNDRED','TWO HUNDRED','THREE HUNDRED','FOUR HUNDRED','FIVE HUNDRED','SIX HUNDRED','SEVEN HUNDRED','EIGHT HUNDRED','NINE HUNDRED']
words_for_thousand = ["",'ONE THOUSAND','TWO THOUSAND','THREE THOUSAND','FOUR THOUSAND','FIVE THOUSAND','SIX THOUSAND','SEVEN THOUSAND','EIGHT THOUSAND','NINE THOUSAND']

n = input('Enter a number from 0 to 9999:')

if (len(n) == 2 and int(n) < 20) or len(n) == 1:
    print(words_upto_19[int(n)])
    
elif len(n) == 2 and int(n) > 19:
    if int(n[1]) != 0:
        print(words_for_tens[int(n[0])] + ' ' + words_upto_19[int(n[1])])
        
    else:
        print(words_for_tens[int(n[0])])
        
elif len(n) == 3:
    print(words_for_hundreds[int(n[0])] + ' AND ' + words_for_tens[int(n[1])] + ' ' + words_upto_19[int(n[2])])

elif len(n) == 4:
    if int(n[2]) < 19:
        print(words_for_thousand[int(n[0])] + ' ' + words_for_hundreds[int(n[1])] + ' AND ' + words_upto_19[int(n[2:4])])
        
    else:
        print(words_for_thousand[int(n[0])] + ' ' + words_for_hundreds[int(n[1])] + ' AND ' + words_for_tens[int(n[2])] + ' ' + words_upto_19[int(n[3])])

else:
    print('Please enter a number from 0 to 9999')
