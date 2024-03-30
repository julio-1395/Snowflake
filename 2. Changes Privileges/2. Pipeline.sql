
--Grant SELECT and INSERT privileges directly to the users
GRANT SELECT, INSERT ON TABLE production.Sales TO USER Marcos, Tomas, James, Lucia, Carlos;

--Grant privileges to a role
GRANT SELECT, INSERT ON TABLE production.Sales TO ROLE production_role;

--Add the users to the role
GRANT production_role TO USER Marcos, Tomas, James, Lucia, Carlos;

--See Current Privileges
SHOW GRANTS ON TABLE production.Sales;
