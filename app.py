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

# Route for the Parts table.
# This route will handle requests to http://127.0.0.1:5000/parts
@app.route('/parts', methods=['GET'])
def get_parts():
    """Fetches all records from the PARTS table."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    data = conn.execute('SELECT * FROM PARTS').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the Suppliers table.
# This route will handle requests to http://127.0.0.1:5000/suppliers
@app.route('/suppliers', methods=['GET'])
def get_suppliers():
    """Fetches all records from the SUPPLIERS table."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    data = conn.execute('SELECT * FROM SUPPLIERS').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the PART_SUPPLIERS table.
# This route will handle requests to http://127.0.0.1:5000/part_suppliers
@app.route('/part_suppliers', methods=['GET'])
def get_part_suppliers():
    """Fetches all records from the PART_SUPPLIERS table."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    data = conn.execute('SELECT * FROM PART_SUPPLIERS').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the PROCUREMENT_EVENTS table.
# This route will handle requests to http://127.0.0.1:5000/procurement_events
@app.route('/procurement_events', methods=['GET'])
def get_procurement_events():
    """Fetches all records from the PROCUREMENT_EVENTS table."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    data = conn.execute('SELECT * FROM PROCUREMENT_EVENTS').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# Route for the CDSIDS table.
# This route will handle requests to http://127.0.0.1:5000/cdsids
@app.route('/cdsids', methods=['GET'])
def get_cdsids():
    """Fetches all records from the CDSIDS table."""
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    data = conn.execute('SELECT * FROM CDSIDS').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

# --- Run the application ---
if __name__ == '__main__':
    # The 'debug=True' option provides helpful error messages during development.
    # The host='0.0.0.0' makes the server accessible externally.
    app.run(debug=True, host='0.0.0.0')
