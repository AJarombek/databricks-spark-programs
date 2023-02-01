/**
 * Variables for working within a Databricks workspace.
 * Author: Andrew Jarombek
 * Date: 1/31/2023
 */

variable "databricks_host" {
  description = "Host for a Databricks workspace"
  default     = ""
  type        = string
}

variable "databricks_token" {
  description = "Token for a Databricks workspace"
  default     = ""
  type        = string
  sensitive   = true
}