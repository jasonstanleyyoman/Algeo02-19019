import React from 'react';
import AboutUs from './AboutUs';
import { useHistory } from 'react-router-dom';
import Button from 'react-bootstrap/Button';

import './style.css';
import image1 from '../assets/chika-sidenav.jpg';

function Sidebar() {
    const history = useHistory();
    const GoHome = () => history.push('/');

    return (
        <div className='sidebar'>
            <img src={image1} className='w-100 fit-image img-fluid' onClick={GoHome} alt="gatau"/>
            <div className='row container d-flex justify-content-center m-1'>
                <h1 className="title-sidebar">Chika Engine</h1>
            </div>
            <div className='row container d-flex align-items-center m-1'>
                <div className='col no-pad'><h3 className="subtitle-sidebar mx-auto">藤原千花エンジン</h3></div>
                <div className='col no-pad'><h3 className="subtitle-sidebar mx-auto">for all your anime needs</h3></div>
            </div>
            <div className='row container d-flex align-items-center m-1'>
                <div className='col no-pad mx-auto'><AboutUs/></div>
                <div className='col no-pad mx-auto'><Button variant='tombol' onClick={GoHome}>GO BACK</Button>                </div>
            </div>
        </div>
    )
}

export default Sidebar;
