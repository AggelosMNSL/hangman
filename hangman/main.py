#import word
import hang
done1 = True
while done1:
    s = 2
    m = 0
    done2 = True
    word = 'duck'#word.pick()
    found = [word[0],word[len(word)-1]]
    wrong = []
    while done2 :
        for i in range(0,len(word)):                   #print word
            done = True
            for j in range(0,len(found)):
                if found[j] == word[i]:
                    print(word[i],sep='',end='')
                    done = False
            if done:
                print(' _ ',sep='',end='')
        print('')
        x = hang.user_input()
        if '1' in x:                    #1 to exit
            done1 = False
            done2 = False
            print('The word was',word)
            print('Thanks for playing!')
            break
        if (x in found) or (x in wrong):
            print('You already gave that letter!')
        if (x in word) and (x not in found):
            found.append(x)
            for i in range(0,len(word)-1):
                if x == word[i]:
                    s += 1
            print('Found letter:',x)
        elif (x not in found) and (x not in wrong) :
            m += 1
            wrong.append(x)
            print('Wrong!',m,'/5')
        if s == len(word):
            done2 = False
            print('You found the word:',word)
        if m == 5:
            break
    if done2:
        print('The word was :',word,'\nYou lost :(')

