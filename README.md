# DevOps Dashboard - Built with Airplane

A sample project incorporating Airplane Views, Tasks and more to allow non-technical stakeholders to create and destroy AWS EC2 instances.

![A look at the DevOps dashboard with some servers running and one shut down](https://i.imgur.com/dsgTA7I.png)

## Getting Started

Once you've cloned the repo for this project, you'll need a couple other things to get started:

  - [An Airplane account](https://app.airplane.dev/signup). Signing up for a new account will get you a 14 day free trial of the Enterprise plan, but this project will run under the Free plan as well.
  - [The Airplane CLI](https://docs.airplane.dev/platform/airplane-cli) downloaded and installed on your machine.
  - [Config variables](https://app.airplane.dev/settings/config-vars) set up and populated for `AWS_ACCESS_KEY_ID`, `AWS_DEFAULT_REGION` and `AWS_SECRET_ACCESS_KEY`.

## General Architecture

This project contains a view and three tasks:

  - [DevOps Dashboard (View)](https://github.com/kkoppenhaver/airplane-devops-dashboard/blob/main/devops_dashboard.airplane.tsx): This is the main view that renders the table containing all the AWS resources.
  - [create_aws_servers.py (Task)](https://github.com/kkoppenhaver/airplane-devops-dashboard/blob/main/tasks/create_aws_servers_airplane.py): This task is triggered when you click the "Create Server" button and uses the boto3 library to create an EC2 instance on AWS.
  - [delete_aws_servers.py (Task)](https://github.com/kkoppenhaver/airplane-devops-dashboard/blob/main/tasks/delete_aws_servers_airplane.py): This task is triggered when you click the "Delete Server" button and uses the boto3 library to delete the selected EC2 instance on AWS.
  - [view_aws_servers.py (Task)](https://github.com/kkoppenhaver/airplane-devops-dashboard/blob/main/tasks/view_aws_servers_airplane.py): This task powers the View and generates the list of EC2 instances from AWS that becomes the data table in the View.
