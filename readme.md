## Installation Instructions

1. Install python 3
2. Run package_setup.bat
3. Add the publish and subscribe keys to your credentials.ini file. All users should be using the same keys.
    * To create a new set of keys, go to https://pubnub.com, create a free account, go to keys, and create a new keyset
    * <u>NOTICE:</u> Only one user has to do this, since all users should be using the same keys
4. Run sender.py / receiver.py

## Modifying keys

1. Run settings\getKey.py
2. Press the key you'd like to use
3. change the key in settings/keys.py accordingly