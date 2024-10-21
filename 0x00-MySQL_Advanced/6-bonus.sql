-- Create a 'stored procedure' named AddBonus
-- that insert values inside a designated table

DELIMITER $$

CREATE PROCEDURE AddBonus(
    IN userId INT,
    IN projectName VARCHAR(255),
    IN userScore INT
)
BEGIN
    -- Insert the project if it doesn't exist
    INSERT INTO projects (name)
    SELECT projectName
    WHERE NOT EXISTS (SELECT * FROM projects WHERE name = projectName LIMIT 1);

    -- Insert the input data into the intended table
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (
        userId,
        COALESCE((SELECT id FROM projects WHERE name = projectName), LAST_INSERT_ID()),
        userScore
    );

END $$
DELIMITER;
