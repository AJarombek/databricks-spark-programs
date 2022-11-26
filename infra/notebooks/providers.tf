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
  }
}

provider "databricks" {
  host = var.databricks_host
  token = var.databricks_token
}
