/**
 * IAM cross account role infrastructure for a Databricks workspace.
 * Author: Andrew Jarombek
 * Date: 11/17/2022
 */

data "databricks_aws_assume_role_policy" "databricks" {
  external_id = var.databricks_account_id
}

data "databricks_aws_crossaccount_policy" "databricks" {}

resource "aws_iam_role" "cross_account_role" {
  name = "${local.prefix}-crossaccount"
  assume_role_policy = data.databricks_aws_assume_role_policy.databricks.json
}

resource "aws_iam_role_policy" "databricks" {
  name = "${local.prefix}-policy"
  role   = aws_iam_role.cross_account_role.id
  policy = data.databricks_aws_crossaccount_policy.databricks.json
}

resource "databricks_mws_credentials" "databricks" {
  provider = databricks.mws
  account_id = var.databricks_account_id
  role_arn = aws_iam_role.cross_account_role.arn
  credentials_name = "${local.prefix}-creds"
  depends_on = [aws_iam_role_policy.databricks]
}
