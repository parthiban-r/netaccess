# Netaccess
This is an python script for approving the netaccess login. 
The installation steps are specially for macOS and tested.

## Steps  to install 
### Dependencies 
	1. Python 
	2. Python pip
	3. Python mechanize 
	4. git
### Install on macOS
Installing python on Mac the easiest way is to use Homebrew. But you can also use easy_install.

1. Install Homebrew

`/usr/bin/ruby -e “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)`

2. Install Python 2 and pip

`brew install python2`

3. Install mechanize

`pip2 install mechanize`

4. Install git

`brew install git`

5. Clone the netaccess

`git clone https://github.com/parthiban-r/netaccess.git`

6. Change the login details at the netaccess.py file (go to cloned directory)

`un="UserName”`

`pw="Passwrod"`

7. Change netaccess.py to executable

`sudo chmod +x netaccess.py`

8. Copy the file to _usr_local/bin

`sudo cp netaccess.py /usr/local/bin`

Now you able to run the command on Terminal independent of location

`netaccss.py`


### Install on Ubuntu
Since the code in python it should work on linux also. I tested in Ubuntu 18.04

1. Install python and pip

`sudo apt-get install -y python`

`sudo apt-get install -y python-pip`

2. Install mechanize

`pip2 install mechanize`

3. Install git

`sudo apt-get install -y git`

4. Clone the netaccess

`git clone https://github.com/parthiban-r/netaccess.git`

5. Change the login details at the netaccess.py file (go to cloned directory)

`un="UserName”`

`pw="Passwrod"`

6. Change netaccess.py to executable

`sudo chmod +x netaccess.py`

7. Copy the file to _usr_bin

`sudo cp netaccess.py /usr/bin`

Now you able to run the command on Terminal independent of location

`netaccss.py`
