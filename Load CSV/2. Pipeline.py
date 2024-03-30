import snowflake.connector
import boto3

# Snowflake connection parameters
snowflake_account = 'your_account_name'
snowflake_user = 'your_username'
snowflake_password = 'your_password'
snowflake_database = 'your_database'
snowflake_schema = 'your_schema'

# AWS S3 credentials and parameters
aws_access_key = 'your_aws_access_key'
aws_secret_key = 'your_aws_secret_key'
aws_region = 'your_aws_region'
s3_bucket = 'your_s3_bucket'
s3_folder = '1st Quarter/'

# Initialize Snowflake connection
conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    database=snowflake_database,
    schema=snowflake_schema
)

# Initialize AWS S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

# List of CSV files
csv_files = ['Sales.csv', 'Costs.csv', 'Electricity.csv', 'Transport.csv', 'Human Resources.csv', 'Investment.csv']

# Loop through each CSV file and load into Snowflake
for file_name in csv_files:
    # Construct the S3 file path
    s3_file_path = f'{s3_folder}{file_name}'

    # Snowflake table name (remove .csv extension)
    table_name = file_name.split('.')[0]

    # Snowflake COPY INTO command
    copy_into_query = f'''
    COPY INTO {table_name}
    FROM s3://{s3_bucket}/{s3_file_path}
    CREDENTIALS=(
        aws_key_id='{aws_access_key}',
        aws_secret_key='{aws_secret_key}'
    )
    FILE_FORMAT=(
        TYPE=CSV,
        FIELD_OPTIONALLY_ENCLOSED_BY='"',
        SKIP_HEADER=1
    );
    '''

    # Execute the COPY INTO command
    conn.cursor().execute(copy_into_query)

# Close Snowflake connection
conn.close()
