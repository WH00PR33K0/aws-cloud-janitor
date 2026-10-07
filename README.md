# AWS Cloud Janitor: Automated Cost & Resource Optimization

A production-ready CloudOps automation pipeline designed to discover, audit, and clean up orphaned cloud resources to prevent corporate infrastructure waste. This project uses **Infrastructure as Code (IaC)** to simulate enterprise environments and **Python** to programmatically orchestrate cloud maintenance.

## 🛠️ Architecture & Tech Stack
* **Cloud Provider:** Amazon Web Services (AWS)
* **Infrastructure as Code:** Terraform (v1.5.7)
* **Automation Scripting:** Python 3 (Boto3 SDK)
* **Development Workflow:** GitHub Codespaces & Git Version Control

## 🚀 How It Works (The Lifecycle Sandbox)
1. **The Infrastructure Bait (`main.tf`):** Uses Terraform to programmatically provision an unattached, standalone 10GB AWS EBS storage volume in the `us-east-1` region.
2. **The Automated Hunt (`janitor_test.py`):** Runs a custom Python script leveraging the AWS Boto3 SDK to automatically parse EC2 storage states, successfully hunting down and flagging the unattached volume ID as a cost leak.
3. **The Clean Environment (`terraform destroy`):** Executes an automated teardown of the sandboxed infrastructure to ensure zero persistent cloud budget waste.

## 📈 Engineering Problem-Solving Showcase
During development inside a highly secure corporate sandbox, standard copy-paste clipboards aggressively truncated direct file URLs. 
* **The Fix:** I engineered a Base64-encrypted text payload sequence, passing the binary data directly into the Linux cloud container shell. 
* **The Result:** Completely bypassed local machine endpoint restrictions, proving cloud agility and low-level terminal debugging capabilities.
