<<<<<<< HEAD
import React, { useState } from 'react';
import BackgroundSlider from 'react-background-slider';

import '../App.css';
import AboutUs from '../components/AboutUs';
import UploadDocument from '../components/UploadDocument';
import SearchBar from '../components/SearchBar';

import image1 from '../assets/chika-bg1.jpg';
import image2 from '../assets/chika-bg2.jpg';
import image4 from '../assets/chika-bg4.jpg';
import image5 from '../assets/chika-bg6.jpg';
import image6 from '../assets/chika-bg7.jpg';

const Home = () => {
  const [keyword, setKeyword] = useState("");

  return (
    <div className="App">
      <div className="container">
        <BackgroundSlider
          images={[image1, image2, image4, image5, image6]}
          duration={15}
          transition={1}
        />

        <div className="row margin-top-half">
          <div className="col-5 title-bubble">
            <h1 className="title-app animate__fadeIn">Chika Engine</h1>
            <h3 class="subtitle-app animate__fadeIn">藤原千花エンジン</h3>
            <h3 class="slogan-app animate__fadeIn">for all your anime needs</h3>
          </div>
        </div>

        <div class="row margin-top-bot">
          <div class="col-3"> <AboutUs /> </div>
          <div class="col-3"> <UploadDocument /> </div>
          <div class='col'></div>
        </div>

        <SearchBar setKeyword={setKeyword} keyword={keyword} />
      </div>
    </div>
  );
}

=======
import React, { useState } from 'react';
import BackgroundSlider from 'react-background-slider';

import '../App.css';
import AboutUs from '../components/AboutUs';
import UploadDocument from '../components/UploadDocument';
import SearchBar from '../components/SearchBar';

import image1 from '../assets/chika-bg1.jpg';
import image2 from '../assets/chika-bg2.jpg';
import image4 from '../assets/chika-bg4.jpg';
import image5 from '../assets/chika-bg6.jpg';
import image6 from '../assets/chika-bg7.jpg';

const Home = () => {
  const [keyword, setKeyword] = useState("");

  return (
    <div className="App">
      <div className="container">
        <BackgroundSlider
          images={[image1, image2, image4, image5, image6]}
          duration={15}
          transition={1}
        />

        <div className="row margin-top-half">
          <div className="col-5 title-bubble">
            <h1 className="title-app animate__fadeIn">Chika Engine</h1>
            <h3 class="subtitle-app animate__fadeIn">藤原千花エンジン</h3>
            <h3 class="slogan-app animate__fadeIn">for all your anime needs</h3>
          </div>
        </div>

        <div class="row margin-top-bot">
          <div class="col-3"> <AboutUs /> </div>
          <div class="col-3"> <UploadDocument /> </div>
          <div class='col'></div>
        </div>

        <SearchBar setKeyword={setKeyword} keyword={keyword} />
      </div>
    </div>
  );
}

>>>>>>> 5ac8660f78f95d99ecb50dbaa5dcfcf88601936f
export default Home;