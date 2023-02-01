/**
 * Output variables for building a Databricks workspace.
 * Author: Andrew Jarombek
 * Date: 11/21/2022
 */

output "databricks_host" {
  value = databricks_mws_workspaces.databricks.workspace_url
}

output "databricks_token" {
  value     = databricks_mws_workspaces.databricks.token[0].token_value
  sensitive = true
}