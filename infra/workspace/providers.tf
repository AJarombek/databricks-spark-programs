/**
 * Versions of providers used in the Terraform module.
 * Author: Andrew Jarombek
 * Date: 11/26/2022
 */

terraform {
  required_version = ">= 1.1.2"

  required_providers {
    databricks = {
      source  = "databricks/databricks"
      version = ">= 1.6.5"
    }

    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.15.0"
    }
  }
}

provider "databricks" {
  alias    = "mws"
  host     = "https://accounts.cloud.databricks.com"
  username = var.databricks_account_username
  password = var.databricks_account_password
}
