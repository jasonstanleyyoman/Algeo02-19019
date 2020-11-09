import React, {useState, useEffect} from 'react';
import axios from 'axios';

import Feed from '../components/Feed';

const Searched = ({match}) => {
    const [isLoading, setLoading] = useState(true);
    const [feeds, setFeeds] = useState([]);
    const [query, setQuerty] = useState(match.params.query);

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
        component = (<div>
                        <p>Now loading...</p>
                    </div>)
    } else {
        if (feeds.length === 0) {
            component = (<div>
                            <p>Page not found</p>
                        </div>)
        } else {
            component = feeds.map((feed, index) =>
                <div key={`${index}-feed-${match}-${feed.links}`}>
                    <Feed links={feed.links} similarity={feed.similarity} title={feed.title} sentence={feed.first_15_words} />
                </div>
            )
        }
    }

    return(
        <div>
            <div>
                {component}
            </div>
        </div>
    )
}

export default Searched
