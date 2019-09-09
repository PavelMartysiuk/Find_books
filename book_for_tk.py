from os import listdir
from os import path
from collections import defaultdict
import pickle
def helpy(folder):
    books = listdir(folder)
    res = defaultdict(set)
    for book in books:
        print(book)
        with open(path.join(f'./{folder}/' + book)) as file:
            try:
                content = set(file.read().lower().replace(',',' ').replace('.',' ').split())
                for word in content:
                    res[word].add(book)
            except UnicodeDecodeError:
                print('DecodeError')
    pickle_out = open('dicty.pickle','wb')
    pickle.dump(res,pickle_out)
    pickle_out.close()
     

def findbooks(args):
    pickle_in = open('dicty.pickle','rb')
    res = pickle.load(pickle_in)
    firstset = res[args[0].lower()]
    for ss in args[1:]:
        myset = res[ss.lower()]
        if myset:
            firstset &= myset
    return firstset
if __name__ == '__main__':
    helpy('books')
    print(findbooks('Конь'))
