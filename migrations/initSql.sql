DO
'
DECLARE
BEGIN
    set role "auroraAI";
    RAISE INFO ''role set'';
    
    EXCEPTION WHEN OTHERS THEN
    RAISE INFO ''role not set. local environment'';
END;
' LANGUAGE PLPGSQL;