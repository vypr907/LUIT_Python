#!/usr/bin/env python3.7

# --------------------------------------------------------------
# Program: MessageQueue
# Programmer: Steven Laszloffy
# Project: LUIT Week 17
# Purpose: Creates an SQS queue to recieve messages from a Lambda
# - messages will contain current time or random number
# -
# ---------------------------------------------------------------

import boto3


#create SQS client object
client = boto3.client('sqs')

resp = client.create_queue(
    QueueName='randomNumQ')