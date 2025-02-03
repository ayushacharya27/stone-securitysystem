# NgRok Custom Domain Setup Guide

This guide walks you through setting up a custom Domain Setup Guide for Your Ngrok Site.

## Prerequisites

Make sure the following are installed on your system:
- ngrok
- flask-ngrok
- Remember Your Auth key For ngrok Domain
 

## Setup

Now you may find Your domain like this : 
```bash
clear-macaque-recently.ngrok-free.app
```

Now Open Your ngrok.yml file in Your PC , generally it is found in ~/.config/ngrok/ngrok.yml

Copy Paste this text:
```bash
version: "2"
authtoken: Your Auth Token
tunnels:
  flask-app:
    addr: 5000          # Change it According to Port where your Flask app runs
    proto: http
    hostname: clear-macaque-recently.ngrok-free.app  # Your static subdomain , change it According to Your needs
```
Now Run Your app.exe in one terminal
And in Other Terminal 
```bash
ngrok start flask-app
```
