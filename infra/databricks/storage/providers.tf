/**
 * Versions of providers used in the Terraform module.
 * Author: Andrew Jarombek
 * Date: 1/31/2023
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
