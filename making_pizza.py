# import pizza_2


# pizza_2.make_pizza('pepperoni')
# pizza_2.make_pizza('mushrooms', 'green peppers', 'extra cheese')


# # we can as well give pizza_2.py module an alias


# import pizza_2 as p_2


# p_2.make_pizza('pepperoni')
# p_2.make_pizza('mushrooms', 'green peppers', 'extra cheese')



#Or we can import all functions in the module by asterisk instead of dot


from pizza_2 import *

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')