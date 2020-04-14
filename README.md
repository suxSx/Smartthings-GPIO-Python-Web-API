<!-- PROJECT LOGO -->
<!-- ![Imgur](https://imgur.com/0vZ3oHn.png) -->

<!-- SHIELDS -->
<!-- 
*** Template uses shields from https://shields.io/ visit 
*** and create your own if your not happy with the few 
*** selected. For the ones here, you can change 
*** awsome-template-repository to the name of your project.
-->

![GitHub forks](https://img.shields.io/github/forks/suxsx/Smartthings-GPIO-Python-Web-API)
![GitHub stars](https://img.shields.io/github/stars/suxsx/Smartthings-GPIO-Python-Web-API)
![GitHub watchers](https://img.shields.io/github/watchers/suxsx/Smartthings-GPIO-Python-Web-API)
![GitHub](https://img.shields.io/github/license/suxsx/Smartthings-GPIO-Python-Web-API)
![GitHub issues](https://img.shields.io/github/issues/suxsx/Smartthings-GPIO-Python-Web-API)
![GitHub repo size](https://img.shields.io/github/repo-size/suxsx/Smartthings-GPIO-Python-Web-API)

<!-- ABOUT THE PROJECT -->
# Python-Web-API
Easy script for setting up your own Python Web API. Used for communicating with Raspberry PI from Smartthings. It makes it possible for you to turn on and off GPIO pins on your Raspberry PI from Smartthings and integrated your home system to your local Rasperry PI. Or modify it to run any actions you would like.

<!-- SCREEN SHOT FROM THE PROGRAM -->
![Imgur](https://imgur.com/M9Zm5T7.png)


<!-- HOW TO INSTALL -->
## How to install
Download the files locatated in Python-Web-API: ***python-api.py and options.py***. Save them in any folder and run python-api.py
```cmd
sudo python python-api.py
```

Install a new Device Handler in Smartthings using the code found in Smartthings Device Handler ***switch_device_handler_smartthings.groovy***. Add a new device and use ***WEB Service Switch*** as the device type. Do all this from samsungs web portal. 

Open the new device on your Smartthings APP, find settings and enter the IP adress to your Raspberry PI and PORT. 

***NB! This program only works on LAN. You can modify the code if you want to run it on WAN.***


<!-- BASIC INFORMATION YOU NEED TO KNOW -->
## Common Information
Basic information about the project like founding, TODO, CODE of Conduct with a short information text describing it all. 
- Look at TODO if you want to help: [TODO](TODO.md) <br />
- Read the CODE of Conduct before you edit: [Code of Conduct](CODE_OF_CONDUCT.md)<br />
- We use MIT License: [MIT](LICENSE.md)


<!-- CONTACT -->
## Contact
Project Link: [https://github.com/suxsx/Python-Web-API](https://github.com/suxsx/Smartthings-GPIO-Python-Web-API)