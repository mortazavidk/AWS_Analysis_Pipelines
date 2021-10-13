# Modifed by Mahmood Mortazavi Dehkordi 

import boto3
import time
import json
import decimal

# DynamoDB setup
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ordershistorytable')

# Kinesis setup
kinesis = boto3.client("kinesis")
shard_id = ""  # will be replaced with the configuration management module
pre_shard_it = kinesis.get_shard_iterator(StreamName="ordershistorystream", ShardId=shard_id, ShardIteratorType="LATEST")
shard_it = pre_shard_it["ShardIterator"]

while True:
	out = kinesis.get_records(ShardIterator=shard_it, Limit=100)
	for record in out['Records']:
		data = json.loads(record['Data'])
		invoice = data['InvoiceNo']
		customer = int(data['Customer'])
		orderDate = data['InvoiceDate']
		quantity = data['Quantity']
		description = data['Description']
		unitPrice = data['UnitPrice']
		country = data['Country'].rstrip()
		stockCode = data['StockCode']

		# Construct a unique sort key
		orderID = invoice + "-" + stockCode

		response = table.put_item(
			Item = {
				'CustomerID': decimal.Decimal(customer),
				'OrderID': orderID,
				'OrderDate': orderDate,
				'Quantity': decimal.Decimal(quantity),
				'UnitPrice': decimal.Decimal(unitPrice),
				'Description': description,
				'Country': country
			}
		)

	shard_it = out["NextShardIterator"]
	time.sleep(1.0)

