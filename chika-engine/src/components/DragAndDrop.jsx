import React, { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import axios from 'axios';
import { useDropzone } from 'react-dropzone';
import { useHistory } from 'react-router'
import { useProgressbar } from "../context/ProgressbarContext"
import './style.css';

import image1 from '../assets/chika-trans.png';

function DragAndDrop() {
    const [files, setFiles] = useState(null);
    const history = useHistory();
    const progressbar = useProgressbar()
    const { getRootProps, getInputProps } = useDropzone({
        maxFiles : 1,
        multiple : false,
        accept: [".txt", ".html", ".pdf"],
        onDrop: (acceptedFiles) => {
          const file = acceptedFiles[0];
          setFiles(file)

        },
    });

    const handleRemove = () => {
        setFiles(null)
    }

    const handleUpload = () => {

        let formData = new FormData()
        formData.append("file",files)
        formData.append("file_1",files)
        axios.post("http://127.0.0.1:5000/upload",formData, {
            onUploadProgress: (ProgressEvent) => {
				progressbar.setValue((ProgressEvent.loaded / ProgressEvent.total) * 100);
			}
        }).
        then((data)=>{
          console.log(data.data);
          history.go(0);
        })


    }

    useEffect(() => {
        return setFiles(null)
    },[])

    return (
        <div className="dragndrop__container">
            <div {...getRootProps({className : "dropzone"})}>
                <input {...getInputProps()}/>
                {
                    !files ?
                    <div>
                        <div class='d-flex row'>
                            <div class='col-4 no-pad d-flex justify-content-end'>
                                <img src={image1} class='image1'/>
                            </div>
                            <div class='col d-flex justify-content-center align-items-center flex-column'>
                                <p class='draganddrop'>Drag and drop your files here</p> 
                                <p class='draganddrop'>or</p>  
                                <p class='draganddrop'>Click to select files</p>  
                            </div>
                        </div> 
                    </div>:
                    <div class='d-flex row'>
                    <div class='col-4 no-pad d-flex justify-content-end'>
                        <img src={image1} class='image1'/>
                    </div>
                    <div className="col File__container d-flex justify-content-center">
                        <p class='draganddrop'>Filename : {files.name}</p>

                    </div>
                </div> 


                }

            </div>
            {
                files ?
                <div className="Button__container">
                    <Button onClick={handleRemove} variant="tombol">
                        REMOVE
                    </Button>
                    <Button onClick={handleUpload} variant="tombol">
                        UPLOAD FILE
                    </Button>
                </div> :
                null
            }

        </div>
    );
}

export default DragAndDrop;
