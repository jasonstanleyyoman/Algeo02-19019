import React, { useState } from 'react';
import axios from 'axios';
import { useDropzone } from 'react-dropzone';
import { useHistory } from 'react-router'
import './style.css';

function DragAndDrop() {
    const [files, setFiles] = useState([]);
    const history = useHistory();
    const { getRootProps, getInputProps } = useDropzone({
        accept: [".txt", ".html", ".pdf"],
        onDrop: (acceptedFiles) => {
          const file = acceptedFiles[0];
          const formData = new FormData();
          formData.append("file", file);
          formData.append("file_1",file);
          axios.post("http://127.0.0.1:5000/upload",formData).
          then((data)=>{
            console.log(data.data);
            history.go(0);
          })
        },
    });

    /* Add Display Function (?) I don't know if dragging works 
    but you can click the div to upload it too */
    return (
        <div className="DragAndDrop">
            <div {...getRootProps()}>
                <input {...getInputProps()}/>
                <p>Drop files here, but fornow it's only clickable .-.</p>
            </div>

        </div>
    );
}
 
export default DragAndDrop;