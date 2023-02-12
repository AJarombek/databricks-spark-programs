# databricks-spark-programs

### Overview

Spark/Databricks programs hosted on a Databricks environment on AWS.

### Commands

**Set GitHub Secrets**

```bash
brew install gh
gh auth login

gh secret set DATABRICKS_ACCOUNT_USERNAME
gh secret set DATABRICKS_ACCOUNT_PASSWORD
gh secret set DATABRICKS_ACCOUNT_ID

gh secret set AWS_ACCESS_KEY_ID
gh secret set AWS_SECRET_ACCESS_KEY
```

### Directories

| Directory Name | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `.github`      | GitHub Actions for CI/CD pipelines.                                         |
| `infra`        | Infrastructure for a Databricks workspace and resources within a workspace. |

### Version History

**[v1.0.0](https://github.com/AJarombek/databricks-spark-programs/tree/v1.0.0) - Initial Version**

> Release Date: Jan 29th, 2023

* Terraform infrastructure successfully creates Databricks E2 workspace and objects within the workspace
* GitHub Actions workflow for formatting Terraform
* Databricks jobs and notebooks showing the basics of working with Spark in Databricks
