# Simple Mock class. All calls to the attributes return another Mock instance. If the attribute is set, call to it returns that value

from unittest import mock
m = mock.Mock()

m.aaaa


# 1. Single return value

m.return_value = 1

# 2. Side effect

m.side_effect = [1,2,3]

# What will happen when list exhausted?

# Side effect can raise an exception

m.side_effect = [RuntimeError('1'), KeyError('2')]

try: 
    m() 
except RuntimeError: 
    print('we catched runtime error') 
except KeyError: 
    print('we catched key error') 


# 3. Assertions and getting arguments

# Check if the mock was called
m.assert_called_once()

# Count of mock calls
# m.call_count

# return object mock.call with arguments passed to it
# m.call_args
# example:
m.side_effect = [1,2]
m(a=1, b=2)
assert m.call_args == mock.call(a=1,b=2)

# List of all calls of the mock
m.call_args_list


# 4. MagicMock class - magic methods are implemented
# example:
m1 = mock.Mock()
m2 = mock.MagicMock()
try:
    iterator = iter(m1)
except Exception as exc:
    print(exc)
iterator = iter(m2)

# 5. Patching the stuff
# examples in core.py and tests.py
# Testing state and behavior
# - the inner state of the tested object after function
# - the mock method was called with right arguments etc
# Testing with controlled input/output from mock
