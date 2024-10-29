import React from 'react';
import { Link } from 'react-router-dom';
import styles from '../styles/Product.module.css';

const Products = ({ title }) => {
  return (
    <section>{title && <h2>{title}</h2>}
      
    </section>
  )
}
