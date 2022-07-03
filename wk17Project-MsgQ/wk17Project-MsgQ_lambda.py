#!/usr/bin/env python3.7

# --------------------------------------------------------------
# Program: MsgQ_lambda
# Programmer: Steven Laszloffy
# Project: LUIT Week 17
# Purpose: Code for lambda. Sends message to SQS queue.
# - messages will contain current time or random number
# ---------------------------------------------------------------

import boto3
import random

#create variables
randNum = 0
message = ""

#create boto3 SQS object
sqs = boto3.resource('sqs')
q = sqs.get_queue_url(QueueName='randomNumQ')

#create lambda handler
def lambda_handler(event, context):
    
    #generate a random number
    randNum = random.randint(0,1000)
    
    #create message
    message = "Your random number is: "+str(randNum)

    #send message
    response = sqs.send_message(
        QueueUrl=q['QueueUrl'],
        MessageBody=message,
        )
        
    