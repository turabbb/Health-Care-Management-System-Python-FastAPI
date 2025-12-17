# =============================================================================
# TERRAFORM OUTPUTS
# =============================================================================

output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "vpc_cidr" {
  description = "VPC CIDR block"
  value       = aws_vpc.main.cidr_block
}

output "public_subnet_ids" {
  description = "Public subnet IDs"
  value       = [aws_subnet.public_1.id, aws_subnet.public_2.id]
}

output "private_subnet_ids" {
  description = "Private subnet IDs"
  value       = [aws_subnet.private_1.id, aws_subnet.private_2.id]
}

output "ec2_security_group_id" {
  description = "EC2 security group ID"
  value       = aws_security_group.ec2.id
}

output "rds_security_group_id" {
  description = "RDS security group ID"
  value       = aws_security_group.rds.id
}

output "internet_gateway_id" {
  description = "Internet Gateway ID"
  value       = aws_internet_gateway.main.id
}

output "route_table_id" {
  description = "Public route table ID"
  value       = aws_route_table.public.id
}

output "infrastructure_summary" {
  description = "Infrastructure Summary"
  value = <<-EOF

  ══════════════════════════════════════════════════════════════
   INFRASTRUCTURE PROVISIONED SUCCESSFULLY (LocalStack)
  ══════════════════════════════════════════════════════════════
   
   VPC:              ${aws_vpc.main.id}
   Public Subnets:   ${aws_subnet.public_1.id}, ${aws_subnet.public_2.id}
   Private Subnets:  ${aws_subnet.private_1.id}, ${aws_subnet.private_2.id}
   Security Groups:  ${aws_security_group.ec2.id}, ${aws_security_group.rds.id}
   Internet Gateway: ${aws_internet_gateway.main.id}
   
   💰 COST: $0.00 (LocalStack - Free!)
  ══════════════════════════════════════════════════════════════
  EOF
}
