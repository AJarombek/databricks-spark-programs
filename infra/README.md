### Overview

Terraform infrastructure for a Databricks workspace and its associated resources.

### Commands

```bash
# Create Infrastructure
terraform init -upgrade
terraform validate

export TF_VAR_databricks_account_username=XXX
export TF_VAR_databricks_account_password=XXX
export TF_VAR_databricks_account_id=XXX

terraform plan
terraform apply -auto-approve

# Apply the infrastructure in debug mode
TF_LOG=DEBUG terraform apply -auto-approve

# Destroy Infrastructure
terraform destroy -auto-approve
```

### Files

| Filename         | Description                                                                      |
|------------------|----------------------------------------------------------------------------------|
| `administration` | Terraform infrastructure for Databricks administrative resources, such as users. |
| `clusters`       | Terraform infrastructure for Databricks clusters and instance pools.             |
| `notebooks`      | Terraform infrastructure for Databricks notebooks.                               |
| `workspace`      | Terraform infrastructure for a Databricks workspace hosted on AWS.               |
| `main.tf`        | Main Terraform file that configures Databricks infrastructure.                   |
| `var.tf`         | Terraform variables used for Databricks infrastructure.                          |