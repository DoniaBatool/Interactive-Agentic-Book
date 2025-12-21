-- Migration: Add role and isAdmin columns to user table
-- Run this in your database console

-- Add role column
ALTER TABLE "user" 
ADD COLUMN IF NOT EXISTS "role" TEXT DEFAULT 'user';

-- Add isAdmin column
ALTER TABLE "user" 
ADD COLUMN IF NOT EXISTS "isAdmin" BOOLEAN DEFAULT FALSE;

-- Update existing users to have default role
UPDATE "user" 
SET "role" = 'user', "isAdmin" = FALSE 
WHERE "role" IS NULL OR "isAdmin" IS NULL;

-- Create index on role for faster queries
CREATE INDEX IF NOT EXISTS "user_role_idx" ON "user"("role");

