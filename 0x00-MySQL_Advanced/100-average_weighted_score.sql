-- Create stored procedure ComputeAverageWeightedScoreForUser
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE avg_weighted_score FLOAT;

    -- Calculate total weighted score and total weight
    SELECT SUM(p.weight * c.score), SUM(p.weight)
    INTO total_weighted_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Compute average weighted score
    IF total_weight > 0 THEN
        SET avg_weighted_score = total_weighted_score / total_weight;
    ELSE
        SET avg_weighted_score = 0;
    END IF;

    -- Update users table with the computed average weighted score
    UPDATE users
    SET average_score = avg_weighted_score
    WHERE id = user_id;

    -- Select the updated user information
    SELECT * FROM users WHERE id = user_id;

END //

DELIMITER ;
