# Python program to change twilio webhook configuration.
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC49b90a3580d44dc9d4198d69d101d838"
auth_token = "38cbf0bd2df7247e015ddd110bd672b3"
client = Client(account_sid, auth_token)

# webhook = client.conversations.configuration.webhooks().fetch()
#
# print(webhook.method)
# print(webhook.__dict__)

webhook = client.conversations.configuration.webhooks().update(
    filters=["onMessageAdd", "onMessageUpdate", "onMessageRemove"],
    target="webhook",
    pre_webhook_url="https://8c9a78f8qc.execute-api.ap-south-1.amazonaws.com/PROD/message",
    post_webhook_url="https://8c9a78f8qc.execute-api.ap-south-1.amazonaws.com/PROD/message",
    method="POST",
)

print(webhook.__dict__)
