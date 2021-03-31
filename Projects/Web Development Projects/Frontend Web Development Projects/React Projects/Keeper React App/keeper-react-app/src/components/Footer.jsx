import React from "react";

function Footer() {
  const date = new Date();
  const year = date.getFullYear();
  return (
    <footer>
      <p>Copyright ⓒ Kunal Ram Haryani {year} </p>
    </footer>
  );
}

export default Footer;
