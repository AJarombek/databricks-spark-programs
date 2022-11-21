/**
 * Main infrastructure for a Databricks workspace.
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
    key = "databricks-spark-programs/workspace"
    region = "us-east-1"
  }
}

data "databricks_aws_assume_role_policy" "databricks" {
  external_id = var.databricks_account_id
}

data "databricks_aws_crossaccount_policy" "databricks" {}

resource "aws_iam_role" "cross_account_role" {
  name = "${local.prefix}-crossaccount"
  assume_role_policy = data.databricks_aws_assume_role_policy.databricks.json
}

resource "aws_iam_role_policy" "databricks" {
  name = "${local.prefix}-policy"
  role   = aws_iam_role.cross_account_role.id
  policy = data.databricks_aws_crossaccount_policy.databricks.json
}

resource "databricks_mws_credentials" "databricks" {
  provider = databricks.mws
  account_id = var.databricks_account_id
  role_arn = aws_iam_role.cross_account_role.arn
  credentials_name = "${local.prefix}-creds"
  depends_on = [aws_iam_role_policy.databricks]
}
