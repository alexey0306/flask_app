# Introduction
This document contains all the information required to deploy and run LM components in AWS cloud. 

# Table of Contents
- [Infrastructure as a Code](#infrastructure-as-a-code)
- [Terraform](#terraform)
- [Terragrunt](#terragrunt)
- [Installing Terraform and Terragrunt](#installing-terraform-and-terragrunt)
- [Configuring AWS](#configuring-aws)
- [Creating S3 backend](#creating-s3-backend)

# Infrastructure as a Code (IaC)
What is Infrastructure as a Code? IaC is the process of managing and provisioning infrastructure through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools. It can use either scripts or declarative definitions, rather than manual processes

# Terraform
Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions.

Configuration files describe to Terraform the components needed to run a single application or your entire Infrastructure. Terraform generates an execution plan describing what it will do to reach the desired state, and then executes it to build the described infrastructure. As the configuration changes, Terraform is able to determine what changed and create incremental execution plans which can be applied.

The infrastructure Terraform can manage includes low-level components such as compute instances, storage, and networking, as well as high-level components such as DNS entries, SaaS features, etc.

For more information about Terraform check the [official documentation](https://terraform.io)

# Terragrunt
Terragrunt is a thin wrapper that provides extra tools for keeping your configurations DRY, working with multiple Terraform modules, and managing remote state.

# Installing Terraform and Terragrunt
In this section you will find information how to install **Terraform** and **Terragrunt**, tools required to work with LM IaC

## Step 1. Installing Terraform

### Installing Terraform on Linux

**Ubuntu**:
```
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install terraform
```

**CentOS/RHEL**
```
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo yum -y install terraform
```

### Installing Terraform on Mac

1. Download the package from [here](https://www.terraform.io/downloads.html)
2. Move the Downloaded file to **/usr/local/bin** folder
   ```
      cd /Users/<username>/Downloads/terraform_<version>.zip
      mv /Users/<username>/Downloads/terraform /usr/local/bin/terraform
   ```

### Installing Terraform on Windows
Check [here](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started)

## Step 2. Verify Terraform installation
To verify that Terraform has been successfully installed and properly configured type the following command: 
```
terraform -help
```

## Step 3. Installing Terragrunt
In this section we're going to install **Terragrunt**, Terraform wrapper used in the LM project to create multiple environments. To install Terragrunt please follow these steps:

1. Go to [Releases](https://github.com/gruntwork-io/terragrunt/releases) page and download corresponding package
2. Rename the downloaded file to **terragrunt**
3. Add execute permissions to this file
4. Move this file to the any directory, configured in your **PATH**
5. Verify that Terragrunt has been successfully installed
   ```
      terragrunt -help
   ```
   
Ok, we're finished with installing the required tools, so let's configure the Terraform and Terragrunt to work with AWS. 


# Configuring AWS
Terraform supports multiple providers. For LM deployment we're going to use **Amazon Web Services**. To interact with our AWS Infrastructure **Terraform/Terragrunt** requires **Access Keys**. In the section below we're going to install AWS CLI tools, configure the AWS profile and configure Terraform/Terragrunt to use this profile (and its credentials) to interact with our AWS infra. 

- [Installing AWS CLI](#installing-aws-cli)
- [Creating IAM user for Terraform](#creating-iam-user-for-terraform)
- [Configuring AWS profile](#configuring-aws-profile)
- [Configuring Terraform to use AWS](#configuring-terraform-to-use-aws)

## Installing AWS CLI
The AWS Command Line Interface (CLI) is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts. In this step we're going to install **AWS CLI Version 2** on your machine. 

### Linux

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

### MacOS

1. Download the package from [here](https://awscli.amazonaws.com/AWSCLIV2.pkg)
2. Verify the installation
```
which aws
aws --version
```

### Windows
1. Download package from [here](https://awscli.amazonaws.com/AWSCLIV2.msi)
2. Verify the installation
```
aws --version
```

## Creating IAM user for Terraform.
It's recommended to create a separate IAM user for Terraform with its own credentials. To create an IAM user please follow these steps:

1. [Login](https://console.aws.amazon.com) to AWS Console
2. Go to IAM service
3. On the left panel click **Users**
4. Click **Add user** button
5. In the **User name** field type **terraform**
6. In the **Select AWS access type** check only **Programmatic access**. Click **Next**
7. In the Next window give this user the **Administrator** access rights. It can be done in multiple ways and it depends on your current configuration. Click **Next**
8. Click **Next**
9. Review your configuration and if everything is ok, click **Create User**
10. Once the user is created download the **CSV file with credentials**. 

## Configuring AWS profile
In this section we're going to configure the AWS profile. Basically profile consists of credentials, default region and some additional information. To create the profile type the following command:
```
aws configure --profile lazymaestro
AWS Access Key ID [None]: <Your AWS Access Key ID here>
AWS Secret Access Key [None]: <Your AWS Secret Access Key here>
Default region name [None]: <Your region here>
Default output format []: <Leave it as default>

```
Once you finish the AWS CLI will create two files in current user's HOME folder. 
- **$HOME/.aws/config**
- **$HOME/.aws/credentials**


## Configuring Terraform to use AWS
Last step is tell Terraform about our AWS credentials so in can interact with our AWS infrastructure. This is done very easy using the following command:
```
export AWS_PROFILE=lazymaestro
```

# Terraform State
Terraform is using **state files** to store all the information about our infrastructure. This State file is basically a mapping between your configuration and your real physical resources in AWS Cloud. This is the most important file in Terraform. 

## Remote backend
By default state is stored on a local machine in a file called **terraform.tfstate**. However Terraform provides a way to store this State file in a remote location. For LM we will be using S3 bucket to store our state files.

## State Locking
This is very important since **all Terraform configuration is stored in one single file**. THis is why it's very important to provide **State locking** feature which is used to prevent concurrent runs on the same state file. 

In this project we will be using **AWS DynamoDB** as a Locking mechanism. The DynamoDB table is keyed on “LockID” which is set as a bucketName/path, so as long as we have a unique combination of this we don’t have any problem in acquiring locks and running everything in a safe way

# Creating S3 Backend with State lock
S3 bucket configuration is located in **global/<account_id>/s3State**. File **main.tf** contains all the required instructions:
| Name | Description | 
| ---- | ----------- |
| **locals** | List of configurable variables | 
| **provider** | Defines the provider for Terraform. In our case it's **AWS** | 
| **module** | Used to include the module that will be used to create S3 bucket. Please note that we're passing two variables to this module: **region = local.region** and **default_tags=local.default_tags**. These variables are taken from **locals** section | 

## S3 Bucket Module

S3 Bucket module is located in **modules/global/s3State**. Consists of the following files
| File | Description |
|------|------------ |
| **variables.tf** | List of variables used by these module. We pass the variables from **main.tf** file in **global/<account_id>/s3state** folder.|
| **main.tf** | This file contains all Terraform instructions to create required AWS resources | 
| **outputs.tf** | This file contains a list of variables that will be displayed after the Terraform finishes creating the AWS resources | 

## Creating the S3 Bucket
To create an S3 bucket as our Remote backend please do the following: 
1. Go to **global/<account_id>/s3State**
2. Run the following command
   ``` 
   terraform init 
   ```
3. If everything is fine, run the following command
   ```
   terraform plan
   ```
4. Please check the output of **terraform plan** command and if it's OK, please run the following command:
   ```
   terraform apply
   ```
   
The **terraform apply** command will do the following:
1. Create an S3 bucket called **terraform-state-config-locks-<account_id>**
2. Create the AWS DynamoDB table called **terraform-locks**

Once it finishes please go to your AWS Account and make that all AWS resources have been successfully created. You can always destroy all resource you've created by running **terraform destroy** command



# Creating LM resources.

Ok, Terraform part is done, and from now on we will be using **terragrunt** to manage AWS resources. The most important part regarding **terragrunt** is that allows us to create a separate environments with its own list of resources and variables. 

We won't dive deep into how each AWS resource is created, but I will explain pattern used to create all current AWS resources and will be used to create other AWS resources in future.

## Root Terragrunt configuration file
Inside the **infra/<account_id>** there is a root Terragrunt file called **terragrunt.hcl**. This file is common for all created resources. Basically this file does the following: 
1. Reads the configuration file
   ```
   locals {
      common_vars = yamldecode(file("dev.yml"))
   }
   ```
2. Uses an S3 bucket as the Backend to store Terraform state file
   ```
    remote_state {
        backend = "s3"
        ....
    }  
   ```

3. Generates file with Backend configuration
   ```
      generate = {
          path      = "backend.tf"
          if_exists = "overwrite_terragrunt"
      }
   ```
4. Generates file with Provider configuration
   ```
      generate "provider" {
         path = "provider.tf"
         ...
      }
   ```

## Creating Networking in DEV environment
If we go to **infra/<account_id>/** folder we will see three folders: **dev**, **prod** and **staging**. Let's take a look at **dev/networking** folder. 

This folder contains a single **terragrunt.hcl**. This file contains the following commands:

| Name | Description |
-------|-------------|
| **terraform** | This command is used to run specific module. In our case we're using the Networking module from **modules/networking** |
| **locals** | This section is used to load the variables from configuration file. In our case it's **dev.yml** file in **infra/<account_id>/dev**. |
| **include** | This command is used to include the **root Terragrunt file** from the upper directory, where you can find the Backend and Provider configuration | 
| **inputs** | List of input variables required for **networking** module, specified in **terraform** section |

So, what is happening when we run the **terragrunt apply** inside **infra/<account_id>/dev/networking** folder? 
