import React from 'react';
import { Link } from 'react-router-dom';

const SearchBar = ({keyword,setKeyword}) => {
  const BarStyling = {width:"75rem",background:"RGBA(255,255,255,0.8)", border:"none", padding:"1.5rem"};
  
  const something = (event) => {
      if (event.keyCode === 13) {
          alert("Yo Mama")
          document.getElementById("search-feed").scrollIntoView();
      }
  }
  
  return (
    <input 
     style={BarStyling}
     key="random1"
     value={keyword}
     placeholder={"What do you want to know?"}
     //onChange={(e) => setKeyword(e.target.value)}
     onKeyDown={(e) => something(e)}
    />
  );
}

export default SearchBar