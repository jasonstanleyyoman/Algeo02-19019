import React, { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import axios from 'axios';
import { useDropzone } from 'react-dropzone';
import { useHistory } from 'react-router'
import { useProgressbar } from "../context/ProgressbarContext"
import './style.css';

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

    /* Add Display Function (?) I don't know if dragging works
    but you can click the div to upload it too */
    return (
        <div className="dragndrop__container">
            <div {...getRootProps({className : "dropzone"})}>
                <input {...getInputProps()}/>
                {
                    !files ?
                    <p>Drag 'n' drop some files here, or click to select files</p> :
                    <div className="File__container">
                        <p>Filename : {files.name}</p>

                    </div>


                }

            </div>
            {
                files ?
                <div className="Button__container">
                    <Button onClick={handleRemove} variant="tombol">
                        Remove
                    </Button>
                    <Button onClick={handleUpload} variant="tombol">
                        Upload
                    </Button>
                </div> :
                null
            }

        </div>
    );
}

export default DragAndDrop;
