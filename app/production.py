# First Set
first_comm = ["comment", "null"]
first_global_dec = ["const", "classic", "sheriff",
                    "agent", "roster", "map", "site", "omen"]
first_const_dec = ["const"]
first_const_dec1 = [","]
first_data_type = ["classic", "sheriff", "agent", "roster", "map"]
first_value = ["classic_literal", "neg_classic_literal", "sheriff_literal",
               "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend"]
first_map_lit = ["attack", "defend"]
first_conc = ["&"]
first_var_dec = ["classic", "sheriff", "agent", "roster", "map"]
first_init = ["="]
first_var_dec1 = [","]
first_array_dec = ["classic", "sheriff", "agent", "roster", "map"]
first_index = ["classic_literal", "id"]
first_func_stmt = ["id"]
first_args = ["id", "classic_literal", "neg_classic_literal", "sheriff_literal",
              "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend"]
first_variable = ["id"]
first_more_args = [","]
first_array_elem = ["id"]
first_array_index2 = ["["]
first_array_index3 = ["["]
first_struct_elem = ["id"]
first_array_value = ["classic_literal", "neg_classic_literal", "sheriff_literal",
                     "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend", "{"]
first_array_value1 = ["classic_literal", "neg_classic_literal", "sheriff_literal",
                      "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend"]
first_more_array = [","]
first_array_value2 = ["{"]
first_more_array2 = [","]
first_array_value3 = ["{"]
first_more_array3 = [","]
first_struct_dec = ["site"]
first_site_element = ["classic", "sheriff", "agent", "roster", "map"]
first_more_element = ["classic", "sheriff", "agent", "roster", "map"]
first_site_var = ["id"]
first_more_var_site = [",", "null"]
first_func_dec = ["classic", "sheriff", "agent", "roster", "map", "omen"]
first_func_type = ["classic", "sheriff", "agent", "roster", "map", "omen"]
first_param = ["classic", "sheriff", "agent", "roster", "map", "null"]
first_param1 = [",", "null"]
first_local_dec = ["classic", "sheriff", "agent", "roster", "map", "const", "site", "null"]
first_struct_init = ["site"]
first_more_struct = [",", "null"]
first_statements = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id", "++", "--", "defuse",
                    "shoot", "if", "switch", "for", "while", "do", "null"]
first_statement1 = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id", "++", "--", "defuse",
                    "shoot", "if", "switch", "for", "while", "do"]
first_expre_stmt = ["id", "++," "--"]
first_assign_expr = ["id"]
first_assign_op = ["=", "=+", "=-", "=*", "=/", "=^", "=//", "=%"]
first_assign_operand = ["id", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal", "agent_literal", 
                        "roster_literal", "attack", "defend", "++," "--", "(", "and", "or", "n"]
first_expre_stmt1 = [ "id", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal", "++", "--" , "(", "and", "or" , "n"]
first_arith_expr = [ "id", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal", "++", "--" , "("]
first_arith_operand = [ "id", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal", "++", "--" , "("]
first_num_val = ["classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_litera"]
first_una_expr = ["++", "--", "id"]
first_una_op = ["++", "--"]
first_arith_op = ["+", "-", "*", "^", "/", "//", "%"]
first_rela_expr = [ "id", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal", "++", "--" , "("]
first_rela_operand = [ "id", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal", "++", "--" , "("]
first_rela_op = ["==", "=!", "=>", "=<", "<", ">"]
first_log_expr = ["and", "or", "n"]
first_log_expr1 = ["and", "or"]
first_log_expr2 = ["n"]
first_log_op = ["and", "or"]
first_log_operand = ["and", "or", "n" , "id", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal", "++," "--" , "(" , "attack", "defend"]
first_ret_stmt = ["defuse"]
first_ret_operand = ["id", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend", "++", "--", "(", "and", "or", "n"]
first_in_stmt = ["aim"]
first_in_operand = ["id"]
first_out_stmt = ["shoot"]
first_out_operand = [ "id", "\"", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal", "++", "--", "(", "and", "or", "n", "fs"]
first_str_form = ["{", "null"]
first_str_var = ["{", "null"]
first_condi_stmt = ["if", "switch"]
first_if_stmt = ["if"]
first_condition = ["id", "attack", "defend", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal", "(", "++", "--", "and", "or", "n"]
first_if_stmt1 = ["elif", "null"]
first_if_stmt2 = ["else", "null"]
first_switch_stmt = ["switch"]
first_case_literal = ["classic_literal", "agent_literal"]
first_more_votes = ["vote", "null"]
first_break = ["kill", "null"]
first_loop_stmt = ["for", "while", "do"]
first_for_stmt = ["for"]
first_for_init = ["id"]
first_loop_cond = [ "id", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal", "++", "--" , "(", "and", "or" , "n"]
first_break_con = ["revive", "kill"]
first_while_stmt = ["while"]
first_dowhile_stmt = ["do"]
first_function_def = ["plant", "null"]

# Follow Set
follow_comm = ["const", "classic", "sheriff", "agent", "roster", "map", "site", "omen", "#", "bound",  "id",  "++", '--', 
              "defuse", "aim", "shoot", "if", "switch", "for", "while", "do", "}", "plant", "$", "kill", "revive"]
follow_global_dec = ["#", "bound"]
follow_const_dec = [";"]
follow_const_dec1 = [";"]
follow_data_type = ["id", "arr"]
follow_value = [",", ";", ")", "}"]
follow_map_literal = [",", ";", ")", "}"]
follow_conc = [",", ";", ")", "}"]
follow_var_dec = [";"]
follow_init = [",", ";"]
follow_var_dec1 = [";"]
follow_array_dec = [";"]
follow_index = ["]"]
follow_func_stmt = [ "]" , ";" , "+", "-", "*", "^", "/", "//", "%", ")", "==", "=!", "=>", "=<", ">", "<", ",", ")"]
follow_args = [")"]
follow_variable = ["," , ")", ".", "+", "-", "*", "^", "/", "//", "%", "==", "=!", "=>", "=<", ">", "<" , ";", "++", "--", "=", "=+", "=-", "=*", "=/", "=^", "=//", "=%"]
follow_more_args = [")"]
follow_array_elem = ["," , ")", ".", "+", "-", "*", "^", "/", "//", "%", "==", "=!", "=>", "=<", ">", "<" , ";", "++", "--", "=", "=+", "=-", "=*", "=/", "=^", "=//", "=%"]
follow_array_index2 = ["[", "id", "," , ")", ".", "+", "-", "*", "^", "/", "//", "%", "==", "=!", "=>", "=<", ">", "<" , ";", "++", "--", "=", "=+", "=-", "=*", "=/", "=^", "=//", "=%"]
follow_array_index3 = ["id", "," , ")", ".", "+", "-", "*", "^", "/", "//", "%", "==", "=!", "=>", "=<", ">", "<" , ";", "++", "--", "=", "=+", "=-", "=*", "=/", "=^", "=//", "=%"]
follow_struct_elem = ["," , ")", ".", "+", "-", "*", "^", "/", "//", "%", "==", "=!", "=>", "=<", ">", "<" , ";", "++", "--", "=", "=+", "=-", "=*", "=/", "=^", "=//", "=%"]
follow_array_value = ["}"]
follow_array_value1 = ["}"]
follow_more_array = ["}"]
follow_array_value2 = ["}"]
follow_more_array2 = ["}"]
follow_array_value3 = ["}"]
follow_more_array3 = ["}"]
follow_struct_dec = [";"]
follow_site_element = ["}"]
follow_more_element = ["}"]
follow_site_var = [";"]
follow_more_var_site = [";"]
follow_func_dec = [";"]
follow_func_type = ["id"]
follow_param = [")"]
follow_param1 = [")"]
follow_local_dec = [ "#",  "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",  "++", "--", "defuse", "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
follow_struct_init = [";"]
follow_more_struct = ["}"]
follow_statements = ["#", "kill", "revive"]
follow_statement1 = [ "#",  "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",  "++", "--", "defuse", "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
follow_expre_stmt = [";"]
follow_assign_expr = [";"]
follow_assign_op = ["id", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend", "++", "--", "(", "and", "or", "n"]
follow_assign_operand = [";"]
follow_expre_stmt1 = [";", ")"]
follow_arith_expr = [ ";", "+", "-", "*", "^", "/", "//", "%", ")", "==", "=!", "=>", "=<", ">", "<", ";", ","]
follow_arith_operand = [ ";", "+", "-", "*", "^", "/", "//", "%", ")", "==", "=!", "=>", "=<", ">", "<", ";", ","]
follow_num_val = [ ";", "+", "-", "*", "^", "/", "//", "%", ")", "==", "=!", "=>", "=<", ">", "<", ";", ","]
follow_una_expr = [ ";", "+", "-", "*", "^", "/", "//", "%", ")", "==", "=!", "=>", "=<", ">", "<", ";", ","]
follow_una_op = [ "id",";", "+", "-", "*", "^", "/", "//", "%", ")", "==", "=!", "=>", "=<", ">", "<", ";", ","]
follow_arith_op = [ "id", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal", "++", "--" , "(" ]
follow_rela_expr = [";", ")", ","]
follow_rela_operand = [ "==", "=!", "=>", "=<", ">", "<", ";", ")", ","]
follow_rela_op = [ "id", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal", "++", "--" , "(" ]
follow_log_expr = [";", ")", ","]
follow_log_expr1 = [";", ")", ","]
follow_log_expr2 = [";", ")", ","]
follow_log_op = [")"]
follow_log_operand = [",", ")"]
follow_ret_stmt = [";"]
follow_in_stmt = [";"]
follow_in_opernd = [")"]
follow_out_stmt = [";"]
follow_out_operand = [")"]
follow_str_form = ["\""]
follow_str_var = ["roster_literal", "{", "\""]
follow_condi_stmt = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",  "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}" , "kill", "revive"]
follow_if_stmt = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",  "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}" , "kill", "revive"]
follow_condition = [")"]
follow_if_stmt1 = ["else","#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",  "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}" , "kill", "revive"]
follow_if_stmt2 = ["else","#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",  "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}" , "kill", "revive"]
follow_switch_stmt = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",  "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}" , "kill", "revive"]
follow_case_literal = [":"]
follow_more_votes = ["base"]
follow_break = ["}"]
follow_loop_stmt = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",  "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}" , "kill", "revive"]
follow_for_stmt = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",  "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}" , "kill", "revive"]
follow_for_init = [";"]
follow_loop_cond = [";", ")"]
follow_break_con = ["}"]
follow_while_statement = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",  "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}" , "kill", "revive"]
follow_dowhile_stmt = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",  "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}" , "kill", "revive"]
follow_function_def = ["#", "$"]