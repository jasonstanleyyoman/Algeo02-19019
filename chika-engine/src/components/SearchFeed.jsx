import React, {useState, useEffect} from 'react';
import axios from 'axios';

import Feed from './Feed';

const SearchFeed = ({ keyword }) => {
    const [feeds, setFeeds] = useState([]);
    const showResult = async (keyword) => {
            axios({
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                },
                url: "http://localhost:5000/searched/" + keyword, 
                data: {}
            })
            .then(response => {
                console.log(response.data)
            })
            .catch((err) => {
                console.log(err)
            })
    }

    useEffect(() => {
        showResult(keyword);
    }, [keyword]);

    return (
        <>
            {
               feeds.map((feed, index) => (
                   <div key={`${index}-feed-${keyword}`}>
                       <Feed links={feed.links} similarity={feed.similarity} title={feed.title} />
                   </div>
               )) 
            }
        </>
    );
};

export default SearchFeed;