import React, { useState } from 'react';
import BackgroundSlider from 'react-background-slider';
import './App.css';
import AboutUs from './components/AboutUs';
import UploadDocument from './components/UploadDocument';
import SearchBar from './components/SearchBar';
import SearchFeed from './components/SearchFeed';

import image1 from './assets/chika-bg1.jpg';
import image2 from './assets/chika-bg2.jpg';
import image4 from './assets/chika-bg4.jpg';
import image5 from './assets/chika-bg6.jpg';
import image6 from './assets/chika-bg7.jpg';

const App = () => {
  const [keyword, setKeyword] = useState("");


  return (
    <div className="App">
      <div className="container page-size">
        <BackgroundSlider
          images={[image1, image2, image4, image5, image6]}
          duration={15}
          transition={1}
        />

        <div className="row margin-top-half">
          <div className="col-5 title-bubble">
            <h1 className="title-app">Chika Engine Alpha Ver</h1>
            <h3 class="subtitle-app">藤原千花エンジン</h3>
            <h3 class="slogan-app">for all your anime needs</h3>

          </div>

        </div>

        <div class="row margin-top-bot">
          <div class="col-3"> <AboutUs /> </div>
          <div class="col"> <UploadDocument /> </div>
        </div>

        <SearchBar setKeyword={setKeyword} keyword={keyword} />
        <SearchFeed keyword={keyword} />

      </div>

      {/* <br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br> */}
      <div id="search-feed">
        <h4>Yuhuuu you found a placeholder, also ignore those brs ehe</h4>
      </div>

      <div class="d-flex footer justify-content-center">
        <p>Chika Engine created by someone.</p>
      </div>
    </div>
  );
}

export default App;

