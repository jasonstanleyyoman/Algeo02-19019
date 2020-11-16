import React, {useState, useEffect} from 'react';
import axios from 'axios';
import Collapsible from 'react-collapsible';

import Feed from '../components/Feed';
import Sidebar from '../components/Sidebar';
import '../components/style.css';
import CollapseDiv from '../components/CollapseDiv';

import image1 from '../assets/chika-gif1.gif';
import image2 from '../assets/chika-gif2.gif';
import DataTable from '../components/DataTable';

const Searched = ({match}) => {
    const [isLoading, setLoading] = useState(true);
    const [feeds, setFeeds] = useState([]);
    const [titles, setTitles] = useState([]);
    const [terms, setTerms] = useState([]);
    const [result, setResult] = useState([]);
    const [query, setQuerty] = useState(match.params.query);
    const [keyword, setKeyword] = useState("");

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
                console.log(err)
            })
    }

    useEffect(() => {
        showResult();
    }, []);

    let component = ""
    if (isLoading) {
        component = (
                    <div class='feed'>
                        <img src ={image2} class='img-fluid self-align-center loading-img'/>
                        <div class='m-4'></div>
                        <p class='loading-text'>
                            Waiting for Kaguya, ettou...<br/>
                            I mean loading, yeah loading...</p>
                    </div>)
    } else {
        if (feeds.length === 0) {
            component = (
                        <div class='col feed'>
                            <img src ={image1} class='img-fluid self-align-center loading-img'/>
                            <div class='m-4'></div>
                            <p class='loading-text'>
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

    console.log(result);
    return(
        <div class='container no-mar no-pad'>
            <div class='row wrapper'>
                <div class='col-4 no-pad cell'>
                    <Sidebar />
                </div>
                <div class='col-6 d-flex load cell'>
                    <div class='col'>
                        {component}
                        <Collapsible trigger='Search Result Details' classParentString='feed' className='res-text' openedClassName='res-text'>
                            <DataTable titles={titles} terms={terms}/>
                        </Collapsible>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Searched
