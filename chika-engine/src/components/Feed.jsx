import React from 'react';

const Feed = ({links, similarity, title}) => {
    
    return (
        <div>
            <h1>{title}</h1>
            <div>{links}</div>
            <div>{similarity}</div>
        </div>
    );
};

export default Feed;