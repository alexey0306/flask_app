# Introduction
This document contains all the information required to deploy and run LM components in AWS cloud. 

# Table of Contents
- [Infrastructure as a Code](#infrastructure-as-a-code)
- [Terraform](#terraform)
- [Terragrunt](#terragrunt)
- [Installing Terraform and Terragrunt](#installing-terraform-and-terragrunt)
- [Configuring AWS](#configuring-aws)

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
- [Configuring Terraform/Terragrunt to use AWS](#configuring-terraform/terragrunt-to-use-aws)

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
aws configure --profile 
AWS Access Key ID [None]: <Your AWS Access Key ID here>
AWS Secret Access Key [None]: <Your AWS Secret Access Key here>
Default region name [None]: <Your region here>
Default output format []: <Leave it as default>

```
Once you finish the AWS CLI will create two files in current user's HOME folder. 
- **$HOME/.aws/config**
- **$HOME/.aws/credentials**


## Configuring Terraform/Terragrunt to use AWS

   

