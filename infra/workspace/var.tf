/**
 * Variables for building a Databricks workspace.
 * Author: Andrew Jarombek
 * Date: 11/15/2022
 */

variable "databricks_account_username" {
  description = "Username for my Databricks account"
  default = ""
  type = string
  sensitive = true
}

variable "databricks_account_password" {
  description = "Password for my Databricks account"
  default = ""
  type = string
  sensitive = true
}

variable "databricks_account_id" {
  description = "ID for my Databricks account"
  default = ""
  type = string
  sensitive = true
}