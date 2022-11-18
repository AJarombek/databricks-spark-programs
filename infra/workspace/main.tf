/**
 * Infrastructure for a Databricks workspace.
 * Author: Andrew Jarombek
 * Date: 11/17/2022
 */

provider "aws" {
  region = "us-east-1"
}

provider "databricks" {
  alias = "mws"
  host = "https://accounts.cloud.databricks.com"
  username = var.databricks_account_username
  password = var.databricks_account_password
}

terraform {
  required_version = ">= 1.1.2"

  required_providers {
    databricks = {
      source = "databricks/databricks"
    }

    aws = {
      source = "hashicorp/aws"
      version = ">= 4.15.0"
    }
  }

  backend "s3" {
    bucket = "andrew-jarombek-terraform-state"
    encrypt = true
    key = "global-aws-infrastructure/parameter-store/secrets/dbrx"
    region = "us-east-1"
  }
}

data "databricks_aws_assume_role_policy" "dbrx" {
  external_id = var.databricks_account_id
}

data "databricks_aws_crossaccount_policy" "dbrx" {}
