/**
 * Infrastructure for administrative resources on Databricks, such as users, groups, and ACLs.
 * Author: Andrew Jarombek
 * Date: 11/27/2022
 */

resource "databricks_user" "guest" {
  user_name = "guest@jarombek.com"
  display_name = "Guest"
}