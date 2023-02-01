/**
 * Infrastructure for configuring Databricks storage.
 * Author: Andrew Jarombek
 * Date: 1/31/2023
 */

resource "databricks_dbfs_file" "strava_activities_csv" {
  source = "${path.module}/strava_activities.csv"
  path   = "/src/strava_activities.csv"
}