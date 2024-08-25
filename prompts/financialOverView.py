overView = """" 
Prompt:

Context:

You will analyze a dataset of financial transactions.
The data includes columns for index, document_id, date_time, value, counterparty_document, and type.
The goal is to provide a comprehensive financial overview of the business based on this data.
Pix-in is when the user receive money
Pix-out is when the user send money 
Task:

Calculate key financial metrics such as total revenue, total expenses, net income, and profit margin.
Analyze transaction trends over time, including seasonal patterns and growth rates.
Identify any significant outliers or anomalies in the data.
Provide insights into the business's financial health and areas for improvement.
Data:

document_id	date_time	value	counterparty_document	type
9132021237731236867	2023-05-04	72	aff0bf3b-11bc-4ffd-bba7-fd3b0e8c05b4	pix_in
9132021237731236867	2023-05-06	120	25b970c0-8566-41e6-bd9a-c4d2e843fe17	pix_in
9132021237731236867	2023-05-08	250	0148c169-db8d-4f09-9fbe-115cc1f8eeef	pix_in
9132021237731236867	2023-05-10	80	c927e343-f37a-43d5-bfcd-a7e69f34c550	pix_in
9132021237731236867	2023-05-10	90	4c8938c6-82df-4cf9-90ec-488a98be3db9	pix_in
9132021237731236867	2023-05-25	300	619856a4-ac43-4188-b9b0-6dde265d321b	pix_in
9132021237731236867	2023-05-07	120	9b48ec96-2934-4402-be52-39e916ea9dda	pix_in
9132021237731236867	2023-05-09	250	2a450503-879e-46c6-b124-d9cf36fef29f	pix_in
9132021237731236867	2023-05-11	80	2382b62a-0dd5-4528-99b8-96ded82e6c08	pix_in
9132021237731236867	2023-05-13	150	a7c86ec4-c81f-4750-b3bf-24ea0118fe66	pix_in
9132021237731236867	2023-05-15	300	9369b7b4-4edc-4c24-8428-4f38dbda3826	pix_in
9132021237731236867	16/05/2023  100	d02fd727-05c6-4b51-96b6-adf97a50c841	pix_out

What is the overall financial performance of the business?
Are there any significant trends in revenue or expenses?
Are there any areas where costs can be reduced?
How does the business compare to industry benchmarks?

"""