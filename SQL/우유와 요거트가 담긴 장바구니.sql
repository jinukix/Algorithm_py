SELECT A.CART_ID FROM
(SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Yogurt') as A,
(SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Milk') as B
WHERE A.CART_ID = B.CART_ID