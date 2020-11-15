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
            Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
            dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
            consectetur ac, vestibulum at eros.
            Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
            dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
            consectetur ac, vestibulum at eros.
          </p>
          <div className="pembatas"></div>
          <h1>How to Use</h1>
          <p>
            Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
            dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
            consectetur ac, vestibulum at eros.
            Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
            dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
            consectetur ac, vestibulum at eros.
          </p>
          <p>
            Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
            dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
            consectetur ac, vestibulum at eros.
            Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
            dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
            consectetur ac, vestibulum at eros.
          </p>
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
