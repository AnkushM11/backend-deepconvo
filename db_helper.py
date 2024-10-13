import psycopg2
global cnx

# Establish the connection
cnx = psycopg2.connect(
    host="ep-shy-feather-a5rr4wlg.us-east-2.aws.neon.tech",
    user="deepconvo_owner",
    password="9moSFhlbO1vY",
    database="deepconvo"
)

def view_budget(campaign_name: str):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = f"SELECT budget FROM CAMPAIGN WHERE campaignName = %s"
    cursor.execute(query,(campaign_name,))

    # Fetching the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # Returning the order status
    if result:
        return result[0]
    else:
        return None

# Function to fetch the order status from the order_tracking table
def view_total_spend(campaign_name: str):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = f"SELECT totalSpend FROM CAMPAIGN WHERE campaignName = %s"
    cursor.execute(query,(campaign_name,))

    # Fetching the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # Returning the order status
    if result:
        return result[0]
    else:
        return None

def view_current_status(campaign_name: str):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = f"SELECT status FROM CAMPAIGN WHERE campaignName = %s"
    cursor.execute(query,(campaign_name,))

    # Fetching the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # Returning the order status
    if result:
        return result[0]
    else:
        return None

def edit_budget(campaign_name: str, budget: float):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = f"UPDATE CAMPAIGN SET budget = %s WHERE campaignName = %s;"
    cursor.execute(query,(budget,campaign_name))

    # Fetching the result
    cnx.commit()

    # Closing the cursor
    cursor.close()

    return

def edit_status(campaign_name: str, status: str):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = f"UPDATE CAMPAIGN SET status = %s WHERE campaignName = %s;"
    cursor.execute(query,(status,campaign_name))

    # Fetching the result
    cnx.commit()

    # Closing the cursor
    cursor.close()

    return