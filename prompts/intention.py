intentions = f"""
CONTEXT: 
    1. You will answer 0 or 1 based in your input.

TASKS: 
    1. You are tasked for summarizing their input in one number according their message following the label in our database
    2. Your objective is understand what is the intention of user
    3. There are 2 intentions 
        0 - Explorer
        1 - Not Explorer

EXAMPLES:
    ##note: These examples are for you undestand how to work.   

        Example 1: 
            user message: 
            Como você pode me ajudar?
            recommended answer:
            0
        
        Example 2: 
            user message: 
            Como você foi criado
            recommended answer:
            0
        
        Example 3: 
            user message: 
            Quanto gastei na no mês de dezembro?
            recommended answer:
            1

        Example 4: 
            user message: 
            Liste um top 3 áreas que mais gastei
            recommended answer:
            1
 """
