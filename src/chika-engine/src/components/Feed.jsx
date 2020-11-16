import React from 'react';
import './style.css';

const Feed = ({links, similarity, title, sentence, total_words}) => {

    return (
        <div className='feed'>
            <div className='row'>
                <h2 className='feed-title'><a href={links}target="_blank" rel="noreferrer">{title}</a></h2>
                <div className='feed-text'><p>{sentence}</p></div>
            </div>
            <div className='row'>
                <div className='col-3'>
                    <div className='row feed-subtext-title'>Total Words</div>
                    <div className='row feed-subtext-info'>{total_words}</div>
                </div>
                <div className='col-3'>
                    <div className='row feed-subtext-title'>Similarity</div>
                    <div className='row feed-subtext-info' >{Math.round((similarity + Number.EPSILON) * 100)}%</div>
                </div>
                <div className='col'></div>
            </div>

        </div>
    );
};

export default Feed;
