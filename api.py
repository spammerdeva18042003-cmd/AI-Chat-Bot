# Import the necessary libraries for the web framework and database interaction.
from flask import Flask, jsonify
import os, sqlite3

# Initialize the Flask application.
app = Flask(__name__)

# we are giving the full path to the database file.
# DB_FILE = r'C:\Users\devad\Documents\AI Chat bot\jlr_supplychain.db' 

# here we are giving the relative path to the database file.
DB_FILE = 'jlr_supplychain.db' 


def get_db_connection():

    # Check if the database file exists first
    # if not os.path.exists(DB_FILE):
    #     print(f"Error: Database file not found at {DB_FILE}")
    #     return None
    
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# This route will handle requests to http://127.0.0.1:5000/build_programs
@app.route('/build_programs', methods=['GET'])
def get_build_programs():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
    
    data = conn.execute('SELECT * FROM Build_Programs').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Parts table.
@app.route('/parts', methods=['GET'])
def get_parts():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Parts').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Suppliers table.
@app.route('/suppliers', methods=['GET'])
def get_suppliers():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Suppliers').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Supplier_Certifications table.
@app.route('/supplier_certifications', methods=['GET'])
def get_supplier_certifications():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Supplier_Certifications').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Supplier_Risk_Index table.
@app.route('/supplier_risk_index', methods=['GET'])
def get_supplier_risk_index():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Supplier_Risk_Index').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Supplier_Part_Relationship table.
@app.route('/supplier_part_relationship', methods=['GET'])
def get_supplier_part_relationship():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Supplier_Part_Relationship').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Inventory table.
@app.route('/inventory', methods=['GET'])
def get_inventory():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Inventory').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Purchase_Orders table.
@app.route('/purchase_orders', methods=['GET'])
def get_purchase_orders():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Purchase_Orders').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Purchase_Order_Items table.
@app.route('/purchase_order_items', methods=['GET'])
def get_purchase_order_items():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Purchase_Order_Items').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Products table.
@app.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Products').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Bill_Of_Materials table.
@app.route('/bill_of_materials', methods=['GET'])
def get_bill_of_materials():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Bill_Of_Materials').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Production_Schedule table.
@app.route('/production_schedule', methods=['GET'])
def get_production_schedule():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Production_Schedule').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Demand_Forecasts table.
@app.route('/demand_forecasts', methods=['GET'])
def get_demand_forecasts():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Demand_Forecasts').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Alternative_Parts table.
@app.route('/alternative_parts', methods=['GET'])
def get_alternative_parts():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Alternative_Parts').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Procurement_Triggers table.
@app.route('/procurement_triggers', methods=['GET'])
def get_procurement_triggers():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Procurement_Triggers').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Alerts_Events table.
@app.route('/alerts_events', methods=['GET'])
def get_alerts_events():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Alerts_Events').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Real_Time_Tracking table.
@app.route('/real_time_tracking', methods=['GET'])
def get_real_time_tracking():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Real_Time_Tracking').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Supplier_Performance_History table.
@app.route('/supplier_performance_history', methods=['GET'])
def get_supplier_performance_history():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM Supplier_Performance_History').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the PLM_Integration_Logs table.
@app.route('/plm_integration_logs', methods=['GET'])
def get_plm_integration_logs():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500
        
    data = conn.execute('SELECT * FROM PLM_Integration_Logs').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Run the application.
if __name__ == '__main__':
    # The 'debug=True' option provides helpful error messages during development.
    # The host='0.0.0.0' makes the server accessible externally.
    app.run(debug=True, host='0.0.0.0')

# import requests

# url = "https://b5602e2fa6c6.ngrok-free.app/build_programs"
# headers = {
#     "ngrok-skip-browser-warning": "1"
# }

# response = requests.get(url, headers=headers)
# print(response.json())

#https://73522787afa3.ngrok-free.app/