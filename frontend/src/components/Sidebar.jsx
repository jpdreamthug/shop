import React from "react";
import { Link, NavLink } from "react-router-dom";
import styles from "../styles/Sidebar.module.css";
import { useSelector } from "react-redux";

const Sidebar = () => {
  const { list } = useSelector(({ categories }) => categories);

  console.log("list", list);

  return (
    <section className={styles.sidebar}>
      <div className={styles.title}>CATEGORIES</div>
      <nav>
        <ul className={styles.menu}>
          {list.map(({ id, name }) => (
            <li key={id}>
              <NavLink 
              className={({ isActive }) => `${styles.link} ${isActive ? styles.active: ""}`}
              to={`/categories/${id}`}>{name}
              </NavLink>
            </li>
          ))}
        </ul>
      </nav>
      <div className={styles.footerLinks}>
        <Link to="/help">Help</Link>
        <Link to="/terms">Terms & Conditions</Link>
      </div>
    </section>
  );
};

export default Sidebar;
