# =============================================================================
# EC2 INSTANCE (Commented out - slow in LocalStack)
# =============================================================================

# resource "aws_instance" "app" {
#   ami                         = "ami-12345678"
#   instance_type               = var.ec2_instance_type
#   vpc_security_group_ids      = [aws_security_group.ec2.id]
#   subnet_id                   = aws_subnet.public_1.id
#   associate_public_ip_address = true
#
#   tags = {
#     Name        = "${var.project_name}-${var.environment}-server"
#     Description = "Healthcare API Server"
#   }
# }
