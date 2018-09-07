# 利用イメージ


![image](https://user-images.githubusercontent.com/12773136/45201856-e07c5400-b2b1-11e8-9e1c-a6eeca8dd0ac.png)

# 初期設定

## インストール

## 前提

前提として、AWS IoT Embedded C SDK のランタイム環境を構築が完了していること
https://docs.aws.amazon.com/ja_jp/iot/latest/developerguide/iot-embedded-c-sdk.html
このsdkを/root配下にインストールします

例：
cd /root
git clone https://github.com/aws/aws-iot-device-sdk-embedded-C.git -b release

## DeployIoTインストール

cd /root
git clone https://github.com/shigeru-yokochi/DeployIoT.git
cd DeployIoT


## AWS IoTへの接続設定

/root/DeployIoT にlocal_define.hを作成して内容を定義する

```c
#define AWS_IOT_MQTT_HOST              "xxxxxx.iot.ap-northeast-1.amazonaws.com"	//AWS IoTのエンドポイント
#define AWS_IOT_MQTT_CLIENT_ID         "raspberrypi-zero-205"						//クライアントID(AWS_IOT_MY_THING_NAMEと同じ)
#define AWS_IOT_MY_THING_NAME 	       "raspberrypi-zero-205"						//AWS IoTへ登録したThings名
#define AWS_IOT_ROOT_CA_FILENAME       "root-CA.crt"								//ルート証明書ファイル名
#define AWS_IOT_CERTIFICATE_FILENAME   "raspberrypi-zero-205.cert.pem"				//デバイス証明書ファイル名
#define AWS_IOT_PRIVATE_KEY_FILENAME   "raspberrypi-zero-205.private.key"			//プライベートキーファイル名
#define CERT_DIRECTORY	               "../aws-iot-device-sdk-embedded-C/certs"		//aws-iot-device-sdk-embedded-C/certsへの相対パス"
#define MQTT_TOPIC                     "sdkTest/sub"                                //MQTTトピックス名
```


## power on時に起動させる設定

/etc/rc.local に以下を設定　

```sh
su -c "bash /root/DeployIoT/AutoStart.sh &"
```

# デプロイ設定

カレントディレクトリに存在しているdeploy.txt内容を定義する

例：/root/xxxxxxにcloneされているGitHubレポジトリをpullしたあとmakeとrebootを実行する

```txt
cd /root/xxxxxx
git pull
make
reboot
```

# 参考

利用イメージ内のAWS Lambda functionコードも含んでいます

```
lambda_function.lambda_handler.py
```
