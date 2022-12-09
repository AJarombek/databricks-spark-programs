/**
 * Infrastructure for building Databricks jobs.
 * Author: Andrew Jarombek
 * Date: 11/27/2022
 */

locals {
  permissions = {
    can_manage: "CAN_MANAGE",
    can_manage_run: "CAN_MANAGE_RUN",
    can_read: "CAN_READ",
    is_owner: "IS_OWNER"
  }
}

data "databricks_spark_version" "latest" {
  depends_on = [var.databricks_host]
}

data "databricks_user" "guest" {
  user_name = "guest@jarombek.com"
  depends_on = [var.databricks_host]
}

data "databricks_node_type" "smallest" {
  local_disk = true
}

data "databricks_current_user" "me" {
  depends_on = [var.databricks_host]
}

data "databricks_notebook" "hello_world" {
  path = "${data.databricks_current_user.me.home}/hello_world"
  format = "SOURCE"
}

resource "databricks_job" "hello_world" {
  name = "hello_world"

  new_cluster {
    num_workers = 1
    spark_version = data.databricks_spark_version.latest.id
    node_type_id = data.databricks_node_type.smallest.id
  }

  notebook_task {
    notebook_path = data.databricks_notebook.hello_world.path
  }
}

resource "databricks_permissions" "hello_world" {
  job_id = databricks_job.hello_world.id

  access_control {
    user_name = data.databricks_user.guest.user_name
    permission_level = local.permissions.can_manage_run
  }
}