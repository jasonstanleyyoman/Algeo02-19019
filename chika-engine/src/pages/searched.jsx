import React, {useState, useEffect} from 'react';
import axios from 'axios';

import Feed from '../components/Feed';
import Sidebar from '../components/Sidebar';
import SearchBar from '../components/SearchBar';
import '../components/style.css';

import image from '../assets/chika-gif1.gif';
import image2 from '../assets/chika2.jpg';

const Searched = ({match}) => {
    const [isLoading, setLoading] = useState(true);
    const [feeds, setFeeds] = useState([]);
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
                console.log(response.data);
                setFeeds(response.data.data);
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
                    <div class='container'>
                        <img src ={image} class='img-fluid self-align-center loading-img'/>
                            <div class='loading-text'><h1><span></span></h1></div>
                        
                    </div>)
    } else {
        if (feeds.length === 0) {
            component = (<div>
                            <SearchBar setKeyword={setKeyword} keyword={keyword} />
                            <div class='feed'>
                                <img src ={image2} class='img-fluid self-align-center loading-img'/>
                                <p class='loading-text'>Bummer, no data found.</p>
                            </div>
                        </div>)
        } else {
            component = feeds.map((feed, index) =>
                <div>
                    <SearchBar setKeyword={setKeyword} keyword={keyword} />
                    <div key={`${index}-feed-${match}-${feed.links}`}>
                        <Feed links={feed.links} similarity={feed.similarity} title={feed.title} sentence={feed.first_15_words} total_words={feed.total_words}/>
                    </div>
                </div>
            )
        }
    }

    return(
        <div class='container no-mar no-pad'>
            <div class='row'>
                <div class='col-4 no-pad'>
                    <Sidebar />
                </div>
                <div class='col d-flex load'>
                    {component}
                </div>
            </div>
        </div>
    )
}

export default Searched
