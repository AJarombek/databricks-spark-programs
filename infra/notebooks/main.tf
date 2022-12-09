/**
 * Infrastructure for building Databricks notebooks.
 * Author: Andrew Jarombek
 * Date: 11/26/2022
 */

locals {
  permissions = {
    can_manage: "CAN_MANAGE",
    can_run: "CAN_RUN",
    can_read: "CAN_READ"
  }
}

data "databricks_current_user" "me" {
  depends_on = [var.databricks_host]
}

data "databricks_user" "guest" {
  user_name = "guest@jarombek.com"
  depends_on = [var.databricks_host]
}

resource "databricks_notebook" "hello_world" {
  path = "${data.databricks_current_user.me.home}/hello_world"
  language = "PYTHON"
  content_base64 = base64encode(<<-EOT
    print("Hello World")
    EOT
  )
}

resource "databricks_permissions" "hello_world" {
  notebook_path = databricks_notebook.hello_world.id

  access_control {
    user_name = data.databricks_user.guest.user_name
    permission_level = local.permissions.can_run
  }
}

resource "databricks_notebook" "spark_temp_view_python" {
  path = "${data.databricks_current_user.me.home}/spark_temp_view_python"
  language = "PYTHON"
  source = "${path.module}/python/spark_temp_view_python.py"
}
