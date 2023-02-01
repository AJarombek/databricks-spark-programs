/**
 * Local variables for a Databricks workspace.
 * Author: Andrew Jarombek
 * Date: 11/20/2022
 */

locals {
  vpc_name   = "databricks-vpc"
  prefix     = "jarombek-databricks"
  cidr_block = "10.3.0.0/16"
  region     = "us-east-1"
}