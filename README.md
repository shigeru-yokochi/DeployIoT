## AWS IoTへの接続設定

カレントディレクトリにlocal_define.hを作成して内容を定義する

```c:local_define.h
#define AWS_IOT_MQTT_HOST              "xxxxxx.iot.ap-northeast-1.amazonaws.com"	//AWS IoTのエンドポイント
#define AWS_IOT_MQTT_CLIENT_ID         "raspberrypi-zero-205"						//クライアントID(AWS_IOT_MY_THING_NAMEと同じ)
#define AWS_IOT_MY_THING_NAME 	       "raspberrypi-zero-205"						//AWS IoTへ登録したThings名
#define AWS_IOT_ROOT_CA_FILENAME       "root-CA.crt"								//ルート証明書ファイル名
#define AWS_IOT_CERTIFICATE_FILENAME   "raspberrypi-zero-205.cert.pem"				//デバイス証明書ファイル名
#define AWS_IOT_PRIVATE_KEY_FILENAME   "raspberrypi-zero-205.private.key"			//プライベートキーファイル名
#define CERT_DIRECTORY	               "../aws-iot-device-sdk-embedded-C/certs"		//aws-iot-device-sdk-embedded-C/certsへの相対パス"	//Relative path from the current directory
```


## power on時に起動させる設定

/etc/rc.local に以下を設定　

```
su -c "bash /root/DeployIoT/AutoStart.sh &"
```

