💻 Azure DevOps Import Guide (Excel Format)
==========================================

✅ Prerequisites
---------------

-   You must have at least **Basic access** to a project.

-   Install [Azure DevOps Office
    Integration](https://learn.microsoft.com/en-us/azure/devops/office/devops-tools).

📥 Steps to Import Excel
-----------------------

1.  Open Excel and go to `Team > New List`.

2.  Connect to your **Azure DevOps Project**.

3.  Copy content from `Hierarchical_Product_Backlog.xlsx` into the sheet.

🗂️ Column Setup
--------------

| Excel Column   | Azure DevOps Field          |
|----------------|-----------------------------|
| Work Item Type | Work Item Type              |
| Feature        | Title                       |
| User Story     | Description                 |
| Task           | Description / Comments      |
| ID             | ID (auto-managed)           |
| Parent ID      | Parent (linked via Publish) |

🚀 Publishing
------------

1.  After pasting all rows, assign correct `Work Item Types`.

2.  Assign `Parent ID` to build hierarchy:

-   Tasks → Features

-   Features → Epics

1.  Click `Publish` to sync with Azure DevOps.

🧠 Tips
------

-   Azure DevOps enforces hierarchy in process templates (Epic → Feature → User
    Story → Task).

-   Ensure all required fields are populated before publishing.
