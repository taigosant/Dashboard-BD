
path = '/home/taigo/Documents/2018.2/BD/Dashboard-BD/data/amazon-meta.txt'

if __name__ == '__main__':
    with open(path) as arq:
        count = 0
        text = arq.read()
        tokens = text.split('\n\n')
        for token in tokens:
            with open(str(count) + '.txt', 'a+') as neoFile:
                neoFile.write(token)
            count += 1
            neoFile.close()


