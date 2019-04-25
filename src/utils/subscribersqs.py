"""this is to send sqs messages"""
import boto3
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


def sqs_queue():
    """Create SQS client"""
    sqs = boto3.client('sqs')
    queue_url = os.getenv('SQS_QUEUE_URL')
    print(queue_url)
    # Send message to SQS queue
    # response = sqs.send_message(
    #     QueueUrl=queue_url,
    #     DelaySeconds=10,
    #     MessageAttributes={
    #         'Title': {
    #             'DataType': 'String',
    #             'StringValue': 'SOWJANYA'
    #         },
    #         'Author': {
    #             'DataType': 'String',
    #             'StringValue': 'SOWJANYA'
    #         },
    #         'WeeksOn': {
    #             'DataType': 'Number',
    #             'StringValue': '4'
    #         }
    #     },
    #
    #     MessageBody=(
    #         'THIS IS ICP  '
    #         'week of 12/11/2018.'
    #     )
    # )
    # print("this is SQS")
    #
    # print(response['MessageId'])

    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=10,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )
    print(response)
    message = response['Messages']

    # receipt_handle = message[0]

    # print(receipt_handle)

    # Delete received message from queue
    # sqs.delete_message(
    #     QueueUrl=queue_url,
    #     ReceiptHandle=receipt_handle
    # )
    print("messaaaaaa")
    print('Received and deleted message: %s' % message)


sqs_queue()
