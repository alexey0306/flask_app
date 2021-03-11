# Introduction
This document contains all the information required to deploy and run LM components in AWS cloud. 

# Table of Contents
- [Infrastructure as a Code](#infrastructure-as-a-code)
- [Terraform](#terraform)
- [Terragrunt](#terragrunt)

# Infrastructure as a Code (IaC)
What is Infrastructure as a Code? IaC is the process of managing and provisioning infrastructure through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools. It can use either scripts or declarative definitions, rather than manual processes

# Terraform
Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions.

Configuration files describe to Terraform the components needed to run a single application or your entire Infrastructure. Terraform generates an execution plan describing what it will do to reach the desired state, and then executes it to build the described infrastructure. As the configuration changes, Terraform is able to determine what changed and create incremental execution plans which can be applied.

The infrastructure Terraform can manage includes low-level components such as compute instances, storage, and networking, as well as high-level components such as DNS entries, SaaS features, etc.

For more information about Terraform check the [official documentation](https://terraform.io)

# Terragrunt

# LM

