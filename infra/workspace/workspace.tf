/**
 * Infrastructure for a Databricks AWS E2 workspace.
 * Author: Andrew Jarombek
 * Date: 11/20/2022
 */

resource "databricks_mws_workspaces" "databricks" {
  provider       = databricks.mws
  account_id     = var.databricks_account_id
  aws_region     = local.region
  workspace_name = local.prefix

  credentials_id           = databricks_mws_credentials.databricks.credentials_id
  storage_configuration_id = databricks_mws_storage_configurations.databricks.storage_configuration_id
  network_id               = databricks_mws_networks.databricks.network_id

  token {
    comment = "Terraform"
  }
}