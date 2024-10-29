import React, { useState, useEffect } from 'react';
import styles from '../styles/Catalog.module.css';
import Product from './Product';

const Catalog = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios("products/");
        setProducts(response.data);
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    };

    fetchProducts();
  }, [])();

  return (
    <div className={styles.catalog}>

    </div>
  );
};

export default Catalog;
