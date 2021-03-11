# Introduction
This document contains all the information required to deploy and run LM components in AWS cloud. 

# Table of Contents
- [Infrastructure as a Code](#infrastructure-as-a-code)
- [Terraform](#terraform)
- [Terragrunt](#terragrunt)
- [Getting started with LM IaC](#getting-started-with-lm-iac)

# Infrastructure as a Code (IaC)
What is Infrastructure as a Code? IaC is the process of managing and provisioning infrastructure through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools. It can use either scripts or declarative definitions, rather than manual processes

# Terraform
Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions.

Configuration files describe to Terraform the components needed to run a single application or your entire Infrastructure. Terraform generates an execution plan describing what it will do to reach the desired state, and then executes it to build the described infrastructure. As the configuration changes, Terraform is able to determine what changed and create incremental execution plans which can be applied.

The infrastructure Terraform can manage includes low-level components such as compute instances, storage, and networking, as well as high-level components such as DNS entries, SaaS features, etc.

For more information about Terraform check the [official documentation](https://terraform.io)

# Terragrunt
Terragrunt is a thin wrapper that provides extra tools for keeping your configurations DRY, working with multiple Terraform modules, and managing remote state.

# Getting with LM IaC
In this section you will find information of how to deploy the LM components in the AWS cloud. Terraform supports multiple providers and in this particular section we will be using **Terraform for AWS**

## Step 1. Installing Terraform
In this section we're going to install Terraform on your machine. 

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



