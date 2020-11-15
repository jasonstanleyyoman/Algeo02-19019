import React from 'react';
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
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
          <h3 class="about-us-title">Chika Engine</h3>
          <h5 class="about-us-jap">藤原千花エンジン</h5><br/>
          <p>
          Chika Engine adalah search engine yang dirancang untuk memenuhi salah satu
          tugas besar mata kuliah di Teknik Informatika, yaitu Aljabar Linear dan Geometri.
          Search engine yang dirancang menggunakan kalkulasi TF-IDF
          (Term Frequency-Inverse Document Frequency) dan cosine similarity.
          Chika Engine dirancang oleh 3 mahasiswa Teknik Informatika angkatan 2019,
          yaitu Jason Stanley Yoman (13519019), Shaffira Alya Mevia (13519083), dan
          Cynthia Rusadi (13519118).
          </p>

          <h4 class='loading-text'>How to Use</h4>
          <p>Masukkan query pada search bar kemudian tekan 'Enter'. Atau, bisa juga
            memasukkan files (.html, .txt, .pdf) terlebih dahulu. </p>

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