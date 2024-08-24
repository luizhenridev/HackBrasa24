predictions = f""" 
Context:

You will analyze a dataset of transactions.
The data includes columns for document_id, date_time, value, card_number, type, mcc, state, and product.
The goal is to provide forecasts for the business owner based on this data.
Task:

Analyze the provided data to identify trends, patterns, and correlations.
Forecast future sales, customer behavior, or other relevant metrics.
Provide actionable insights and recommendations based on your analysis.
Data:

document_id	date_time	value	card_number	type	mcc	state	product
9132021237731236867	2023-05-04	72	7031240677467536384	Crédito	5499	RN	blusa
9132021237731236867	2023-05-06	120	7031240677467536384	Crédito	5499	RN	Calça
9132021237731236867	2023-05-08	250	7031240677467536384	Débito	5499	RN	Tênis
9132021237731236867	2023-05-10	80	7031240677467536384	Débito	5499	RN	Acessório
9132021237731236867	2023-05-10	90	7031240677467536384	Crédito	5499	RN	Cueca
9132021237731236867	2023-05-25	300	7031240677467536384	Crédito	5499	RN	Blusa
9132021237731236867	2023-05-07	120	7031240677467536384	Débito	5499	RN	Calça jeans
9132021237731236867	2023-05-09	250	7031240677467536384	Crédito	5499	RN	Tênis esportivo
9132021237731236867	2023-05-11	80	7031240677467536384	Débito	5499	RN	Relógio de pulso
9132021237731236867	2023-05-13	150	7031240677467536384	Crédito	5499	RN	Camisa polo
9132021237731236867	2023-05-15	300	7031240677467536384	Débito	5499	RN	Sapato social

What are the most popular products or categories?
How are sales trending over time?
Are there any seasonal patterns in sales?
What is the average customer spending per transaction?
How can we improve customer retention and loyalty?
Additional Notes:

You can use data visualization techniques to explore the data and identify patterns.
Consider using statistical models or machine learning algorithms for forecasting.
Tailor your insights and recommendations to the specific needs of the business owner.



"""