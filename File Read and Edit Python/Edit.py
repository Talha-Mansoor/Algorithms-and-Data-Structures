# Name: Talha Mansoor
# NSID= kgy284
#Student number: 11346490
# Instructor's name: Ed Pakroka


'''Function inputs a file called MLK.txt, converts to lowercase, removes punctuatotion and then counts its words.
It outputs a word count file called MLKfreq.txt and lists top 20 words in console.'''

import string
def clean_txt(text_str):                 #Function to clean text
    lowercase=text_str.lower()

    for p in string.punctuation:
        lowercase=lowercase.replace(p," ")
    return lowercase


def main_funciton():
    wordfreq={}
    Clean=""
    x=open("MLK.txt","r")       #run clean_txt function by passing lines from MLK to be cleaned and returned
    for line in x:
        line=line.rstrip('\n')
        Clean+=clean_txt(line)

    #print(Clean)


    excluded_words = ('the', 'a', 'and', 'of' ,'is', 'to', 'be', 'are', 'on', 'at', 'an','but')
    wordlist = Clean.split(' ')                   #making list of words from cleaned text to be counted
    #print(wordlist)


    for key in wordlist:
        if key not in excluded_words:
            if key not in wordfreq:
                wordfreq[key]=1
            else:
                wordfreq[key]+=1
    del wordfreq['']
    sort={}
    for key in sorted(wordfreq):
        sort[key]=str(wordfreq[key])
    #print(sort)
   # print(wordfreq)

    x.close()
    y=open("MLKfreq.txt","w")  #close previous opened file and open new file to write key-value pairs on
    final_dic=""

    for k in sort:
        final_dic+=k+' '+str(sort[k])+'\n'

    y.write(str(final_dic))
    y.close()

    # Functions sorts a dictionary by values (descending order)
    def sort_dict_by_value(dictionary):
        #parameter is the dictionary to be sorted


        values = sorted(dictionary.values(), reverse=True)
        # make a copy of original dictionary so its values are not changed by this function
        duplicate = dictionary.copy()
        pairs_sorted_by_value = []  # initialize list of keu-value pairs to be returned

        for a in values:
            for x in duplicate:  # look for corresponding key, stop search When key found
                if duplicate[x] == a:  #
                    break
            # once corresponding key found, add the key-value pair to the list to be returned
            # delete key from duplicate dictionary so it doesn't show up in another search for the same value
            pairs_sorted_by_value.append([x, a])
            del duplicate[x]

        return pairs_sorted_by_value

    print ('Top 20 most frequent words are as follows:')
    count = 0
    sorted_dict=sort_dict_by_value(wordfreq)
    for p in sorted_dict[:20]:
       print(p[0] + " " + str(p[1]))


main_funciton()
