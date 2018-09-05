cd /root/DeployIoT
chmod 644 AutoStart.sh
chmod 644 deploy.sh
git pull
chmod 755 AutoStart.sh
chmod 755 deploy.sh
make
reboot
