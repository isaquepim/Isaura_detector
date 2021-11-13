import unidecode 
import nltk
import regex as re
import string
import json
import pickle
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.ensemble import RandomForestClassifier

class Pipeline:

    def __init__(self) -> None:
        self.stemmer = nltk.stem.RSLPStemmer()
        self.maxlen = 746

        with open('tokenizer.json') as f:
            data = json.load(f)
            self.tokenizer = tokenizer_from_json(data)

        self.clf = pickle.load(open('finalized_model.sav', 'rb'))

    def clean_text(self,text):
        text = text.lower()
        text = unidecode.unidecode(text)
        num = re.compile(r'[-+]?[.\d]*[\d]+[:,.\d]*')
        text = num.sub(r'', text)
        text = ''.join([word for word in text if word in string.printable])
        text = [char for char in text if char not in string.punctuation]
        text = ''.join(text)
        tokenized = text.split()
        stem = []
        for tkn in tokenized:
            stem.append(self.stemmer.stem(tkn))
        text = ' '.join(stem)
        pad_type = 'post'
        trunc_type = 'post'   
        X = self.tokenizer.texts_to_sequences([text])
        X_pad = pad_sequences(X,padding=pad_type, truncating=trunc_type, maxlen=self.maxlen)

        return X_pad/5000

    def classify(self,text):
        text = self.clean_text(text)
        return self.clf.predict(text)


def main():
    p = Pipeline()

    print(p.classify('''
    
    O governo dos Países Baixos anunciou esta sexta-feira um conjunto de restrições para conter o aumento de casos de infeção de covid-19 que se têm verificado nas últimas semanas e que culminaram com mais de 16 mil novos casos nos dois últimos dias.

Em conferência de imprensa, o primeiro-ministro interino Mark Rutter e o seu ministro da Saúde, Hugo De Jonge, explicaram as medidas que entram este sábado em vigor e que serão válidas para as próximas três semanas.

As lojas e os serviços considerados não essenciais passam a ter de fechar às 18.00 horas, enquanto as lojas essenciais, a restauração e os supermercados passam a ter de fechar às 20.00.

Nos eventos públicos, passa a ser obrigatório que as pessoas estejam sentadas, com distanciamento físico e com um limite máximo de 1250 pessoas numa sala. Os eventos desportivos terão de se realizar sem público.

O governo holandês voltou a decretar o teletrabalho obrigatório, sempre que possível, mas mantém as escolas abertas, embora no ensino superior haja um limite máximo de alunos por sala.

É ainda obrigatório o uso de máscara em locais fechados, sendo que as pessoas devem guardar uma distância social de um metro e meio. O governo definiu ainda que as famílias não recebam em casa mais de quatro pessoas fora do agregado familiar.

Todos aqueles que moram na mesma casa com pessoas infetadas com covid-19 estão obrigadas a ficar em quarentena, uma regra que se aplica a vacinados e não vacinados.

Segundo os dados oficiais dos Países Baixos, 82,4 da população com mais de 12 anos já recebeu as duas doses da vacina, enquanto a 85,9 foi administrada pelo menos uma dose. No entanto, estima-se que cerca de 13 dos cidadãos holandeses não planeiam ser vacinados para já
    
    
    ''')[0])


if __name__ == '__main__':
    main()