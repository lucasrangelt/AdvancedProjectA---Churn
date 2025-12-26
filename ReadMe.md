# Introdução
Esse projeto de análise de churn serve para verificar as possíveis causas das evasões (cancelamentos) pela parte de clientes, e tentar entender como diminuir essas evasões.

Trabalharemos com uma tabela CSV de uma empresa de telecomunicações onde há diversas informações sobre clientes, como dados demográficos, serviços escolhidos, métodos de pagamento, taxas, se há evasão ou não e há quanto tempo o cliente está assinando o serviço até o momento da análise. A tabela utilizada é de domínio público e se encontra pelo seguinte link: [https://www.kaggle.com/datasets/blastchar/telco-customer-churn]

# Ferramentas que Usei
- Usei ***GIT/GitHub*** para subir meu projeto para o repositório e torná-lo público, facilitando assim o acesso de todos.
- Usei ***SQL*** para criar uma tabela dentro do PostgreSQL com todos os dados extraídos do arquivo principal.
- Usei ***Excel*** para rapidamente ter referência das colunas, seus nomes e seus tipos de dados.
- Usei ***Python*** e suas bibliotecas numpy, pandas e matplotlib para trabalhar com o dataframe do arquivo, modelar dados criando colunas e alterando formatos, criar gráficos e estabelecer taxas de churning relacionando a coluna de churn com as demais.
- Usei ***Power BI*** para organizar, visualizar, modelar e analisar os dados coletados, aprofundando os resultados obtidos com o gráficos no python.
- Usei ***VS Code*** para criar e editar o arquivo ReadMe.md, trabalhar nos arquivos SQL, Python e estabelecer Source Control.

# O que é e por que falar sobre churn?

O churn nada mais é do que a evasão ou cancelamento dos serviços da empresa por parte de um cliente. Em forma mais popular, "perder o cliente" seria um termo mais utilizado.

É muito mais caro trazer um cliente novo do que manter um cliente existente. Perder clientes significa deixar de ter ganhos e ainda ter que aumentar os gastos com propaganda (marketing) a fim de compensar o cliente perdido. Lidar com o churn, portanto, é uma das tarefas mais importantes de uma empresa em relação a seus clientes. Essa é uma tarefa complexa que recai geralmente sobre as equipes de marketing, desenvolvimento de produto, suporte ao cliente e áreas afins.

A liderança da empresa toma as melhores medidas baseado nas sugestões de um analista (de dados ou negócios), que surgem a partir de um levantamento de dados sobre os clientes da empresa.

# Levantamento de Dados
Esse projeto se dividirá em três partes: O início em SQL e mais os resultados e relações entre colunas em Python, os aprofundamentos e análises em Power BI, e a confirmação dessas análises utilizando um modelo de regressão logística novamente em python.

Antes de qualquer coisa, caso precisemos expandir nossa base ou fazer queries nela, criaremos uma tabela com esses dados no PostgreSQL. O arquivo "**0-CSVtoPSQL.sql**" no repositório mostra como isso é feito.

Logo, vamos fazer duas queries simples de seleção de dados a fim de obter a informação sobre a proporção de churn. Essas queries se encontram no arquivo "**1-queries-rawchurn.sql**".

A primeira query:
```sql
SELECT
    CASE
        WHEN churn = TRUE THEN 'True values'
        WHEN churn = FALSE THEN 'False values'
        ELSE 'Null values'
    END AS title,
    COUNT(churn) AS totalvalues,
    SUM(totalcharges) AS sumvalues
FROM
    churntable
GROUP BY
    title
```
traz o seguinte resultado (output):

![1.1-query1-output](1.1-query1-output.png)

A segunda query, busca estabelecer a proporção geral de evasão entre os clientes que deram churn e o total de clientes:
```
SELECT
    AVG(CASE WHEN churn = TRUE THEN 1.0 ELSE 0.0 END) AS churn_rate
FROM
    churntable
```
e traz o seguinte resultado:

![1.2-query1-output](1.2-query2-output.png)

Para facilitar nosso trabalho, importaremos o arquivo CSV original para o Excel ("**2-demonstration-table.xlsx**"), a fim de visualizar os nomes das colunas e tipos de arquivos. Esse arquivo em Excel não terá muito uso além disso, e continuaremos referenciando o arquivo original em CSV.

Entrando na segunda parte da análise, trabalharemos com as bibliotecas python a fim de obter gráficos de relações entre a coluna churn e as demais. Mais precisamente, após ler o arquivo CSV e fazer algumas modificações, o nosso objetivo será de obter as taxas de churn por coluna, dividindo o número de clientes que deram churn pelo número total de clientes por coluna. os valores, após printados, aparecem como mostra o arquivo "**3.1-python-churn-groups.txt**":
```
TenureGroup
Less than 6 months    1481
More than 5 years     1407
1 to 2 years          1024
2 to 3 years           832
4 to 5 years           832
3 to 4 years           762
6 months to 1 year     705
gender
Female    0.269209
Male      0.261603
Name: count, dtype: float64 SeniorCitizen
0    0.236062
1    0.416813
Name: count, dtype: float64 Partner
No     0.329580
Yes    0.196649
Name: count, dtype: float64 Dependents
No     0.312791
Yes    0.154502
Name: count, dtype: float64 TenureGroup
Less than 6 months    0.529372
6 months to 1 year    0.358865
1 to 2 years          0.287109
2 to 3 years          0.216346
3 to 4 years          0.190289
4 to 5 years          0.144231
More than 5 years     0.066098
Name: count, dtype: float64 PhoneService
Yes    0.267096
No     0.249267
Name: count, dtype: float64 MultipleLines
No                  0.250442
No phone service    0.249267
Yes                 0.286099
Name: count, dtype: float64 InternetService
Fiber optic    0.418928
DSL            0.189591
No             0.074050
Name: count, dtype: float64 OnlineSecurity
No                     0.417667
Yes                    0.146112
No internet service    0.074050
Name: count, dtype: float64 OnlineBackup
No                     0.399288
Yes                    0.215315
No internet service    0.074050
Name: count, dtype: float64 DeviceProtection
No                     0.391276
Yes                    0.225021
No internet service    0.074050
Name: count, dtype: float64 TechSupport
No                     0.416355
Yes                    0.151663
No internet service    0.074050
Name: count, dtype: float64 StreamingTV
No                     0.335231
Yes                    0.300702
No internet service    0.074050
Name: count, dtype: float64 StreamingMovies
No                     0.336804
Yes                    0.299414
No internet service    0.074050
Name: count, dtype: float64 Contract
Month-to-month    0.427097
One year          0.112695
Name: count, dtype: float64 PaperlessBilling
Yes    0.335651
No     0.163301
Name: count, dtype: float64 PaymentMethod
Electronic check             0.452854
Mailed check                 0.191067
Bank transfer (automatic)    0.167098
Credit card (automatic)      0.152431
Name: count, dtype: float64 MonthlyGroup
Higher Than Average    0.345399
Lower Than Average     0.164744
Name: count, dtype: float64 TotalGroup
Lower Than Average     0.316890
Higher Than Average    0.179652
```

Em seguida, vamos ignorar algumas colunas com valores parecidos e focar onde há diferença significativa de churn. Prepararemos três plots (gráficos) para visualizar melhor essas diferenças em taxas. O código está no arquivo "**3-python-pandas-plots.py**", e as plots são as seguintes:
![py_plots_p1](py_plots_p1.png)
![py_plots_p2](py_plots_p2.png)
![py_plots_p3](py_plots_p3.png)

Agora, no Power BI, criaremos 6 páginas para melhor estudar o churn por: Demografia, Serviços, Pagamentos, Permanência, Taxas Mensais e Dispersão de Clientes por Taxas Totais.

Após alguns ajustes, adições de colunas usando o Power Query e formatando gráficos, temos as informações necessárias para as páginas.

Teremos também um pequeno gráfico no canto superior direito das três primeiras páginas a fim de analisar as taxas totais dos clientes conforme selecionamos nossos dados.

# Análise e Soluções

![pbi_1](pbi_1.png)
Nas queries em SQL, vemos uma considerável taxa total de churn de 26,5%. Todos esses gráficos e plots nos mostram os itens que mais afetam o churn de clientes. O ideal é sempre focar em fatores que estão dentro do controle da empresa. Nos gráficos de demografia, logo vemos que o número de idosos que cancelam o serviço é disproporcionalmente mais elevado (quase duas vezes maior) do que o número de não-idosos que cancelam o serviço.

A causa disso é provavelmente a velocidade e complexidade da tecnologia que avança cada vez mais e algumas pessoas não conseguem acompanhar. Há de verificar também a eficiência do suporte técnico, pois algumas equipes podem não ter um treinamento adequado para com esse grupo. Uma solução para isso, seria a criação de planos simplificados e específicos para o público sênior.

Ainda em demografia, vemos que pessoas sem parceiros ou dependentes tendem a dar mais churn. Pode-se criar ou melhorar um plano ou benefícios para uso individual, baseado na disponibilidade da empresa.

![pbi_2](pbi_2.png)
Em serviços, vimos que clientes que instalam fibra ótica tem uma taxa de evasão maior, embora o serviço seja superior. Apesar de ser um mercado competitivo onde vários clientes estejam mudando de serviço todos os dias, a empresa deve assegurar a qualidade do seu próprio serviço de fibra, incluindo suporte técnico.

Também o número de clientes que escolhem não contratar os serviços extras, como backup online e suporte técnico tendem a dar o dobro de churn do que os que contratam. Há duas hipóteses: a primeira é que esse tipo de cliente já contrata o serviço buscando tal flexibilidade. A segunda hipótese é que a falta deles causa o churn. Em ambos os casos (principalmente no segundo), deve-se verificar a possibilidade de upselling (isto é, a venda casada desses serviços).

![pbi_3](pbi_3.png)
![pbi_4](pbi_4.png)
Na página seguinte, vemos os clientes por tipo de pagamento. Em questões de quantidade, muito mais clientes assinam contratos mensais e dão churn, quando comparados a contratos de um ano ou dois. No próximo gráfico, que é o de permanência, também vemos que a esmagadora maioria dos clientes que dão churn o fazem nos primeiros meses de serviço. Juntando essas duas informações, podemos propôr oferecer descontos ou serviços gratuitos nos contratos de tempo maior após o término dos contratos mensais.

![pbi_5](pbi_5.png)
Na página de taxas mensais, o fato de valores baixos, como 10, terem uma proporção significativa de churn pode implicar baixa qualidade dos serviços básicos. Taxas mensais mais altas tem proporções extremamente voláteis, de 7% a 40%, e a primeira vista essas proporções são independentes do preço. Ou seja, sozinho esse gráfico não se sustenta e isso mostra que os clientes dão mais churn baseado no serviço ofertado do que no preço que pagam por ele.

![pbi_6](pbi_6.png)
Na última página, temos o a quantidade de clientes por taxas totais e o tamanho dos pontos indicam a quantidade de churn. O ideal é que os pontos estejam cada vez menores conforme as taxas aumentam comparados aos pontos anteriores na mesma altura (quantidade de clientes). Realmente é o que acontece no gráfico na maior parte das vezes. Essa visualização serve para perceber que os clientes que dão churn geralmente são os que pagaram uma taxa total menor, embora ainda haja um número considerável na casa dos milhares que terminou o serviço. Porém, não há decisões para se tomar nessa parte, visto que taxa total é meramente uma consequência e esses últimos valores são apenas para fins de análise.

Um passo extra ideal seriam estudos de causalidade. Isto é, pequenas pesquisas com clientes que estão cancelando o serviço para saber o motivo a fim de se ter uma análise mais completa e tomar melhores decisões.

# Confirmação e/ou retificação das análises

Voltando ao python, chega então a hora de verificar nossas análises. Isso é feito através de um modelo de regressão logística, cujo objetivo é nos permitir interpretar a influência de cada variável através de uma lista de razão de chances. Adicionalmente obteremos métricas de classificação do modelo para testes em clientes futuros, além de uma matriz de confusão que reflete esse modelo.

Antes disso, ocorrerá uma limpeza de dados específica para essa tarefa, onde mesclaremos os valores "No internet service" e "No phone service" com os valores "No", a fim de reduzir redundância.

Após criar, treinar e testar o modelo com as colunas relevantes temos então o resultado na imagem a seguir, com os coeficientes logarítmicos (log-odds) já convertidos em razões de chances.

![logreg_output.png](logreg_output.png)
Valores acima de 1 significa um aumento na probabilidade de churn enquanto que abaixo significa uma diminuição.

Ao analisar os valores, logo vemos que a taxa de churn para quem assina o serviço de fibra ótica é aproximadamente 2.44 ou 144% maior do que a base (isto é, quem assina DSL), o que comprova nossa análise anterior.

O fato de um cliente ter dependentes diminui a taxa de churn em aproximadamente 15%, como mostra a imagem, mas o fato de ter parceiros não muda praticamente nada. Isso sugere que essas análises iniciais sofreram com a multicolinearidade, e talvez seja melhor usar os recursos da empresa com outros clientes.

Quanto aos clientes idosos, percebe-se um aumento de 17% na probabilidade de churn, o que comprova nossa análise de que idosos cancelam com mais frequência, mas não é um número tão grande quanto o imaginado.

A lista também mostra que clientes que contratam os serviços como segurança online, backup, etc. tem menos chances de cancelar, comprovando nossa análise. Porém, os que contratam serviços de streaming tem chances muito maiores de darem churn, com um aumento de 30% para StreamingTV e 45% para StreamingMovies.

E por último, concluímos que os contratos realmente diminuem absurdamente a quantidade de churn, com o contrato de um ano reduzindo a probabilidade base em 50% e o contrato de dois anos reduz em 77%. O tempo de permanência também reduz em 53% a chances de churn a cada desvio padrão (nesse caso, seria cerca de 24 meses).

Quanto aos outros elementos da imagem, logo abaixo da lista, temos as métricas de classificação. Pelo fato de o modelo se basear em uma tabela de churn com muito mais clientes permanecendo do que saindo, temos um desbalanceamento de classe. Por isso, foi usado o atributo class_weight="balanced" que busca atribuir a mesma importância tanto para clientes que dão churn quanto para os que não dão. Isso sacrifica um pouco da precisão para obter mais recall nos clientes que dão churn.

No final da imagem temos uma simples matriz de confusão.

# Dados para Stakeholders

Se, após todas as recomendações, a taxa de churn for reduzida de 26,5% para 22% (o que é uma projeção conservadora), isso seria uma redução de 1869 para 1549 clientes que deram churn, o que evita a perda de 320 clientes.

Como cada cliente que deu churn corresponde a um rendimento médio mensal de $74,44, então há uma retenção de $23820 sem contar o custo de aquisição de clientes que também não precisará ser gasto para compensar 320 clientes que teriam saído.

Há também o valor de vida médio por cliente. Nesse caso, usando a fórmula (Taxas mensais de churn / Taxa de churn), veremos que antes das recomendações temos um valor de 280,90. Após as recomendações esse valor sobe para 338,36, o que corresponde a um aumento de 20,5% de valor médio por cliente.

# O Que Aprendi e Conclusões

Aprendi a utilizar o editor do Power Query no Power BI, melhorei meus conhecimentos práticos sobre pandas e matplotlib, SQL, e ferramentas gerais dentro do próprio Power BI. Personalizei as páginas a fim de deixá-las limpas e fáceis de se visualizar. Soube escolher dados relevantes no processo de levantamento de dados.

Fiz minhas análises causais, com hipóteses baseadas nos dados cruzados do arquivo principal CSV. Elaborei soluções a fim de amenizar o churn com base nas análises feitas, e por último verifiquei minhas análises utilizando um modelo de regressão logística, corrigindo as necessárias e confirmando as corretas.