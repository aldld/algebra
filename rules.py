"""
List of rules for pattern matching and substitution

== Pattern: ==

'?<type> <x>' assigns the name <x> in the dictionary to the value found in that
position of the expression with the following possible types:
    - ?c: constant
    - ?v: variable or expression
    - ?: constant, variable or expression
    - ?o: operator

== Skeleton: ==

':(<name>)' substitutes the value from the dictionary assigned to the key <name>
into its position in the resulting expression.

`(<operation>) substitutes in the string 'operations[<operation>]', which is associated
with the class representing <operation>.

{<Python expression>}: Evaluate an expression in the Python interpreter and
substitute the result of the expression in its place. Example:
    {
        'pattern': [':o operation', '?c c1', '?c c2'],
        'rule':    '{`(:(operation))(:(c1), :(c2)).evaluate()}'
    }
    
    On the expression ['+', '2', '3']
    Substitues in the result of operations['+'](2, 3).evaluate() (= 5)
"""

from operations import operations

# NOTE: Patterns must match exactly => commutative property is ignored, must be
# explicitly accounted for!
realNumberRules = [
    
    # Replace an expression containing only one element with an atom
    {
        'pattern':  ['? atom'],
        'skeleton': ':(atom)'
    },
    
    # Evaluating an operation on constants
    {
        'pattern':  ['?o operation', '?c c1', '?c c2'],
        'skeleton': '{`(:(operation))(:(c1), :(c2)).evaluate()}'
    },
    
    # Additive identity a + 0 = a
    {
        'pattern':  ['+', '? a', 0],
        'skeleton': ':(a)'
    },
    {
        'pattern':  ['+', 0, '? a'],
        'skeleton': ':(a)'
    },
    
    # Multiplicative identity a * 1 = a
    {
        'pattern':  ['*', '? a', 1],
        'skeleton': ':(a)'
    },
    {
        'pattern':  ['*', 1, '? a'],
        'skeleton': ':(a)'
    },
    
    # Multiplication by zero a*0 = 0
    {
        'pattern':  ['*', '? a', 0],
        'skeleton': 0
    },
    {
        'pattern':  ['*', 0, '? a'],
        'skeleton': 0
    },
    
    # Left distributive property a*(b + c) = (a*b) + (a*c)
    {
        'pattern':  ['*', '? a', ['+', '? b', '? c']],
        'skeleton': ['+', ['*', ':(a)', ':(b)'], ['*', ':(a)', ':(c)']]
    },
    
    # Right distributive property (a + b)*c = (a*c) + (b*c)
    {
        'pattern':  ['*', ['+', '? a', '? b'], '? c'],
        'skeleton': ['+', ['*', ':(a)', ':(c)'], ['*', ':(b)', ':(c)']]
    }
    
    # To be continued...
    
]
