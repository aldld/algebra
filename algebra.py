import rules

def dictionary(expression, pattern):
    """ Returns a dictionary of variables {'name': <name (from pattern)>, 'value': <value (from expression)>}
        Returns False if the expression does not match the pattern """
    
    variables = {}
    
    if isinstance(pattern, list):
        # If pattern is a list, expression must also be a list to match.
        if not isinstance(expression, list): return False
        # They must also be the same length
        if len(expression) != len(pattern): return False
        
        # Recurse into subexpressions and subpatterns
        for subexpr, subpat in zip(expression, pattern):
            subdict = dictionary(subexpr, subpat)
            
            if not (bool(subdict) or (subdict == {})):
                return False
            
            # Ensure there are no naming conflicts between the subdictionary and the
            # current-level dictionary
            for name in subdict.keys():
                if name in variables.keys():
                    if subdict[name] != variables[name]: return False
            
            # No naming conflicts; merge the subdictionary with the current-level dictionary
            #variables = dict(variables.items() + subdict.items())
            variables.update(subdict)
            
    else: # Pattern is atomic
        tentativeVariable = {}
        if isinstance(pattern, str):
            if pattern[0] == '?': # Pattern is defining a variable
                if pattern[1] == 'c': # Constant
                    if isinstance(expression, (int, float)):
                        tentativeVariable['name'] = pattern[3:]
                        tentativeVariable['value'] = expression
                    else: return False
                elif pattern[1] == 'v': # Variable or list
                    if isinstance(expression, (str, list)):
                        tentativeVariable['name'] = pattern[3:]
                        tentativeVariable['value'] = expression
                    else: return False
                elif pattern[1] == ' ': # Constant, variable or list
                    if isinstance(expression, (str, list, int, float)):
                        tentativeVariable['name'] = pattern[2:]
                        tentativeVariable['value'] = expression
                    else: return False
                elif pattern[1] == 'o': # Operator
                    if isinstance(expression, str):
                        tentativeVariable['name'] = pattern[3:]
                        tentativeVariable['value'] = expression
                    else: return False
            else: # Pattern is a definite variable
                if expression != pattern: return False
        else: # Pattern is a constant
            if expression != pattern: return False
        
        if bool(tentativeVariable):
            # Ensure the tentative variable does not conflict with existing variables
            if tentativeVariable['name'] in variables.keys():
                if tentativeVariable['value'] != variables[tentativeVariable['name']]:
                    return False
            
            variables[tentativeVariable['name']] = tentativeVariable['value']
    
    return variables

def partMatch(expression, rule):
    """ Tests expression/pattern match when at least one argument is atomic. """
    
    if isinstance(expression, list) and isinstance(rule, list):
        raise Exception("expression and rule cannot both be lists.")
    
def matches(expression, pattern):
    """ Returns True if the expression matches the rule's pattern, False if it
        does not. """
    
    """
    # Expression and pattern are both lists
    if isinstance(expression, list) and isinstance(rule['pattern'], list):
        # For an expression to match, it must have the same number of parts as the pattern
        if len(expression) != len(rule['pattern']): return False
        
        # Test individual parts of the expression and pattern
        for subexpr, subpat in zip(expression, rule['pattern']):
            # Subexpression and subpattern are both lists
            if isinstance(subexpr, list) and isinstance(subpat, list):
                if not match(subexpr, subpat): return False
                continue
            
            if not partMatch(subexpr, subpat): return False
        
        return True
    
    else:
        return partMatch(expression, rule)
    """
    
    d = dictionary(expression, pattern)
    """
    if bool(d) or (d == {}):
        print(pattern)
        print(d)
    """
    return bool(d) or (d == {})

def simplified(expression, ruleList=rules.realNumberRules):
    """ Returns True if the expression does not match any patterns (cannot be simplified
        further), False if it does match a pattern. """
    
    for rule in ruleList:
        if matches(expression, rule['pattern']): return False
    
    return True

def getMatchingRule(expression, ruleList=rules.realNumberRules):
    """ Returns the first rule in ruleList whose pattern matches the given
        expression. Returns None if no matching rules found. """
    
    for rule in ruleList:
        if matches(expression, rule): return rule
    
    return None

def applyRule(expression, rule):
    """ Applies the given rule to the given expression.
        Assumes that the expression matches the rule's pattern! """
    
    variableDict = dictionary(expression, rule['pattern'])
    
    if not (bool(d) or d == {}):
        raise Exception("Expression does not match rule")
    
    result = rule['skeleton']
    
    

def simplify(expression, ruleList=rules.realNumberRules):
    """ Accepts an expression in list structure and returns a new expression
        simplified according to the rules specified. """
    
    # If an expression is atomic, assume it is already simplified
    if not isinstance(expression, list): return
    
    # Simplify individual subexpressions
    for subexpr in expression:
        simplify(subexpr, ruleList)
    
    # Simplify the expression itself
    while not simplified(expression):
        rule = getMatchingRule(expression, ruleList)
        applyRule(expression, rule)
    
    # Finished simplifying
    
if __name__ == '__main__':
    e = ['*', ['+', 'y', 'z'], 'x']
    print(simplify(e))
