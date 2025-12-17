# =============================================================================
# RDS POSTGRESQL (Commented out - slow in LocalStack)
# =============================================================================

# resource "aws_db_subnet_group" "main" {
#   name        = "${var.project_name}-${var.environment}-db-subnet"
#   description = "Database subnet group"
#   subnet_ids  = [aws_subnet.private_1.id, aws_subnet.private_2.id]
#
#   tags = {
#     Name = "${var.project_name}-${var.environment}-db-subnet"
#   }
# }

# resource "aws_db_instance" "main" {
#   identifier = "${var.project_name}-${var.environment}-db"
#
#   engine               = "postgres"
#   engine_version       = "15.4"
#   instance_class       = var.db_instance_class
#   allocated_storage    = var.db_allocated_storage
#   storage_type         = "gp2"
#
#   db_name  = var.db_name
#   username = var.db_username
#   password = var.db_password
#   port     = 5432
#
#   db_subnet_group_name   = aws_db_subnet_group.main.name
#   vpc_security_group_ids = [aws_security_group.rds.id]
#   publicly_accessible    = false
#   multi_az               = false
#
#   skip_final_snapshot      = true
#   delete_automated_backups = true
#   deletion_protection      = false
#
#   tags = {
#     Name = "${var.project_name}-${var.environment}-db"
#   }
# }
