import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import './style.css';

function DragAndDrop() {
    const [files, setFiles] = useState([]);

    const { getRootProps, getInputProps } = useDropzone({
        accept: ".html",
        onDrop: (acceptedFiles) => {
          setFiles(
            acceptedFiles.map((file) =>
              Object.assign(file, {
                preview: URL.createObjectURL(file),
              })
            )
          )
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