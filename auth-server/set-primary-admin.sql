-- Set donia1510aptech@gmail.com as primary admin
-- Run this in your Neon database console

-- Update the user to be admin
UPDATE "user" 
SET 
    "isAdmin" = TRUE,
    "role" = 'admin'
WHERE "email" = 'donia1510aptech@gmail.com';

-- Verify the update
SELECT id, email, name, "isAdmin", role, "emailVerified", "createdAt"
FROM "user" 
WHERE "email" = 'donia1510aptech@gmail.com';

-- If user doesn't exist, you'll need to create it first via sign-up
-- This script only updates existing users

