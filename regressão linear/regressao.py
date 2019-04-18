from pandas import DataFrame
from sklearn import linear_model

Stock_Market = {'gostaDeLer': [1,1,1,0,1,0,1,0,1,1],
'criativo': [1,1,0,1,0,0,0,1,0,1],
'escrever': [1,1,1,0,1,0,1,1,0,1],
'questionador': [1,0,1,1,0,1,1,0,1,1],
'gostaDeCalculos': [0,0,0,1,1,0,0,0,0,1],
'gostaDeFazerCoisasNaPratica': [1,0,1,1,1,1,0,1,1,1],
'gostaDeTecnologia': [0,1,0,1,0,1,0,0,1,1],
'temRaciocinioLogico': [0,0,1,1,1,1,0,0,0,1],
'sePreocupaComAnimais': [1,1,1,1,0,1,1,1,1,1],
'medicina/veterinaria': [0,1,0,0,0,0,1,1,1,1],
'sePreocupaComMeioAmbiente': [1,0,1,1,0,1,1,1,1,1],
'sePreocupaComAsPessoas': [1,0,0,1,0,1,1,0,0,1],
't': [10,10,10,20,20,20,30,30,30,40],
}

df = DataFrame(Stock_Market,columns=['gostaDeLer','criativo','escrever','questionador','gostaDeCalculos','gostaDeFazerCoisasNaPratica'
,'gostaDeTecnologia','temRaciocinioLogico','sePreocupaComAnimais','medicina/veterinaria',
'sePreocupaComMeioAmbiente','sePreocupaComAsPessoas','t'])

X = df[['gostaDeLer','criativo','escrever','questionador','gostaDeCalculos',
'gostaDeFazerCoisasNaPratica','gostaDeTecnologia','temRaciocinioLogico',
'sePreocupaComAnimais','medicina/veterinaria','sePreocupaComMeioAmbiente','sePreocupaComAsPessoas']] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['t']
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept)
print('Coefficients: \n', regr.coef)

print ('Area : \n', regr.predict([[1,1,1,1,1,1,1,1,1,1,1,1]])[0])