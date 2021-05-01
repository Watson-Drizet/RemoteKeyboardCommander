from pubnub.callbacks import SubscribeCallback
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from inner.utils import Utils


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

    config = Utils.load_ini_file(r"credentials.ini")
    _pnconfig.publish_key = config.get("PubNub", "publish_key")
    _pnconfig.subscribe_key = config.get("PubNub", "subscribe_key")

    if _pnconfig.publish_key == "" or _pnconfig.subscribe_key == "":
        raise ValueError(
            "The inner\\credentials.ini file is missing the publish key and / or the subscribe key.\n"
            "Create your publish and subscribe key from https://www.pubnub.com/docs/quickstarts/python\n"
            "All users must use the same publish and subscription keys")

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
