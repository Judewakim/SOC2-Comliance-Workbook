# 📊 Amaanī SOC 2 Compliance Automation Kit

### Built by Jude Wakim — Amaanī Cloud Security Architect  
**Email:** judewakim@wakimworks.com  
**Website:** wakim-works.com <br>
**Version:** 1.0

---

## 🌩️ What is Amaanī?

Amaanī is a cloud security automation consultancy focused on helping financial enterprises harden, monitor, and validate their AWS environments against strict compliance standards such as SOC 2.

Our mission is to make security and compliance achievable, repeatable, and provable — without sacrificing developer speed or cloud flexibility.

---

## 📦 What’s Inside This ZIP?

| File | Purpose |
|------|---------|
| `Amaani_SOC2_Compliance_Workbook.xlsx` | The master security checklist. Split into tabs by domain (IAM, Data Protection, Monitoring, etc.). Each row maps to a SOC 2 control. |
| `amaani_compliance_checker.py` | The Python script that connects to your AWS account and fills in the “Compliant?” column for each item using CLI/API logic. |
| `iam_compliance_user.tf` | Terraform code to create a new IAM user with all required read-only permissions to run the automation script. |
| `amaani-compliance-readonly.json` | The exact IAM policy used to limit access to only what the script needs. |
| `credentials.json` (optional) | Google Service Account credentials (not included by default — see setup instructions below). |
| `README.md` | You’re reading it :) |

---

## ✅ Purpose of the Workbook

The workbook helps your organization:
- Identify gaps in security, availability, privacy, and other SOC 2 principles
- Prove compliance through evidence (CLI output, screenshots, or policy configs)
- Quantify your risk posture via automated scoring
- Track remediation over time

---

## 🧪 How to Run the Automation

### Option A: Using Your Own AWS User
Make sure your AWS CLI is configured and you have at least read-only permissions.

```bash
aws configure
python amaani_compliance_checker.py
```

### Option B: Using the Provided IAM User (Terraform)
1. Deploy the IAM user and policy
```hcl 
 terraform init
terraform apply
```

2. Use the output keys to configure AWS CLI

```bash
aws configure
python amaani_compliance_checker.py
```

---

## 🧰 Prerequisites
•	Python 3.8+
•	boto3, gspread, and oauth2client installed:

```bash
pip install boto3 gspread oauth2client
```

•	A Google Service Account with Editor access to the Google Sheet
•	Share your workbook with the service account email
•	Save the credentials.json locally

---

## 📬 Contact Amaanī
If you need help with setup, custom compliance automation, or SOC 2 Type II readiness:

Jude Wakim
Cloud Security Architect
Email: judewakim@wakimworks.com
Based in: U.S. / Remote
Specialties: AWS Security, Terraform, SOC 2, Zero Trust Architectures

⸻

Thank you for trusting Amaanī with your cloud security journey.
“Security First. Compliance Included.”

---

## ✅ Final Structure of ZIP

Amaani_SOC2_Compliance_Kit.zip
├── terraform/
│   ├── iam-compliance-user.tf
├── scripts/
│   ├── amaani-compliance-checker.py
│   ├── amaani-compliance-readonly.json
│   └── credentials.json  <-- added manually by client
├── assets/
│   └── amaani-soc2-workbook.xlsx
├── .gitignore
├── README.md
├── credentials-creation.md


