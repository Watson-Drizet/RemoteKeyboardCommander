from pubnub.callbacks import SubscribeCallback
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub


class _MySubscribeCallback(SubscribeCallback):
    _message = None

    def presence(self, pubnub, presence):
        pass

    def status(self, pubnub, status):
        pass

    def message(self, pubnub, message):
        _MySubscribeCallback._message = message.message
        print("Received: " + message.message, end=" - ")

    @staticmethod
    def get_msg_and_empty():
        result = _MySubscribeCallback._message
        _MySubscribeCallback._message = None
        return result


class PubNubManager:
    channel = "chan-1"

    _pnconfig = PNConfiguration()
    _pnconfig.publish_key = 'pub-c-dd5c661f-ba65-4081-815a-04dc3eac0296'  # TODO Move to a separate file
    _pnconfig.subscribe_key = 'sub-c-4f073e42-a145-11eb-8d7b-b642bba3de20'
    _pnconfig.ssl = True
    _pubnub = PubNub(_pnconfig)
    _pubnub.add_listener(_MySubscribeCallback())
    _pubnub.subscribe().channels(channel).execute()

    @staticmethod
    def send(message: str):
        if message is not None:
            PubNubManager._pubnub.publish() \
                .channel(PubNubManager.channel) \
                .message(str(message)) \
                .pn_async(PubNubManager._my_publish_callback)

    @staticmethod
    def receive():
        PubNubManager._pubnub.publish() \
            .channel(PubNubManager.channel) \
            .pn_async(PubNubManager._my_publish_callback)

        return _MySubscribeCallback.get_msg_and_empty()

    @staticmethod
    def _my_publish_callback(envelope, status):
        # Check whether request successfully completed or not
        if not status.is_error():
            pass
