-- 10 MySql queries
-- 1. Create databse
CREATE DATABASE schooldb;
USE schooldb;

-- 2. Creating table TEACHERS;
CREATE TABLE teachers (
    id INT NOT NULL AUTO_INCREMENT,
    teacher_name VARCHAR(20) NOT NULL,
    sex CHAR(1),
    phone_no VARCHAR(15) NOT NULL,
    qualification VARCHAR(10) NOT NULL,
    experience INT,
    PRIMARY KEY (id)
);

-- 3. Setting auto increment to id column using ALTER
ALTER TABLE teachers AUTO_INCREMENT=1;

-- 4. Inserting a row into teachers table
INSERT INTO teachers VALUES(
    1, "Param", 'M',
    "+91999912342", "PhD in CS",
    5
);

-- 5. Displaying data of teachers using SELECT
SELECT * FROM teachers;

-- 6. Inserting another row into teachers table (using auto increment value)
INSERT INTO teachers (
    teacher_name, sex, phone_no,
    qualification, experience
    ) VALUES (
    "Karan", "M", "+911234567890",
    "MBA", 2
);

-- 7. Updating a row
UPDATE teachers 
SET experience=3 
WHERE teacher_name="Karan";

-- 8. Showing count of each qualification
SELECT qualification, COUNT(*) as total_teachers 
FROM teachers
GROUP BY qualification;

-- 9. Displaying phone no. code of teachers
SELECT teacher_name, 
SUBSTRING(phone_no, 1, 3) AS phone_code 
FROM teachers;

-- 10. Deleting a row from teachers;
DELETE FROM teachers
WHERE id=2;