-- Verify existing user's email (for development)
-- Run this in Neon DB SQL Editor

-- Update user's emailVerified status to true
UPDATE "user" 
SET "emailVerified" = TRUE 
WHERE email = 'donia1510aptech@gmail.com';

-- Verify the update
SELECT id, email, name, "emailVerified", "role", "isAdmin" 
FROM "user" 
WHERE email = 'donia1510aptech@gmail.com';

