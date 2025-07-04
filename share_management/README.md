# Share Management System - Odoo Module

## Module Purpose
The `share_management` module is a lightweight Odoo module designed to manage shareholders, share transactions, and dividends within an organization. It provides functionality to:
- Register and manage shareholder details.
- Record share transactions (buy, sell, transfer).
- Calculate shareholding percentages dynamically.
- Track dividend payments.
- Display a summarized dashboard with key metrics.

This module is ideal for businesses needing to track share ownership and related financial activities in a simple, integrated way within Odoo.

## Installation Instructions
1. **Download the Module**:
   - Clone or download the `share_management` module to your Odoo custom addons directory (e.g., `/home/ku/odoo_web/odoo/custom_addons/`).

2. **Update the Addons Path**:
   - Ensure the custom addons directory is included in your Odoo configuration file (`odoo.conf`):
     ```ini
     [options]
     addons_path = /home/ku/odoo_web/odoo/odoo/addons,/home/ku/odoo_web/odoo/custom_addons
     ```

3. **Install Dependencies**:
   - The module has no external Python dependencies beyond standard Odoo requirements. Ensure your Odoo environment is set up with Python 3.12 and necessary libraries (e.g., `lxml`).

4. **Update the Module List**:
   - Start the Odoo server with the `--update` flag to register the module:
     ```bash
     ./odoo-bin -c /path/to/odoo.conf --update=share_management
     ```

5. **Install the Module**:
   - Log in to Odoo as an administrator.
   - Navigate to **Apps** > **Update Apps List**.
   - Search for `share_management` and click **Install**.

6. **Configure Access Rights**:
   - Assign users to the `Share Manager` group for full CRUD access or the `Share Viewer` group for read-only access via **Settings** > **Users & Companies** > **Groups**.

## Usage Instructions
### 1. Managing Shareholders
- Navigate to the **Shareholders** menu to create or view shareholder records.
- Each shareholder record includes:
  - Name, linked partner, total shares, total invested amount, share percentage, and total dividends.
  - Smart buttons for quick access to total shares, share percentage, and dividend history.
  - One2many fields showing related transactions and dividends.
- Use the list or form view to manage shareholders.

### 2. Recording Share Transactions
- Access the **Share Transactions** menu to log buy, sell, or transfer transactions.
- Fields include:
  - `shareholder_id`: The shareholder initiating the transaction.
  - `type`: Select from Buy, Sell, or Transfer.
  - `quantity`: Number of shares involved.
  - `price_per_share`: Price per share (set to 0 for transfers).
  - `amount`: Total amount (calculated as `quantity * price_per_share`).
  - `receiver_id`: Required for transfers to specify the recipient shareholder.
  - `date`: Date of the transaction.
- Transactions automatically update the shareholder's `total_shares` and `total_invested` fields.

### 3. Managing Dividends
- Use the **Dividends** menu to record dividend payments.
- Fields include:
  - `shareholder_id`: The recipient shareholder.
  - `amount`: Dividend amount.
  - `date`: Payment date.
- Dividend totals are aggregated in the shareholder's `dividend_received` field.

### 4. Importing Transactions via CSV
- Use the provided CSV import template (`share_transaction_import_template.csv`) for bulk transaction imports.
- **Steps**:
  1. Navigate to **Share Transactions** > **Import**.
  2. Download the template and populate it with data. Ensure:
     - `shareholder_id` and `receiver_id` match existing shareholder names or IDs.
     - `type` is one of: Buy, Sell, Transfer.
     - `date` is in YYYY-MM-DD format.
  3. Upload the CSV file via the Odoo import wizard.
  4. Map fields as needed and validate the import.
- Example CSV content:
  ```csv
  shareholder_id,type,quantity,price_per_share,amount,receiver_id,date
  "John Doe",Buy,100,10.00,1000.00,,2025-07-01
  "Jane Smith",Sell,50,12.00,600.00,,2025-07-02
  "John Doe",Transfer,20,0.00,0.00,"Jane Smith",2025-07-03
  ```

### 5. Viewing the Dashboard
- Access the dashboard via the **Shareholders** menu (optional Kanban or Graph view).
- View:
  - Pie or bar chart showing share distribution by shareholder.
  - Table of recent transactions and dividends.
  - Smart buttons for quick insights into shares and dividends.

## Sample Usage Data
To test the module, create the following records:
1. **Shareholders**:
   - Name: John Doe, Partner: John Doe, Total Shares: 0, Total Invested: 0
   - Name: Jane Smith, Partner: Jane Smith, Total Shares: 0, Total Invested: 0
2. **Share Transactions**:
   - John Doe buys 100 shares at $10 each on 2025-07-01.
   - Jane Smith sells 50 shares at $12 each on 2025-07-02.
   - John Doe transfers 20 shares to Jane Smith on 2025-07-03.
3. **Dividends**:
   - John Doe receives $500 dividend on 2025-07-04.
   - Jane Smith receives $300 dividend on 2025-07-04.
4. **Verify**:
   - Check shareholder records for updated shares, percentages, and dividends.
   - View the dashboard for visual summaries.

## Troubleshooting
- **RecursionError in `share.transaction`**: If you encounter a `RecursionError`, review the `create` method in `models/share_transaction.py`. Ensure recursive calls to `self.env['share.transaction'].create` are guarded with a context flag (e.g., `skip_recursive_create`).
- **HTML Sanitization Issues**: Sanitize HTML fields using `odoo.tools.html_sanitize` before saving to avoid errors in `mail.thread` logging.
- **Import Errors**: Ensure CSV data matches the expected format and that referenced shareholders exist in the database.

## Notes
- The module is compatible with Odoo 17 and 18 (verify your version).
- For further customization, extend the module by adding scheduled actions or notifications as per the optional stretch features.
- Contact the Odoo community or module developer for support with complex issues.