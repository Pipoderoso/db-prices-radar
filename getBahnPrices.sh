#/!bin/bash

## Dependencies:
# sudo apt install npm

## Install main repo:
# mkdir -p $HOME/lib
# cd $HOME/lib
# git clone https://github.com/juliuste/db-prices-radar.git
# cd db-prices-radar
# npm install

cd $HOME/lib/db-prices-radar
node index.js > data.json 
python3 selectData.py