# DevOps Dashboard - Built with Airplane

A sample project incorporating Airplane Views, Tasks and more to allow non-technical stakeholders to create and destroy AWS EC2 instances.

![A look at the DevOps dashboard with some servers running and one shut down](https://i.imgur.com/dsgTA7I.png)

## General Architecture

This project contains a view and three tasks:

  - DevOps Dashboard (View): This is the main view that renders the table containing all the AWS resources.
  - [create_aws_servers.py (Task)](https://github.com/kkoppenhaver/airplane-devops-dashboard/blob/main/tasks/create_aws_servers_airplane.py): This task is triggered when you click the "Create Server" button and uses the boto3 library to create an EC2 instance on AWS.
  - [delete_aws_servers.py (Task)](https://github.com/kkoppenhaver/airplane-devops-dashboard/blob/main/tasks/delete_aws_servers_airplane.py): This task is triggered when you click the "Delete Server" button and uses the boto3 library to delete the selected EC2 instance on AWS.
  - [view_aws_servers.py (Task)](https://github.com/kkoppenhaver/airplane-devops-dashboard/blob/main/tasks/view_aws_servers_airplane.py): This task powers the View and generates the list of EC2 instances from AWS that becomes the data table in the View.