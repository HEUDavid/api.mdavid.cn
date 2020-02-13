#!/bin/sh

echo "====> start <====" &&
echo "step1: ==========================================================================================> update sources.list" &&
cd /etc/apt &&
echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free" > sources.list &&
echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free" >> sources.list &&
echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free" >> sources.list &&
echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free" >> sources.list &&
apt-get update &&

echo "step2: ==============================================================================================> apt install pkg" &&
apt-get install net-tools openssh-server vim -y &&

echo "step3: ======================================================================================================> set ssh" &&
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config &&
echo "input passwd for root plz" &&
read passwd &&
echo "root:${passwd}" | chpasswd &&
service ssh restart &&

echo "step4: ======================================================================================================> set pip" &&
cd ~ &&
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple &&

echo "step5: ==============================================================================================> pip install pkg" &&
pip install django &&
python -m django --version &&

echo "====> end <===="
