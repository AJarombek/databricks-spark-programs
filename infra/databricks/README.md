### Overview

Terraform module for creating Databricks resources within a workspace.

### Files

| Filename         | Description                                                                      |
|------------------|----------------------------------------------------------------------------------|
| `administration` | Terraform infrastructure for Databricks administrative resources, such as users. |
| `clusters`       | Terraform infrastructure for Databricks clusters and instance pools.             |
| `jobs`           | Terraform infrastructure for Databricks jobs.                                    |
| `notebooks`      | Terraform infrastructure for Databricks notebooks.                               |
| `storage`        | Terraform infrastructure for HDFS and external storage.                          |
| `main.tf`        | Terraform infrastructure for Databricks resources within a workspace.            |
| `providers.tf`   | Databricks provider configuration.                                               |
| `var.tf`         | Terraform variables for the module.                                              |