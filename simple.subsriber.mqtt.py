import paho.mqtt.client as mqtt

broker_user = "username"
broker_pwd = "password"
broker_host = "192.168.*.*"
broker_port = 1883 
subscriber_topic = "/subscribed/topic"

#callback function
def on_message(client, data, message):
    print("Subscriber:")
    print(f"topic: {subscriber_topic}, messsage received: {message.payload}")

subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
subscriber.username_pw_set(broker_user, broker_pwd)
subscriber.connect(broker_host, broker_port)
subscriber.on_message = on_message

subscriber.subscribe(subscriber_topic)

subscriber.loop_forever()
