
## power on時に起動させる設定

/etc/rc.local に以下を設定　

```
su -c "bash /root/DeployIoT/AutoStart.sh &"
```