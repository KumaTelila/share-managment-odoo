# Share Management Odoo Module

## Overview
The `share_management` module enables tracking of shareholders, share transactions (buy/sell/transfer), dividends, and share percentages in Odoo. It includes a dashboard for quick insights.

## Installation
1. **Place Module**:
   - Copy the `share_management` folder to your Odoo custom addons directory (e.g., `/home/ku/odoo_web/odoo/custom_addons/`).

2. **Configure Addons Path**:
   - Update `odoo.conf`:
     ```ini
     [options]
     addons_path = /home/ku/odoo_web/odoo/odoo/addons,/home/ku/odoo_web/odoo/custom_addons
     ```

3. **Install Dependencies**:
   - Ensure Python 3.12 and Odoo dependencies (e.g., `lxml`) are installed.

4. **Update Module List**:
   - Run:
     ```bash
     ./odoo-bin -c /path/to/odoo.conf -u share_management
     ```

5. **Install Module**:
   - In Odoo, go to **Apps**, update the apps list, search for `share_management`, and click **Install**.

6. **Set Permissions**:
   - In **Settings** > **Users & Companies** > **Groups**, assign users to:
     - **Share Manager**: Full access.
     - **Share Viewer**: Read-only.

## Usage
### 1. Shareholders
- Go to **Shareholders** to add/edit records.
- Fields: Name, Partner, Total Shares, Total Invested, Share %, Dividends.
- Features: Smart buttons for shares, percentage, dividends; lists of transactions and dividends.

### 2. Share Transactions
- In **Share Transactions**, log buy, sell, or transfer actions.
- Fields:
  - Shareholder, Type (Buy/Sell/Transfer), Quantity, Price per Share, Amount, Receiver (for transfers), Date.
- Updates shareholder shares and investment automatically.

### 3. Dividends
- In **Dividends**, record payments.
- Fields: Shareholder, Amount, Date.
- Totals update in shareholder records.

### 4. CSV Import
- Use `share_transaction_import_template.csv` for bulk imports.
- **Steps**:
  1. Go to **Share Transactions** > **Import**.
  2. Upload the CSV with:
     ```csv
     shareholder_id,type,quantity,price_per_share,amount,receiver_id,date
     "John Doe",Buy,100,10.00,1000.00,,2025-07-01
     "Jane Smith",Sell,50,12.00,600.00,,2025-07-02
     "John Doe",Transfer,20,0.00,0.00,"Jane Smith",2025-07-03
     ```
  3. Map fields and import. Shareholders are created automatically if they don't exist.

### 5. Dashboard
- Access via **Shareholders** menu.
- Shows: Pie/bar chart of share distribution, recent transactions, and dividends.

## Sample Test Data
1. **Shareholders**:
   - John Doe: 0 shares, 0 invested.
   - Jane Smith: 0 shares, 0 invested.
2. **Transactions**:
   - John Doe: Buy 100 shares, 10 each, 2025-07-01.
   - Jane Smith: Sell 50 shares, 12 each, 2025-07-02.
   - John Doe: Transfer 20 shares to Jane Smith, 2025-07-03.
3. **Dividends**:
   - John Doe: 500, 2025-07-04.
   - Jane Smith: 300, 2025-07-04.
4. **Verify**: Check updated shares, percentages, and dashboard.
