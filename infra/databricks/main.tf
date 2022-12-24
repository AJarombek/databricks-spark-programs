/**
 * Infrastructure within a databricks workspace.
 * Author: Andrew Jarombek
 * Date: 12/23/2022
 */

module "administration" {
  source = "./administration"
  databricks_host = var.databricks_host
  databricks_token = var.databricks_token
}

module "notebooks" {
  source = "./notebooks"
  databricks_host = var.databricks_host
  databricks_token = var.databricks_token

  depends_on = [module.administration]
}

module "jobs" {
  source = "./jobs"
  databricks_host = var.databricks_host
  databricks_token = var.databricks_token

  depends_on = [module.administration, module.notebooks]
}

module "clusters" {
  source = "./clusters"
  databricks_host = var.databricks_host
  databricks_token = var.databricks_token

  depends_on = [module.administration]
}