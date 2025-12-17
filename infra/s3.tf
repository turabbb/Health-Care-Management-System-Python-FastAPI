# =============================================================================
# S3 BUCKET (Commented out - slow in LocalStack)
# =============================================================================

# resource "random_string" "bucket_suffix" {
#   length  = 8
#   special = false
#   upper   = false
# }

# resource "aws_s3_bucket" "data" {
#   bucket        = "${var.project_name}-${var.environment}-data-${random_string.bucket_suffix.result}"
#   force_destroy = true
#
#   tags = {
#     Name = "${var.project_name}-${var.environment}-data"
#   }
# }
