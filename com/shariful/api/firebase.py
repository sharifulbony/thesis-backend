from __future__ import print_function

import datetime

from firebase_admin import messaging
import service

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("../../../data/firebase/sheba-f1a73-firebase-adminsdk-yjtrm-71783ff88a.json")
firebase_admin.initialize_app(cred)

token = 'cHfM0grKTSC7cR3Tv7d7_k:APA91bEK57W_B1WkyVLDYRYWP0-xiYKeL7IB3-dvvD79FC3qO3c1o091VM2Sq147WS0n2NQkiuU_YLBciKM-u5zmzjljHlm18QCSiGCqpSp3_AJPOGMViqXn9dbif-aNO0rRRxbVcbCp'

def getToken(id):
    data=service.get_device(id)
    # token_col = data.loc[:, 'token']
    # token=token_col.values
    # token = data['token'].to_numpy()
    # token = data['token'].to_numpy()
    token = data['token'].tolist()
    # token = data.loc[:,'token']

    return token



def sendPush(id,title, msg, dataObject=None):
    # See documentation on defining a message payload.
    registration_token = getToken(id)

    # registration_token=[
    #     'cHfM0grKTSC7cR3Tv7d7_k:APA91bEK57W_B1WkyVLDYRYWP0-xiYKeL7IB3-dvvD79FC3qO3c1o091VM2Sq147WS0n2NQkiuU_YLBciKM-u5zmzjljHlm18QCSiGCqpSp3_AJPOGMViqXn9dbif-aNO0rRRxbVcbCp'
    # ]

    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg
        ),
        data=dataObject,
        tokens=registration_token,
    )

    # Send a message to the device.csv corresponding to the provided
    # registration token.
    response = messaging.send_multicast(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)


def send_to_token():

    # [START send_to_token]
    # This registration token comes from the client FCM SDKs.
    registration_token = 'e2U7HhOMTX-7hJRAFXuXM6:APA91bH-HvejJREHyZl8qXGAH7a6UWuyTKpeqVT0n5qzuk3bhVeNhLs09VcyGZKp24hSf1Gjux621Yzcg_SDN-n3jJxOcA6JYk0ZC6a-LWNSZMpIxCXSi513IhZpMJ4d5FOr9MoaawW7'

    # See documentation on defining a message payload.
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        token=registration_token,
    )

    # Send a message to the device.csv corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
    # [END send_to_token]


def send_to_topic():
    # [START send_to_topic]
    # The topic name can be optionally prefixed with "/topics/".
    topic = 'highScores'

    # See documentation on defining a message payload.
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        topic=topic,
    )

    # Send a message to the devices subscribed to the provided topic.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
    # [END send_to_topic]


def send_to_condition():
    # [START send_to_condition]
    # Define a condition which will send to devices which are subscribed
    # to either the Google stock or the tech industry topics.
    condition = "'stock-GOOG' in topics || 'industry-tech' in topics"

    # See documentation on defining a message payload.
    message = messaging.Message(
        notification=messaging.Notification(
            title='$GOOG up 1.43% on the day',
            body='$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.',
        ),
        condition=condition,
    )

    # Send a message to devices subscribed to the combination of topics
    # specified by the provided condition.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
    # [END send_to_condition]


def send_dry_run():
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        token='token',
    )

    # [START send_dry_run]
    # Send a message in the dry run mode.
    response = messaging.send(message, dry_run=True)
    # Response is a message ID string.
    print('Dry run successful:', response)
    # [END send_dry_run]


def android_message():
    # [START android_message]
    message = messaging.Message(
        android=messaging.AndroidConfig(
            ttl=datetime.timedelta(seconds=3600),
            priority='normal',
            notification=messaging.AndroidNotification(
                title='$GOOG up 1.43% on the day',
                body='$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.',
                icon='stock_ticker_update',
                color='#f45342'
            ),
        ),
        topic='industry-tech',
    )
    # [END android_message]
    return message


def apns_message():
    # [START apns_message]
    message = messaging.Message(
        apns=messaging.APNSConfig(
            headers={'apns-priority': '10'},
            payload=messaging.APNSPayload(
                aps=messaging.Aps(
                    alert=messaging.ApsAlert(
                        title='$GOOG up 1.43% on the day',
                        body='$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.',
                    ),
                    badge=42,
                ),
            ),
        ),
        topic='industry-tech',
    )
    # [END apns_message]
    return message


def webpush_message():
    # [START webpush_message]
    message = messaging.Message(
        webpush=messaging.WebpushConfig(
            notification=messaging.WebpushNotification(
                title='$GOOG up 1.43% on the day',
                body='$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.',
                icon='https://my-server/icon.png',
            ),
        ),
        # topic='industry-tech',
    )
    # [END webpush_message]
    return message


def all_platforms_message():
    # [START multi_platforms_message]
    message = messaging.Message(
        notification=messaging.Notification(
            title='$GOOG up 1.43% on the day',
            body='$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.',
        ),
        android=messaging.AndroidConfig(
            ttl=datetime.timedelta(seconds=3600),
            priority='normal',
            notification=messaging.AndroidNotification(
                icon='stock_ticker_update',
                color='#f45342'
            ),
        ),
        apns=messaging.APNSConfig(
            payload=messaging.APNSPayload(
                aps=messaging.Aps(badge=42),
            ),
        ),
        topic='industry-tech',
    )
    # [END multi_platforms_message]
    return message


def subscribe_to_topic():
    topic = 'highScores'
    # [START subscribe]
    # These registration tokens come from the client FCM SDKs.
    registration_tokens = [
        'YOUR_REGISTRATION_TOKEN_1',
        # ...
        'YOUR_REGISTRATION_TOKEN_n',
    ]

    # Subscribe the devices corresponding to the registration tokens to the
    # topic.
    response = messaging.subscribe_to_topic(registration_tokens, topic)
    # See the TopicManagementResponse reference documentation
    # for the contents of response.
    print(response.success_count, 'tokens were subscribed successfully')
    # [END subscribe]


def unsubscribe_from_topic():
    topic = 'highScores'
    # [START unsubscribe]
    # These registration tokens come from the client FCM SDKs.
    registration_tokens = [
        'YOUR_REGISTRATION_TOKEN_1',
        # ...
        'YOUR_REGISTRATION_TOKEN_n',
    ]

    # Unubscribe the devices corresponding to the registration tokens from the
    # topic.
    response = messaging.unsubscribe_from_topic(registration_tokens, topic)
    # See the TopicManagementResponse reference documentation
    # for the contents of response.
    print(response.success_count, 'tokens were unsubscribed successfully')
    # [END unsubscribe]


def send_all():
    registration_token = 'e2U7HhOMTX-7hJRAFXuXM6:APA91bH-HvejJREHyZl8qXGAH7a6UWuyTKpeqVT0n5qzuk3bhVeNhLs09VcyGZKp24hSf1Gjux621Yzcg_SDN-n3jJxOcA6JYk0ZC6a-LWNSZMpIxCXSi513IhZpMJ4d5FOr9MoaawW7'
    # [START send_all]
    # Create a list containing up to 500 messages.
    messages = [
        messaging.Message(
            notification=messaging.Notification('Price drop', '5% off all electronics'),
            token=registration_token,
        ),
        # ...
        messaging.Message(
            notification=messaging.Notification('Price drop', '2% off all books'),
            topic='readers-club',
        ),
    ]

    response = messaging.send_all(messages)
    # See the BatchResponse reference documentation
    # for the contents of response.
    print('{0} messages were sent successfully'.format(response.success_count))
    # [END send_all]


def send_multicast():
    # [START send_multicast]
    # Create a list containing up to 500 registration tokens.
    # These registration tokens come from the client FCM SDKs.
    registration_tokens = [
        'YOUR_REGISTRATION_TOKEN_1',
        # ...
        'YOUR_REGISTRATION_TOKEN_N',
    ]

    message = messaging.MulticastMessage(
        data={'score': '850', 'time': '2:45'},
        tokens=registration_tokens,
    )
    response = messaging.send_multicast(message)
    # See the BatchResponse reference documentation
    # for the contents of response.
    print('{0} messages were sent successfully'.format(response.success_count))
    # [END send_multicast]


def send_multicast_and_handle_errors():
    # [START send_multicast_error]
    # These registration tokens come from the client FCM SDKs.
    registration_tokens = [
        'YOUR_REGISTRATION_TOKEN_1',
        # ...
        'YOUR_REGISTRATION_TOKEN_N',
    ]

    message = messaging.MulticastMessage(
        data={'score': '850', 'time': '2:45'},
        tokens=registration_tokens,
    )
    response = messaging.send_multicast(message)
    if response.failure_count > 0:
        responses = response.responses
        failed_tokens = []
        for idx, resp in enumerate(responses):
            if not resp.success:
                # The order of responses corresponds to the order of the registration tokens.
                failed_tokens.append(registration_tokens[idx])
        print('List of tokens that caused failures: {0}'.format(failed_tokens))
    # [END send_multicast_error]