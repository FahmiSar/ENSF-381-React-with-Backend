import React from 'react';

const CartItem = ({ item, removeFromCart }) => {

  const handleRemove = (item) =>{
    removeFromCart(item);
  }

  const calculateCostForOne = (item) => {
    return(item.price * item.quantity).toFixed(2);
  }

  return (
    <div className="cart-item">
      <img src={item.image} alt={item.name} />
      <div className="item-details">
        <p className="item-name">{item.name}</p>
        <p className="item-price">${item.price}</p>
        <p className="item-quantity">Quantity: {item.quantity}</p>
        <p className="item-total-cost">Total Cost: ${calculateCostForOne(item)}</p>
        <button onClick={() => handleRemove(item)}>Remove</button>
      </div>
    </div>
  );
};

export default CartItem;
