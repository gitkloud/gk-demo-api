# Python Fast API for Gitkloud Mini Project

Python Fast API

## Pre-requisites

1. Python Version(python3.10)
2. pip/pip3 (package manager for python development/runtime)

## Setup
1. Create a venv
    ```bash
    python3.10 -m venv  .venv

    source .venv/bin/activate (linux/mac/unix users)
    source.bat .venv\bin\Activate.ps1 (windows users)
    ```

2. Install dependencies
    ```
    pip install -r requirements.txt
    ```

3. Linting
    ```
    pylint src/*
    ```

3. Unit tests
    ```
    pytest -v
    ```

4. Running the app
    ```
    python src/main.py
    ```

5. Accessing the app
    ```
    http://localhost:8000 ---> app
    http://localhost:8000/docs ----> API Document
    ```

CICD Pipeline

CI - Continous Integration
CD - Continous delivery

CI Process
    - Checkout SCM
    - Lint
    - Unit Test
    - Sonar( Opt)
    - Package ( we package as a zip `gk-demo-api-1.0.0.zip` )
    - Publish ( Push to Artifactory(s3, nexus, jfrog)

CD Process
    - deploy_to_dev
            (
                1. pull the artifact(.zip) from artifactory(s3)
                2. unzip it
                3. ship it to deploy target(Ec2 instance)
                4. Install deps
                5. Run the app
            )

* Jenkins
* Setup basic needs for jenkins


~/.jenkins

Server
1. Dev 
    -> Ubuntu
            1. Python3+
                sudo apt install python3.12 -y
            2. Pip
                sudo apt install python3-pip -y
            3. sudo pip install -r requirements.txt

            4. Setup a Service File (help to run ur program using system process)

 QA
 UAT
 Prod


[Unit]
Description=GK Demo API Services
After=multi-user.target

[Service]
Type=simple
Restart=always
WorkingDirectory=/home/ubuntu/app/
ExecStart=/usr/bin/python3 /home/ubuntu/app/src/main.py

[Install]
WantedBy=multi-user.target


vi /lib/systemd/system/gk.service

sudo systemctl daemon-reload
 it will load our service file to OS

sudo systemctl enable gk.service

sudo systemctl start gk.service

sudo systemctl stop gk.service

sudo systemctl restart gk.service


44.202.106.203
