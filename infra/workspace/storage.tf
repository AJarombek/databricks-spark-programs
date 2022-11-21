/**
 * S3 and additional storage infrastructure for a Databricks workspace.
 * Author: Andrew Jarombek
 * Date: 11/20/2022
 */

resource "aws_s3_bucket" "root_storage_bucket" {
  bucket = "${local.prefix}-rootbucket"
  force_destroy = true
}

resource "aws_s3_bucket_acl" "root_storage_bucket" {
  bucket = aws_s3_bucket.root_storage_bucket.id
  acl = "private"
}

resource "aws_s3_bucket_versioning" "root_storage_bucket" {
  bucket = aws_s3_bucket.root_storage_bucket.id
  versioning_configuration {
    status = "Disabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "root_storage_bucket" {
  bucket = aws_s3_bucket.root_storage_bucket.bucket
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "root_storage_bucket" {
  bucket = aws_s3_bucket.root_storage_bucket.id
  block_public_acls = true
  block_public_policy = true
  ignore_public_acls = true
  restrict_public_buckets = true
  depends_on = [aws_s3_bucket.root_storage_bucket]
}

data "databricks_aws_bucket_policy" "databricks" {
  bucket = aws_s3_bucket.root_storage_bucket.bucket
}

resource "aws_s3_bucket_policy" "root_bucket_policy" {
  bucket = aws_s3_bucket.root_storage_bucket.id
  policy = data.databricks_aws_bucket_policy.databricks.json
  depends_on = [aws_s3_bucket_public_access_block.root_storage_bucket]
}

resource "databricks_mws_storage_configurations" "databricks" {
  provider = databricks.mws
  account_id = var.databricks_account_id
  bucket_name = aws_s3_bucket.root_storage_bucket.bucket
  storage_configuration_name = "${local.prefix}-storage"
}
