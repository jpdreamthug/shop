import React, { useEffect } from "react";
import AppRoutes from "./Routes";
import Header from "./Header";
import Footer from "./Footer";
import Sidebar from "./Sidebar";
import "../styles/App.css";
import { useDispatch } from "react-redux";
import { getCategories } from "../features/categories/categoriesSlice";

const App = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getCategories());
  }, [dispatch]);

  return (
    <div className="app">
      <Header />
      <div className="container">
        <Sidebar />
        <AppRoutes />
      </div>
      <Footer />
    </div>
  );
};

export default App;
