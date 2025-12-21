-- Make a user admin by email
-- Usage: Update the email address below and run this in your database

UPDATE "user" 
SET 
    "isAdmin" = TRUE,
    "role" = 'admin'
WHERE "email" = 'your-email@example.com';

-- Verify the update
SELECT id, email, name, "isAdmin", role, "emailVerified" 
FROM "user" 
WHERE "email" = 'your-email@example.com';

