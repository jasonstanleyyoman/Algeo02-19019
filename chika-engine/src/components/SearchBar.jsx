import React  from 'react';
import { useHistory, Link } from 'react-router-dom';

const BarStyling = {width:"70rem",background:"RGBA(255,255,255,0.8)", border:"none", padding:"1.5rem"};

const SearchBar = ({keyword,setKeyword}) => {
  const history = useHistory();

  const redirect = (event) => {
      // when enter, redirects
      if (event.keyCode === 13) {
          //alert("Yo Mama")
          // document.getElementById("search-feed").scrollIntoView();
          history.push('searched/' + keyword)
      }
  }

  return ( 
    <input 
     style={BarStyling}
     key="random1"
     value={keyword}
     placeholder={"What do you want to know?"}
     onChange={(e) => setKeyword(e.target.value)}
     onKeyDown={(e) => redirect(e)}
    />
  );
}

export default SearchBar