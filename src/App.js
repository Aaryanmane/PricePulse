import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <div className="container py-4">
      {/* Header */}
      <div className="bg-info text-white text-center py-3 mb-4">
        <h2>PricePulse - E-Commerce Price Tracker</h2>
      </div>

      {/* URL Input Section */}
      <div className="mb-4">
        <label htmlFor="amazonUrl" className="form-label">
          Enter Amazon Product URL:
        </label>
        <div className="input-group">
          <input
            type="text"
            className="form-control"
            id="amazonUrl"
            placeholder=""
          />
          <button className="btn btn-success">Track</button>
        </div>
      </div>

      {/* Product Preview Section */}
      <div className="mb-4">
        <h5 className="mb-3">Product Preview:</h5>
        <div className="card">
          <div className="row g-0">
            <div
              className="col-md-2 bg-light d-flex align-items-center justify-content-center"
              style={{ minHeight: "100px" }}
            >
              {/* Image Placeholder */}
              <div
                className="bg-secondary"
                style={{ width: "80px", height: "80px" }}
              ></div>
            </div>
            <div className="col-md-10 p-3">
              {/* Product details will be here */}
              <p>Product Name: </p>
              <p>Current Price: </p>
            </div>
          </div>
        </div>
      </div>

      {/* Price History Graph Section */}
      <div className="mb-4">
        <h5 className="mb-3">Price History Graph:</h5>
        <div
          className="border border-secondary p-5 text-center text-muted"
          style={{ minHeight: "200px" }}
        >
          [Graph Placeholder]
        </div>
      </div>

      {/* Available on Other Platforms Section */}
      <div>
        <h5 className="mb-3">Available on Other Platforms (Bonus):</h5>
        <ul className="list-group">
          <li className="list-group-item">Flipkart: </li>
          <li className="list-group-item">Meesho: </li>
          <li className="list-group-item">BigBasket: </li>
        </ul>
      </div>
    </div>
  );
}

export default App;
