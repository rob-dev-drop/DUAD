sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]

final_result = {

}

purchase_tracker_upc = [

]

purchase_tracker_price = [

]

for index in sales:
    purchaselist = index.get('items')
    for index2 in purchaselist:
        purchase_upc = index2.get('upc')
        purchase_price = index2.get('unit_price')
        purchase_tracker_upc.append(purchase_upc)
        purchase_tracker_price.append(purchase_price)


for upc in range(0, len(purchase_tracker_upc)):
    if purchase_tracker_upc[upc] not in final_result:
        final_result[purchase_tracker_upc[upc]] = purchase_tracker_price[upc]
    else:
        final_result[purchase_tracker_upc[upc]] += purchase_tracker_price[upc]

print(final_result)    

#Cree un diccionario que guarde el total de ventas de cada UPC.