import React from 'react';

const Feed = ({links, similarity, title}) => {
    
    return (
        <div>
            <div>{links}</div>
            <div>{similarity}</div>
            <div>{title}</div>
        </div>
    );
};

export default Feed;