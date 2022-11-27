/**
 * Infrastructure for configuring Databricks clusters and instance pools.
 * Author: Andrew Jarombek
 * Date: 11/26/2022
 */

data "databricks_spark_version" "latest" {}

data "databricks_node_type" "smallest" {
  local_disk = true
}

resource "databricks_cluster" "all_purpose" {
  cluster_name = "All Purpose"
  spark_version = data.databricks_spark_version.latest.id
  instance_pool_id = databricks_instance_pool.smallest.id
  autotermination_minutes = 15

  autoscale {
    min_workers = 1
    max_workers = 10
  }
}

resource "databricks_cluster_policy" "all_purpose" {
  name = "All Purpose Policy"
  definition = jsonencode({
    "dbus_per_hour": {
      "type": "range",
      "maxValue": 10
    },
    "autotermination_minutes": {
      "type": "fixed",
      "value": 15,
      "hidden": true
    }
  })
}

resource "databricks_instance_pool" "smallest" {
  instance_pool_name = "Smallest Nodes"
  min_idle_instances = 0
  max_capacity = 30
  node_type_id = data.databricks_node_type.smallest.id
  preload_spark_versions = [
    data.databricks_spark_version.latest.id
  ]

  idle_instance_autotermination_minutes = 15
}