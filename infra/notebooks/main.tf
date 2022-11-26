/**
 * Infrastructure for building Databricks notebooks.
 * Author: Andrew Jarombek
 * Date: 11/26/2022
 */

data "databricks_current_user" "me" {
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
