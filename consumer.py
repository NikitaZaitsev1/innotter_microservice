import pika, json

from app.schemas.stats import Stats

from logics.manage_db import manage_db

params = pika.URLParameters('amqps://qqrcvbgr:Ptu8OHLHnbTjVG2SoNSxVAuQoZaqC9VE@moose.rmq.cloudamqp.com/qqrcvbgr')
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='microservice')


def callback(ch, method, properties, body):
    data = json.loads(body)
    stats = Stats.parse_raw(data)  # Get data for DynamoDB

    manage_db('stats_db', stats.user_id, stats.action)  # Send data to DynamoDB


channel.basic_consume(queue='microservice', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
channel.close()
