🛠️ Jira Import Guide (CSV Format)
================================

✅ Prerequisites
---------------

-   You must be a **Jira Administrator**.

-   You need a project ready for issue import (create one if needed).

📥 Steps to Import CSV
---------------------

1.  Go to **Jira \> Settings \> System \> External System Import**.

2.  Click on **CSV**.

3.  Upload the file: `Hierarchical_Product_Backlog.csv`.

🗂️ Column Mapping Suggestions
----------------------------

| CSV Column     | Jira Field                             |
|----------------|----------------------------------------|
| Work Item Type | Issue Type                             |
| Feature        | Summary                                |
| User Story     | Description                            |
| Task           | Description / Comment                  |
| ID             | Issue ID (custom field)                |
| Parent ID      | Parent ID (custom field or issue link) |

*Note*: Jira Advanced Roadmaps uses issue links or parent-child relationships to
structure hierarchy.

🧠 Tips
------

-   Ensure `Issue Type` values (Epic, Feature, Task) exist in your Jira project.

-   Use Automation Rules or Advanced Roadmaps for hierarchy linking.
