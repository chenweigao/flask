#!/bin/bash
sudo apt-get install sqlite3
export DB_PATH=/usr/local/mongodb
pip3 install -r requirements.txt -i https://pypi.douban.com/simple
curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-4.0.2.tgz
tar -zxvf mongodb-linux-x86_64-ubuntu1604-4.0.2.tgz
# sudo mv mongodb-linux-x86_64-ubuntu1604-4.0.2/ /usr/local/mongodb
sudo mv mongodb-linux-x86_64-ubuntu1604-4.0.2/ DB_PATH
export PATH=/usr/local/mongodb/bin:$PATH
sudo mkdir -p /data/db
# cd /usr/local/mongodb/bin
cd DB_PATH