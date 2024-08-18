import React from "react";

function PublicLayout({ children }) {
    return (<div>
        <div className="header">
      <div><p>Logo</p></div>
      <ul>
        <li><a href="#">About</a></li>
        <li><a href="#">Projects</a></li>
        <li><a href="#">Content</a></li>
      </ul>
    </div>
    <div>
        {children}
    </div>
        </div>);
}

export default PublicLayout;
