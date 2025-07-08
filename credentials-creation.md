# 🔐 How to Create `credentials.json` for Amaani Compliance Automation

To enable the Python script to read and write to your Google Sheet, you'll need to create a service account and generate a `credentials.json` file. Follow these steps carefully.

---

## 🧱 STEP 1: Set Up Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Click **Project Selector** in the top bar → Click **“New Project”**
   - Name it: `Amaani Compliance`

---

## 🔧 STEP 2: Enable Required APIs

1. In the left sidebar, go to:
   - **APIs & Services** → **Library**
2. Search for and enable:
   - ✅ Google Sheets API
   - ✅ Google Drive API

---

## 👤 STEP 3: Create the Service Account

1. In the sidebar, go to:
   - **IAM & Admin** → **Service Accounts**
2. Click **“Create Service Account”**
   - Name: `Amaani Sheets Bot`
   - Role: *(leave blank or Viewer — not needed for Sheets access)*
3. Click **Done**

---

## 🔑 STEP 4: Create the `credentials.json` File

1. Click the service account you just created
2. Copy the **email address** (you'll need this later)
3. Go to the **“Keys”** tab
4. Click **“Add Key” → “Create New Key”**
   - Choose **JSON**
5. A file will download to your computer — rename it:
   - Name: `credentials.json`
6. Move this file into the **same folder** as the Python script:
   `amaani_compliance_checker.py`

---

## 📤 STEP 5: Share Your Google Sheet with the Bot

1. Open the Google Sheet workbook
2. Click the **Share** button (top-right)
3. Paste the **service account email** you copied earlier
4. Give it **Editor access**
5. Click **Send**

---

✅ You're done! The Python script will now be able to authenticate with Google and update your compliance workbook.

If you need help, contact:  
📧 **judewakim@wakimworks.com**  
🌐 **wakim-works.com**
