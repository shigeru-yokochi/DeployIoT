cd /root/DeployIoT
git pull >> /tmp/DeployIoT.log
echo `pwd` >> /tmp/DeployIoT.log
echo $PATH >> /tmp/DeployIoT.log
make >> /tmp/DeployIoT.log
#reboot
