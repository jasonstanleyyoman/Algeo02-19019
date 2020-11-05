import React from 'react';
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import DragAndDrop from './DragAndDrop.jsx';
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
          <h3>Upload you document</h3>

          <DragAndDrop />

        </Modal.Body>
      </Modal>
    );
  }


function UploadDocument() {
    const [modalShow, setModalShow] = React.useState(false);

    return (
        <>
        <Button variant="tombol" onClick={() => setModalShow(true)}>
            UPLOAD DOCUMENT
        </Button>

        <MyVerticallyCenteredModal
            show={modalShow}
            onHide={() => setModalShow(false)}
        />
        </>
    );
} 

export default UploadDocument;
