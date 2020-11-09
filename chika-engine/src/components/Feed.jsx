import React from 'react';

const Feed = ({links, similarity, title, sentence}) => {
    
    return (
        <div>
            <h2><a href={links}target="_blank">{title}</a></h2>
            <div>Tingkat kemiripan: {similarity}%</div>
            <div>{sentence}</div>
        </div>
    );
};

export default Feed;