#################AUTO-CREATE NEW USER WITH PROPER COMPLIANCE PERMISSIONS###########################

######PROVIDER##################
provider "aws" {
  region = "us-east-1"
}

#########RESOURCES##################
resource "aws_iam_user" "amaani_compliance" {
  name = "amaani_compliance_user"
  tags = {
    Purpose = "Amaanī Compliance Automation"
  }
}

resource "aws_iam_policy" "amaani_compliance_policy" {
  name        = "AmaaniComplianceReadOnlyPolicy"
  description = "Provides minimum read-only access for Amaanī compliance automation"
  policy      = file("${path.module}/amaani-compliance-readonly.json")
}

resource "aws_iam_user_policy_attachment" "attach" {
  user       = aws_iam_user.amaani_compliance.name
  policy_arn = aws_iam_policy.amaani_compliance_policy.arn
}

resource "aws_iam_access_key" "compliance" {
  user = aws_iam_user.amaani_compliance.name
}


##########OUTPUTS#################
output "amaani_user_name" {
  value = aws_iam_user.amaani_compliance.name
}

output "access_key_id" {
  value     = aws_iam_access_key.compliance.id
  sensitive = true
}

output "secret_access_key" {
  value     = aws_iam_access_key.compliance.secret
  sensitive = true
}

output "console_login_url" {
  value = "https://signin.aws.amazon.com/console"
}
