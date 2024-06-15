-- Ensure the index does not already exist
DROP INDEX IF EXISTS idx_name_first_score ON names;

-- Create the index on the first letter of name and score
CREATE INDEX idx_name_first_score ON names (SUBSTRING(name, 1, 1), score);
