/**
 * VPC and VPC Endpoint infrastructure for a Databricks workspace.
 * Author: Andrew Jarombek
 * Date: 11/20/2022
 */

data "aws_availability_zones" "available" {}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  version = "3.2.0"

  name = local.vpc_name
  cidr_block = local.cidr_block
  azs = data.aws_availability_zones.available.names

  enable_dns_hostnames = true
  enable_nat_gateway = true
  single_nat_gateway = true
  create_igw = true

  public_subnets = [cidrsubnet(local.cidr_block, 3, 0)]
  private_subnets = [
    cidrsubnet(local.cidr_block, 3, 1),
    cidrsubnet(local.cidr_block, 3, 2)
  ]

  manage_default_security_group = true
  default_security_group_name = "${local.prefix}-sg"

  default_security_group_egress = [{
    cidr_blocks = "0.0.0.0/0"
  }]

  default_security_group_ingress = [{
    description = "Allow all internal TCP and UDP traffic"
    self = true
  }]
}

module "vpc_endpoints" {
  source = "terraform-aws-modules/vpc/aws//modules/vpc-endpoints"
  version = "3.2.0"
}
