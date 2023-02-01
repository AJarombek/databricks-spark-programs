/**
 * Variables for building infrastructure in Databricks.
 * Author: Andrew Jarombek
 * Date: 12/23/2022
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