from django.apps import AppConfig


class MqttSubscriberConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MQTT_Subscriber'
