# Mlops-task3
#Creating DockerFile to run our ML model under supervision of Jenkins Jobs
This repository is created to publish mlops Task3.



We will see how we can automate the entire process of launching Jenkins from docker container and deploy the code from the Github
let’s start — —>
1:.Creating container image that’s has Jenkins installed using Dockerfile

2. When we launch the our above created customized image it should launch Jenkins

3. Creation of a job chain of job1, job2, job3 and job4 using build pipeline plugin in Jenkins

4. Job1 : Getting the Github repo automatically when the developer pushes the repo into Github

5. Job2 : By looking at the code or program file, Jenkins should automatically start the respective language interpreter install image container to deploy code.

6. Job3 : Test your app if it is working or not.

7. Job4 : if app is not working , then send email to developer with error messages.

8. Create One extra job job5 for monitor : If container where app is running. fails due to any reson then this job should automatically start the container again.

creating a customized image using docker now we run the container using the command [sudo service jenkins start] once the container is launched.now we will go to jenkins and start creating new job

by using a trigger method we will create a Github trigger where Jenkins automatically pull the data as soon as the Developer push the code,using the Github Hooks


