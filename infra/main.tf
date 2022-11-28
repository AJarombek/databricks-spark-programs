/**
 * Infrastructure setup for Databricks.
 * Author: Andrew Jarombek
 * Date: 11/23/2022
 */

provider "aws" {
  region = "us-east-1"
}

terraform {
  required_version = ">= 1.1.2"

  required_providers {
    databricks = {
      source = "databricks/databricks"
      version = ">= 1.6.5"
    }

    aws = {
      source = "hashicorp/aws"
      version = ">= 4.15.0"
    }
  }

  backend "s3" {
    bucket = "andrew-jarombek-terraform-state"
    encrypt = true
    key = "databricks-spark-programs/infra"
    region = "us-east-1"
  }
}

module "e2" {
  source = "./workspace"
  databricks_account_username = var.databricks_account_username
  databricks_account_password = var.databricks_account_password
  databricks_account_id = var.databricks_account_id
}

module "notebooks" {
  source = "./notebooks"
  databricks_host = module.e2.databricks_host
  databricks_token = module.e2.databricks_token
}

module "clusters" {
  source = "./clusters"
  databricks_host = module.e2.databricks_host
  databricks_token = module.e2.databricks_token
}

module "administration" {
  source = "./administration"
  databricks_host = module.e2.databricks_host
  databricks_token = module.e2.databricks_token
}