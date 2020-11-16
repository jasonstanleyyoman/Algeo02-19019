import React from 'react';
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import { BiExit } from "react-icons/bi"
import { DiGithubAlt } from "react-icons/di"
import { FiInstagram } from "react-icons/fi"
import './style.css';

function MyVerticallyCenteredModal(props) {
    return (
      <Modal
        {...props}
        size="lg"
        dialogClassName="about-us"
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <Modal.Body>
          <BiExit onClick={props.onHide}/>
          <h3 class="about-us-title">Chika Engine</h3>
          <h5 class="about-us-jap">藤原千花エンジン</h5>
          <span className="pembatas"></span>
          <h1>Search Engine</h1>
          <p>
              Chika Engine adalah search engine yang dirancang untuk memenuhi salah satu
              tugas besar mata kuliah di Teknik Informatika, yaitu Aljabar Linear dan Geometri.
              Search engine yang dirancang menggunakan kalkulasi TF-IDF
              (Term Frequency-Inverse Document Frequency) dan cosine similarity.
              Chika Engine dirancang oleh 3 mahasiswa Teknik Informatika angkatan 2019,
              yaitu Jason Stanley Yoman (13519019), Shaffira Alya Mevia (13519083), dan
              Cynthia Rusadi (13519118).
          </p>

          <div className="pembatas"></div>
              <h4 class='loading-text'>How to Use</h4>
              <p>Masukkan query pada search bar kemudian tekan 'Enter'. Atau, bisa juga
                memasukkan files (.html, .txt, .pdf) terlebih dahulu.
                Tekan Search Results Detail untuk melihat tabel</p>
            <div className="pembatas"></div>
          <h1>About Us</h1>
          <div className="aboutus__container">
              <h4>Jason Stanley Yoman</h4>
              <h6>13519019</h6>

                  <div className="social">
                      <div className="social__icon">
                          <a href="https://github.com/jasonstanleyyoman"  target="__blank">
                          <DiGithubAlt />
                          </a>
                          jasonstanleyyoman
                      </div>

                      <div className="social__icon">
                          <a href="https://www.instagram.com/jasonstanley00/"  target="__blank">
                          <FiInstagram />
                          </a>
                          @jasonstanley00

                      </div>

                  </div>
          </div>
          <div className="aboutus__container">
              <h4>Shaffira Alya Mevia</h4>
              <h6>13519083</h6>

                  <div className="social">
                      <div className="social__icon">
                          <a href="https://github.com/salyamevia"  target="__blank">
                          <DiGithubAlt />
                          </a>
                          salyamevia

                      </div>

                      <div className="social__icon">
                          <a href="https://www.instagram.com/salyamevia/"  target="__blank">
                          <FiInstagram />
                          </a>
                          @salyamevia
                      </div>

                  </div>
          </div>
          <div className="aboutus__container">
              <h4>Cynthia Rusadi</h4>
              <h6>13519118</h6>

                  <div className="social">
                      <div className="social__icon">
                          <a href="https://github.com/cyn-rus"  target="__blank">
                          <DiGithubAlt />
                          </a>
                          cyn-rus
                      </div>

                      <div className="social__icon">
                          <a href="https://www.instagram.com/cyn.rus/"  target="__blank">
                          <FiInstagram />
                          </a>
                          @cyn.rus
                      </div>

                  </div>
          </div>
          <div className="pembatas"></div>



        </Modal.Body>
      </Modal>
    );
  }

function AboutUs() {
    const [modalShow, setModalShow] = React.useState(false);

    return (
        <>
        <Button variant="tombol" onClick={() => setModalShow(true)}>
            ABOUT US
        </Button>

        <MyVerticallyCenteredModal
            show={modalShow}
            onHide={() => setModalShow(false)}
        />
        </>
    );
}

export default AboutUs;
