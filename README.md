# Introduction
This document contains all the information required to deploy and run LM components in AWS cloud. 

# Table of Contents
- [Infrastructure as a Code](#infrastructure-as-a-code)
- [Terraform](#terraform)
- [Terragrunt](#terragrunt)
- [Installing Terraform and Terragrunt](#installing-terraform-and-terragrunt)

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


# AWS Configuration
In this section we're going to install AWS CLI tools, configure the AWS profile and configure Terraform/Terragrunt to use this profile to interact with our AWS infra. 

- [Installing AWS CLI](#installing-aws-cli)
- [Configuring AWS profile](#configuring-aws-profile)
- [Configuring Terraform/Terragrunt to use AWS](#configuring-terraform/terragrunt-to-use-aws)

## Installing AWS CLI

## Configuring AWS profile

## Configuring Terraform/Terragrunt to use AWS

   

