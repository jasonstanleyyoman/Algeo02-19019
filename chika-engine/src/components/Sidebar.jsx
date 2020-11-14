import React from 'react';
import UploadDocument from './UploadDocument';
import AboutUs from './AboutUs';
import { useHistory } from 'react-router-dom';
import './style.css';

import image1 from '../assets/chika-sidenav.jpg';

function Sidebar() {
    const history = useHistory();
    const GoHome = () => history.push('/');
    
    return (
        <div class='sidebar'>
            <img src={image1} class='w-100 fit-image img-fluid' onClick={GoHome}/>
            <div class='row container d-flex justify-content-center m-1'>
                <h1 className="title-sidebar">Chika Engine</h1>
            </div>
            <div class='row container d-flex align-items-center m-1'>
                <div class='col no-pad'><h3 class="subtitle-sidebar mx-auto">藤原千花エンジン</h3></div>
                <div class='col no-pad'><h3 class="subtitle-sidebar mx-auto">for all your anime needs</h3></div>
            </div>
            <div class='row container d-flex align-items-center m-1'>
                <div class='col no-pad mx-auto'><AboutUs/></div>
                <div class='col no-pad mx-auto'><UploadDocument/></div>
            </div>
        </div>
    )
}
 
export default Sidebar;