
DROP PROCEDURE IF EXISTS LoopDemo;

DELIMITER $$
CREATE PROCEDURE LoopDemo()
BEGIN
    DECLARE num INT;
    SET num = 0;
    insertEntries : LOOP
         SET num = num + 1;
         SET @LocationX=  FLOOR(RAND()*(100-0+1)+0);
         SET @LocationY=  FLOOR(RAND()*(100-0+1)+0);
         SET @LocationID=  FLOOR(RAND()*(1000-0+1)+0);
         INSERT INTO locations (LocationID,LocationX,LocationY) VALUES (@LocationID,@LocationX,@LocationY);
         IF num = 100 THEN
            LEAVE insertEntries;
		END IF;
    END LOOP insertEntries;
END$$
DELIMITER ;