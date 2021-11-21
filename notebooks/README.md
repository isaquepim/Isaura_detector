# Notebooks

Os notebooks estão divididos em 2. A explicação vem a seguir.

## summary-Crisp_DM.ipynb

O primeiro notebook, que realiza as etapas iniciais da metodologia Crisp-DM. A ideia inicial era coletar notícias do site piaui.folha.uol para usar no fit do modelo. Para o scrapping do site foi utilizado o Chrome Driver em Python. O notebook coleta as notícias, faz uma análise textual e tenta criar um dataframe classificado para o modelo. Os dados infelizmente não conseguiram ser consistentes para desenvolver um modelo robusto. A problemática é a seguinte: Os dados vem de diversas fontes diferentes: (vídeos, áudios, publicações, correntes de whatsapp, etc.), e nem sempre o conteúdo original estava acessível, apenas trechos ou falas. O fato de estarmos fazendo o scrapping de um site de verificação de notícias adicionava o viés de que a maioria das notícias era falsa. 

Uma das soluções para esse problema seria complementar o dataset com notícias verdadeiras vindas de sites confiáveis. O processo, no entanto, é de certa forma bem artesanal. Para simplificar o processo, encontramos uma referência que tinha em mente a mesma coisa que nós: O dataset [Fakebr](https://github.com/roneysco/Fake.br-Corpus). Feito por brasileiros que caíram no mesmo problema que o nosso, fizeram o scrapping de sites emissores de fakenews, e de maniera semi-automática para cada notícia falsa incorporaram uma verdadeira da mesma temática.


## Fakebr.ipynb

Com o dataset Fakebr em mãos, o trabalho de modelagem fica mais direto. Nesse notebook foi feita uma exploração nos possíveis tipos de tokenização do texto e que técnicas de NLP usar. Optamos por uma bag-of-words, fazendo antes a lematização do texto com o pacote nltk. O tokenizador usado foi do Keras. Com uma priori de que modelos funcionam melhor na área de processamento de texto, avaliamos os modelos:
+ Naive Bayes
+ SVM 
+ Multilayer Perceptron
+ RandomForest

O melhor desempenho foi o do RandomForest. O modelo e o tokenizador são salvos para serem carregados pela aplicação.













