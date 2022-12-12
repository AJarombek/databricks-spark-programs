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
  workflow_cluster_key = "workflow_cluster"
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

data "databricks_notebook" "data_workflow_load_stage" {
  path = "${data.databricks_current_user.me.home}/data_workflow_load_stage"
  format = "SOURCE"
}

data "databricks_notebook" "data_workflow_transform_stage" {
  path = "${data.databricks_current_user.me.home}/data_workflow_transform_stage"
  format = "SOURCE"
}

data "databricks_notebook" "data_workflow_display_stage" {
  path = "${data.databricks_current_user.me.home}/data_workflow_display_stage"
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

resource "databricks_job" "workflow" {
  name = "workflow"

  job_cluster {
    job_cluster_key = local.workflow_cluster_key

    new_cluster {
      num_workers = 1
      spark_version = data.databricks_spark_version.latest.id
      node_type_id = data.databricks_node_type.smallest.id
    }
  }

  task {
    task_key = "load"
    job_cluster_key = local.workflow_cluster_key

    notebook_task {
      notebook_path = data.databricks_notebook.data_workflow_load_stage.path
    }
  }

  task {
    task_key = "transform"
    job_cluster_key = local.workflow_cluster_key

    notebook_task {
      notebook_path = data.databricks_notebook.data_workflow_transform_stage.path
    }

    depends_on {
      task_key = "load"
    }
  }

  task {
    task_key = "display"
    job_cluster_key = local.workflow_cluster_key

    notebook_task {
      notebook_path = data.databricks_notebook.data_workflow_display_stage.path
    }

    depends_on {
      task_key = "transform"
    }
  }
}
