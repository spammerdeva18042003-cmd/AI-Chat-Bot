from flask import Flask, jsonify
import os, sqlite3

# Initialize the Flask application.
app = Flask(__name__)

# Define the database file path.
# Use a relative path, assuming the .db file is in the same directory as this Flask app.
DB_FILE = 'jlr_supply_chain.db'

def get_db_connection():
    """
    Establishes a connection to the SQLite database.
    Sets row_factory to sqlite3.Row to allow accessing columns by name.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# --- API Routes for Database Tables ---

# Route to get all parts
@app.route('/parts', methods=['GET'])
def get_all_parts():
    """Fetches all records from the PARTS table."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    data = conn.execute('SELECT * FROM PARTS').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route to get a specific part by part_number
# Example: http://127.0.0.1:5000/parts/XZL-1824-A or http://127.0.0.1:5000/parts/xzl-1824-a
@app.route('/parts/<string:part_number>', methods=['GET'])
def get_part_by_number(part_number):
    """Fetches a single part record by its part_number, case-insensitively."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    # Convert part_number to uppercase for case-insensitive lookup
    part_number_upper = part_number.upper()
    part = conn.execute('SELECT * FROM PARTS WHERE part_number = ?', (part_number_upper,)).fetchone()
    conn.close()

    if part is None:
        return jsonify({'error': 'Part not found'}), 404
    return jsonify(dict(part))

# Route to get all suppliers
@app.route('/suppliers', methods=['GET'])
def get_all_suppliers():
    """Fetches all records from the SUPPLIERS table."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    data = conn.execute('SELECT * FROM SUPPLIERS').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route to get a specific supplier by supplier_id
# Example: http://127.0.0.1:5000/suppliers/1
@app.route('/suppliers/<int:supplier_id>', methods=['GET'])
def get_supplier_by_id(supplier_id):
    """Fetches a single supplier record by its supplier_id."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    supplier = conn.execute('SELECT * FROM SUPPLIERS WHERE supplier_id = ?', (supplier_id,)).fetchone()
    conn.close()

    if supplier is None:
        return jsonify({'error': 'Supplier not found'}), 404
    return jsonify(dict(supplier))


# Route to get all part_suppliers relationships
@app.route('/part_suppliers', methods=['GET'])
def get_all_part_suppliers():
    """Fetches all records from the PART_SUPPLIERS table."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    data = conn.execute('SELECT * FROM PART_SUPPLIERS').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route to get part_suppliers relationships for a specific part_number
# Example: http://127.0.0.1:5000/part_suppliers/XZL-1824-A or http://127.0.0.1:5000/part_suppliers/xzl-1824-a
@app.route('/part_suppliers/<string:part_number>', methods=['GET'])
def get_part_suppliers_by_part_number(part_number):
    """Fetches all part-supplier relationships for a given part_number, case-insensitively."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    # Convert part_number to uppercase for case-insensitive lookup
    part_number_upper = part_number.upper()
    sql = """
        SELECT PS.*, S.supplier_name, S.geographical_location, S.certifications
        FROM PART_SUPPLIERS PS
        JOIN SUPPLIERS S ON PS.supplier_id = S.supplier_id
        WHERE PS.part_number = ?
    """
    data = conn.execute(sql, (part_number_upper,)).fetchall()
    conn.close()

    if not data:
        return jsonify({'error': 'No supplier relationships found for this part'}), 404
    return jsonify([dict(row) for row in data])


# Route to get all procurement_events
@app.route('/procurement_events', methods=['GET'])
def get_all_procurement_events():
    """Fetches all records from the PROCUREMENT_EVENTS table."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    data = conn.execute('SELECT * FROM PROCUREMENT_EVENTS').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route to get a specific procurement_event by event_id
# Example: http://127.0.0.1:5000/procurement_events/1
@app.route('/procurement_events/<int:event_id>', methods=['GET'])
def get_procurement_event_by_id(event_id):
    """Fetches a single procurement event record by its event_id."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    event = conn.execute('SELECT * FROM PROCUREMENT_EVENTS WHERE event_id = ?', (event_id,)).fetchone()
    conn.close()

    if event is None:
        return jsonify({'error': 'Procurement event not found'}), 404
    return jsonify(dict(event))

# Route to get all cdsids
@app.route('/cdsids', methods=['GET'])
def get_all_cdsids():
    """Fetches all records from the CDSIDS table."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    data = conn.execute('SELECT * FROM CDSIDS').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route to get a specific cdsid by cdsid string
# Example: http://127.0.0.1:5000/cdsids/DDHARSHA or http://127.0.0.1:5000/cdsids/ddharsha
@app.route('/cdsids/<string:cdsid>', methods=['GET'])
def get_cdsid_by_id(cdsid):
    """Fetches a single CDSID record by its cdsid string, case-insensitively."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    # Convert CDSID to uppercase for case-insensitive lookup
    cdsid_upper = cdsid.upper()
    data = conn.execute('SELECT * FROM CDSIDS WHERE cdsid = ?', (cdsid_upper,)).fetchone()
    conn.close()

    if data is None:
        return jsonify({'error': 'CDSID not found'}), 404
    return jsonify(dict(data))

@app.route('/execute_sql', methods=['GET'])
def execute_raw_sql_query():
    """
    Executes a raw SQL query provided as a URL query parameter.
    Highly insecure and vulnerable to SQL Injection. Use only for local testing.
    """
    sql_query = request.args.get('query') # Get the 'query' parameter from the URL

    if not sql_query:
        return jsonify({'error': 'No SQL query provided in the "query" parameter.'}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    try:
        # !!! DANGER: Directly executing user-provided SQL !!!
        cursor = conn.execute(sql_query)
        # For SELECT queries, fetch results
        if sql_query.strip().upper().startswith('SELECT'):
            data = cursor.fetchall()
            response_data = [dict(row) for row in data]
        else:
            # For non-SELECT queries (INSERT, UPDATE, DELETE, CREATE, DROP), commit changes
            conn.commit()
            response_data = {'message': 'SQL command executed successfully', 'rows_affected': cursor.rowcount}
    except sqlite3.Error as e:
        conn.rollback() # Rollback changes if an error occurs
        return jsonify({'error': f'Database query error: {e}'}), 400
    finally:
        conn.close()

    return jsonify(response_data)
# --- Run the application ---
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

