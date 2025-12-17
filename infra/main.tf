# =============================================================================
# TERRAFORM CONFIGURATION - LOCAL DEVELOPMENT (NO AWS CHARGES!)
# =============================================================================
# This configuration works with LocalStack - a FREE local AWS emulator
# No real AWS resources are created, no charges will occur!
# =============================================================================

terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}

# -----------------------------------------------------------------------------
# AWS Provider - Configured for LocalStack (FREE!)
# -----------------------------------------------------------------------------
provider "aws" {
  region                      = var.aws_region
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    ec2            = var.localstack_endpoint
    s3             = var.localstack_endpoint
    rds            = var.localstack_endpoint
    iam            = var.localstack_endpoint
    sts            = var.localstack_endpoint
    secretsmanager = var.localstack_endpoint
  }

  default_tags {
    tags = {
      Project     = "healthcare-system"
      Environment = var.environment
      ManagedBy   = "terraform"
    }
  }
}
