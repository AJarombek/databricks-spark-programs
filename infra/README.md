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

# Destroy Infrastructure
terraform destroy -auto-approve
```