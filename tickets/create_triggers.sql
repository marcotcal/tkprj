-- TRIGGERS CREATION --

-- LOG STATUS CHANGES

DROP TRIGGER IF EXISTS do_write_status_log ON tickets.ticket;

CREATE OR REPLACE FUNCTION tickets.write_status_log()
  RETURNS trigger AS
$BODY$
BEGIN
  		
    IF new.status_id != old.status_id THEN
        IF new.status_id = 2 AND old.status_id != 2 AND old.begin_time IS NULL THEN
           new.begin_time = current_timestamp;
        END IF;  	
        IF new.status_id = 6 AND old.status_id != 6 THEN
            new.close_time = current_timestamp;
        END IF;
        INSERT INTO tickets.ticket_change_log (ticket_id, log_time, status_from_id, status_to_id, user_id)
        VALUES (new.id, current_timestamp, old.status_id, new.status_id, new.updated_by_id);
    END IF;
	
    RETURN new;
   
END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;

CREATE TRIGGER do_write_status_log
  BEFORE UPDATE
  ON tickets.ticket
  FOR EACH ROW
  EXECUTE PROCEDURE tickets.write_status_log();