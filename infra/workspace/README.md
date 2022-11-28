### Overview

Terraform module for creating a Databricks E2 workspace on AWS.

### Files

| Filename       | Description                                                              |
|----------------|--------------------------------------------------------------------------|
| `iam.tf`       | Terraform infrastructure for IAM policies and roles used by Databricks.  |
| `locals.tf`    | Local Terraform variables.                                               |
| `output.tf`    | Output variables returned from the module.                               |
| `providers.tf` | Databricks and AWS provider configuration.                               |
| `storage.tf`   | Terraform infrastructure for S3 storage needed by Databricks.            |
| `var.tf`       | Terraform variables for the module.                                      |
| `vpc.tf`       | Terraform infrastructure for a VPC used to house a Databricks workspace. |
| `workspace.tf` | Terraform infrastructure for a Databricks workspace hosted on AWS.       |

### References

1. [Databricks AWS Workspace](https://registry.terraform.io/providers/databricks/databricks/latest/docs/guides/aws-workspace)