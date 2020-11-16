import React, {useState, useEffect} from 'react';
import axios from 'axios';
import Collapsible from 'react-collapsible';

import Feed from '../components/Feed';
import Sidebar from '../components/Sidebar';
import '../components/style.css';

import image1 from '../assets/chika-gif1.gif';
import image2 from '../assets/chika-gif2.gif';
import DataTable from '../components/DataTable';

const Searched = ({match}) => {
    const [isLoading, setLoading] = useState(true);
    const [feeds, setFeeds] = useState([]);
    const [titles, setTitles] = useState([]);
    const [terms, setTerms] = useState([]);
    const [query] = useState(match.params.query);


    const showResult = async () => {
            axios({
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    'Access-Control-Allow-Origin' : "*",
                    'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
                },
                url: "http://localhost:5000/searched/" + query,
                data: {}
            })
            .then(response => {
                setFeeds(response.data.ranks);
                setTitles(response.data.titles);
                setTerms(response.data.term);
                setLoading(false);
            })
            .catch((err) => {

            })
    }

    useEffect(() => {
        showResult();
    },[]);

    let component = ""
    if (isLoading) {
        component = (
                    <div className='feed'>
                        <img src ={image2} className='img-fluid self-align-center loading-img' alt="test"/>
                        <div className='m-4'></div>
                        <p className='loading-text'>
                            Waiting for Kaguya, ettou...<br/>
                            I mean loading, yeah loading...</p>
                    </div>)
    } else {
        if (feeds.length === 0) {
            component = (
                        <div className='col feed'>
                            <img src ={image1} className='img-fluid self-align-center loading-img' alt="test"/>
                            <div className='m-4'></div>
                            <p className='loading-text'>
                                Bummer, no data found.<br/>
                                Try searching other things.</p>
                        </div>)
        } else {
            component = feeds.map((feed, index) =>
                <div key={`${index}-feed-${match}-${feed.links}`}>
                    <Feed links={feed.links} similarity={feed.similarity} title={feed.title} sentence={feed.first_15_words} total_words={feed.total_words}/>
                </div>
            )
        }
    }


    return(
        <div className='container no-mar no-pad'>
            <div className='row wrapper'>
                <div className='col-4 no-pad cell'>
                    <Sidebar />
                </div>
                <div className='col-7 d-flex cell'>
                    <div className='col'>
                        {component}
                        <Collapsible trigger='Search Result Details' classParentString='res-feed' className='res-text' openedClassName='res-text'>
                            <br></br>
                            <DataTable titles={titles} terms={terms}/>
                        </Collapsible>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Searched
